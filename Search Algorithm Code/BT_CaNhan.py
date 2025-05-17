import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import solver
import time
from collections import Counter
import copy
import threading

WIDTH, HEIGHT = 1300, 730

start_state = ((2, 3, 6)
              ,(1, 5, 0)
              ,(4, 7, 8))
goal_state = ((1, 2, 3)
             ,(4, 5, 6)
             ,(7, 8, 0))
start_entries = []
goal_entries = []


solution = []
node = 0
running_algorithm = False
skip_requested = False

def is_valid_state(state):
    """
    Kiểm tra xem một trạng thái của bài toán 8-puzzle (ô chữ) có hợp lệ hay không.
    Trạng thái hợp lệ phải chứa các số từ 0 đến 8 và mỗi số chỉ xuất hiện một lần.
    """
    flat = [num for row in state for num in row]
    counter = Counter(flat)
    if set(flat) != set(range(9)):
        return False
    for val in range(9):
        if counter[val] != 1:
            return False
    return True

def draw_board(frame, state, entries_list):
    """
    Vẽ bảng (ô chữ) 8-puzzle lên một khung (frame) giao diện người dùng (GUI) cho trước,
    sử dụng các ô nhập liệu (Entry) để hiển thị và cho phép chỉnh sửa trạng thái.
    """
    def validate_input(char):
        return char in '12345678' or char == ''

    vcmd = (root.register(validate_input), '%P')

    for i in range(3):
        row_entries = []
        for j in range(3):
            value = state[i][j]
            entry = tk.Entry(frame, bg = "#FFFFCC", font=("Arial", 16, "bold"), width=5, justify="center",
                             validate="key", validatecommand=vcmd)
            entry.grid(row=i, column=j, ipadx=10, ipady=22)
            if value != 0:
                entry.insert(0, str(value))
            row_entries.append(entry)
        entries_list.append(row_entries)

def get_state_from_entries(entries):
    """
    Lấy trạng thái hiện tại của ô chữ từ các ô nhập liệu (Entry widget) trên giao diện
    người dùng và chuyển đổi thành dạng tuple các tuple.
    """
    state = []
    for row in entries:
        current_row = []
        for entry in row:
            value = entry.get()
            current_row.append(int(value) if value.isdigit() else 0)
        state.append(tuple(current_row))
    return tuple(state)


def run_algorithm(algo):
    """
    Thực thi thuật toán giải đố 8-puzzle được chọn (ví dụ: BFS, DFS, A*, v.v.).
    Hàm này lấy trạng thái đầu và đích từ giao diện, kiểm tra tính hợp lệ,
    sau đó gọi hàm giải tương ứng từ module `solver`. Cuối cùng, nó hiển thị
    lời giải hoặc kết quả tìm kiếm.
    """
    global solution, node, running_algorithm, start_state, goal_state
    if running_algorithm:
        return

    start_state = get_state_from_entries(start_entries)
    goal_state = get_state_from_entries(goal_entries)
    if algo != "No Observation Search" and algo != "Partial Observation Search":
        if not is_valid_state(start_state):
            messagebox.showerror("Lỗi", "START STATE không hợp lệ. Phải chứa đủ các số từ 1 đến 8, không lặp và có đúng 1 ô trống.")
            return
        if not is_valid_state(goal_state):
            messagebox.showerror("Lỗi", "GOAL STATE không hợp lệ. Phải chứa đủ các số từ 1 đến 8, không lặp và có đúng 1 ô trống.")
            return

    running_algorithm = True
    disable_buttons()

    if algo == "BFS":
        solution, node = solver.bfs_solve(start_state, goal_state)
    elif algo == "DFS":
        solution, node = solver.dfs_solve(start_state, goal_state)
    elif algo == "UCS":
        solution, node = solver.ucs_solve(start_state, goal_state)
    elif algo == "IDS":
        solution, node = solver.ids_solve(start_state, goal_state)
    elif algo == "Greedy":
        solution, node = solver.greedy_solve(start_state, goal_state)
    elif algo == "A Star":
        solution, node = solver.a_star_solve(start_state, goal_state)
    elif algo == "IDA Star":
        solution, node = solver.ida_star_solve(start_state, goal_state)
    elif algo == "Simple Hill Climbing":
        solution, node = solver.simple_hill_climbing_solve(start_state, goal_state)
    elif algo == "Hill Climbing":
        solution, node = solver.hill_climbing_solve(start_state, goal_state)
    elif algo == "Stochastic Hill Climbing":
        solution, node = solver.Stochastic_hill_climbing_solve(start_state, goal_state)
    elif algo == "Simulated Annealing":
        solution, node = solver.Simulated_Annealing_solve(start_state, goal_state)
    elif algo == "Beam Search":
        solution, node = solver.beam_search_solve(start_state, goal_state)
    elif algo == "And-Or Graph Search":
        solution = solver.and_or_graph_search(start_state, goal_state)
    elif algo == "Genetic Algorithm":
        solution = solver.genetic_algorithm_solve(start_state, goal_state)
    elif algo == "No Observation Search":
        results_special, generated_starts_special, generated_goals_special = solver.no_observation_search()
    elif algo == "Partial Observation Search":
        results_special, generated_starts_special, generated_goals_special = solver.partial_observation_search(goal_state)
    elif algo == "Generate and Test":
        results_special, generated_starts_special, generated_goals_special = solver.generate_and_test(goal_state), [], [goal_state]
    elif algo == "Q-Learning":
        solution = solver.q_learning(start_state, goal_state)

    if algo != "No Observation Search" and algo != "Partial Observation Search" and algo != "Generate and Test" and algo != "AC-3":
        display_solution()
    else:
        display_belief_search_results(results_special, algo, generated_starts_special, generated_goals_special)

    enable_buttons()
    running_algorithm = False





def show_backtracking():
    def start_backtracking():
        for cell in cells:
            cell.config(text="", bg="white")

        log_text.delete("1.0", tk.END)
        solution, trace_log = solver.backtracking()

        def step_by_step():
            for line in trace_log:
                parts = line.split()
                if parts[0] == "Xét":
                    parts_line = line.split()
                    idx = int(parts_line[2][:-1])
                    val = parts_line[5]

                    if "không hợp lệ" in line:
                        cells[idx].config(text=val, bg="lightcoral")
                    else:
                        cells[idx].config(text=val, bg="lightgreen")
                elif "Quay lui" in line:
                    idx = int(line.split()[9])
                    cells[idx].config(text="", bg="white")

                log_text.insert(tk.END, line + "\n")
                if ("hợp lệ" in line and "không hợp lệ" not in line) or "Quay lui" in line:
                    log_text.insert(tk.END, "="*30 + "\n")
                log_text.see(tk.END)
                time.sleep(1.0 - speed_scale.get())

        threading.Thread(target=step_by_step).start()

    window = tk.Toplevel()
    window.title("Backtracking Visualization")
    win_width, win_height = 460, 580
    window.geometry(f"{win_width}x{win_height}")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_pos = (screen_width // 2) - (win_width // 2)
    y_pos = (screen_height // 2) - (win_height // 2)
    window.geometry(f"+{x_pos}+{y_pos}")

    tk.Label(window, text="Ràng buộc 1: Giá trị các ô phải khác nhau.", font=("Arial", 12, "italic")).pack(anchor="n", padx=10)
    tk.Label(window,  text="Ràng buộc 2: Giá trị Ô_i > Giá_trị Ô_j nếu chỉ số i < j.", font=("Arial", 12, "italic")).pack(anchor="n", padx=10)

    grid_frame = ttk.Frame(window)
    grid_frame.pack(pady=10)
    cells = []
    for i in range(3):
        for j in range(3):
            lbl = tk.Label(grid_frame, text="", width=6, height=3, relief="solid", font=("Arial", 14), bg="white")
            lbl.grid(row=i, column=j, padx=5, pady=5)
            cells.append(lbl)

    ttk.Button(window, text="Start Backtracking", command=start_backtracking).pack(pady=10)

    speed_frame = ttk.Frame(window)
    speed_frame.pack(pady=5)
    tk.Label(speed_frame, text="Speed:").pack(side="left", padx=5)
    speed_scale = tk.Scale(speed_frame, from_=0.0, to=1.0, resolution=0.1, orient="horizontal", length=200)
    speed_scale.set(1.0)
    speed_scale.pack(side="left")

    log_frame = ttk.LabelFrame(window, text="Lịch sử log", padding=10)
    log_frame.pack(padx=10, pady=10, fill="both", expand=True)

    scrollbar = ttk.Scrollbar(log_frame)
    scrollbar.pack(side="right", fill="y")

    log_text = tk.Text(log_frame, height=10, yscrollcommand=scrollbar.set, wrap="word")
    log_text.pack(fill="both", expand=True)
    scrollbar.config(command=log_text.yview)





selected_constraint = None
def open_ac3_visualization_setup_form():
    """
    Mở một cửa sổ mới để người dùng chọn các ràng buộc cho thuật toán AC-3
    trước khi bắt đầu trực quan hóa.
    """
    initial_domains_for_ac3 = [set(range(9)) for _ in range(9)]
    def start_ac3_based_on_constraint():
        global selected_constraint
        selected_constraint = constraint_choice.get()
        if selected_constraint == "Giá trị Ô_i < Giá_trị Ô_j nếu chỉ số i < j.":
            final_domains, execution_log = solver.ac3("increasing")
        elif selected_constraint == "Tổng giá trị (Ô_i +  Ô_j) >= Tổng chỉ số (i + j).":
            final_domains, execution_log = solver.ac3("sum")
        
        setup_window.destroy()
        display_ac3_visualization(final_domains, execution_log, initial_domains_for_ac3)

    setup_window = tk.Toplevel(root)
    win_width, win_height = 400, 200
    setup_window.geometry(f"{win_width}x{win_height}")
    screen_width = setup_window.winfo_screenwidth()
    screen_height = setup_window.winfo_screenheight()
    x_pos = (screen_width // 2) - (win_width // 2)
    y_pos = (screen_height // 2) - (win_height // 2)
    setup_window.geometry(f"+{x_pos}+{y_pos}")

    setup_window.transient(root)
    setup_window.grab_set()

    tk.Label(setup_window, text="Chọn ràng buộc AC-3:", font=("Arial", 12)).pack(pady=10)

    constraint_choice = tk.StringVar()
    combo = ttk.Combobox(setup_window, textvariable=constraint_choice, state="readonly",
                         font=("Arial", 11), width=35)
    combo['values'] = ["Giá trị Ô_i < Giá_trị Ô_j nếu chỉ số i < j.", "Tổng giá trị (Ô_i +  Ô_j) >= Tổng chỉ số (i + j)."]
    combo.current(0)
    combo.pack(pady=10)

    start_button = tk.Button(setup_window, text="Chạy thuật toán AC-3",
                             font=("Arial", 11, "bold"), bg="#27ae60", fg="white",
                             command=start_ac3_based_on_constraint)
    start_button.pack(pady=10)

ac3_board_cell_frames = [] 
ac3_log_text_widget = None
ac3_animation_delay = 400 
AC3_CELL_PIXEL_WIDTH = 80  
AC3_CELL_PIXEL_HEIGHT = 80 
ac3_speed_up_active = False 

def get_cell_normal_bg(domain_set):
    """
    Xác định màu nền cho một ô trên bảng trực quan hóa AC-3 dựa trên
    tập miền (domain) hiện tại của ô đó (ví dụ: màu xanh lá nếu miền
    chỉ còn một giá trị, màu đỏ nếu miền rỗng).
    """
    if not domain_set:
        return "#FFCCCC"  
    elif len(domain_set) == 1:
        return "#CCFFCC"  
    return "white"      

def update_ac3_board_display(domains_to_display):
    """
    Cập nhật hiển thị trực quan của bảng AC-3, thể hiện các miền
    giá trị hiện tại của mỗi ô.
    """
    global ac3_board_cell_frames 
    for r in range(3):
        for c in range(3):
            cell_idx = r * 3 + c
            if cell_idx < len(domains_to_display):
                domain = domains_to_display[cell_idx] 
            else:
                domain = set() 

            text_to_display = ""
            new_font_tuple = ("Arial", 8, "bold") 
            
            if not domain:
                text_to_display = "Ø" 
                new_font_tuple = ("Arial", 24, "bold") 
            elif len(domain) == 1:
                text_to_display = str(list(domain)[0])
                new_font_tuple = ("Arial", 30, "bold") 
            else:
                sorted_domain = sorted(list(domain))
                if len(sorted_domain) <= 3: 
                    text_to_display = ", ".join(map(str, sorted_domain))
                    new_font_tuple = ("Arial", 18, "bold") 
                elif len(sorted_domain) <= 6: 
                    line1 = ", ".join(map(str, sorted_domain[:3]))
                    line2 = ", ".join(map(str, sorted_domain[3:len(sorted_domain)])) 
                    text_to_display = f"{line1}\n{line2}"
                    new_font_tuple = ("Arial", 10, "bold") 
                else: 
                    line1 = ", ".join(map(str, sorted_domain[:3]))
                    line2 = ", ".join(map(str, sorted_domain[3:6]))
                    line3 = ", ".join(map(str, sorted_domain[6:]))
                    text_to_display = f"{line1}\n{line2}\n{line3}"
                    new_font_tuple = ("Arial", 8, "bold") 

            bg_color = get_cell_normal_bg(domain)
            
            if r < len(ac3_board_cell_frames) and c < len(ac3_board_cell_frames[r]) and ac3_board_cell_frames[r][c]:
                cell_frame = ac3_board_cell_frames[r][c] 
                if cell_frame.winfo_children():
                    label_widget = cell_frame.winfo_children()[0]
                    label_widget.config(text=text_to_display, font=new_font_tuple, bg=bg_color) 
                cell_frame.config(bg=bg_color) 


def highlight_arc_cells(xi_idx, xj_idx, highlight=True):
    """
    Làm nổi bật (hoặc bỏ nổi bật) các ô liên quan đến một cung (Xi, Xj)
    đang được xử lý trong thuật toán AC-3 trên bảng trực quan.
    """
    global ac3_board_cell_frames 
    
    bg_xi_normal = "white" 
    bg_xj_normal = "white" 

    if hasattr(solver, 'current_ac3_domains_for_display') and \
       solver.current_ac3_domains_for_display and \
       xi_idx < len(solver.current_ac3_domains_for_display) and \
       xj_idx < len(solver.current_ac3_domains_for_display):
        bg_xi_normal = get_cell_normal_bg(solver.current_ac3_domains_for_display[xi_idx])
        bg_xj_normal = get_cell_normal_bg(solver.current_ac3_domains_for_display[xj_idx])

    color_xi_eff = "lightgreen" if highlight else bg_xi_normal
    color_xj_eff = "lightgreen" if highlight else bg_xj_normal
    
    row_i, col_i = divmod(xi_idx, 3)
    row_j, col_j = divmod(xj_idx, 3)
    
    if len(ac3_board_cell_frames) > row_i and len(ac3_board_cell_frames[row_i]) > col_i and \
       ac3_board_cell_frames[row_i][col_i] and \
       len(ac3_board_cell_frames) > row_j and len(ac3_board_cell_frames[row_j]) > col_j and \
       ac3_board_cell_frames[row_j][col_j]:
        
        frame_xi = ac3_board_cell_frames[row_i][col_i]
        frame_xj = ac3_board_cell_frames[row_j][col_j]
        
        frame_xi.config(bg=color_xi_eff)
        if frame_xi.winfo_children(): 
            frame_xi.winfo_children()[0].config(bg=color_xi_eff)

        frame_xj.config(bg=color_xj_eff)
        if frame_xj.winfo_children(): 
            frame_xj.winfo_children()[0].config(bg=color_xj_eff)

def speed_up_ac3_animation_action(button_widget):
    """
    Đặt độ trễ của hoạt ảnh AC-3 về 0 để tăng tốc độ trực quan hóa
    và vô hiệu hóa nút tăng tốc.
    """
    global ac3_animation_delay, ac3_speed_up_active
    ac3_animation_delay = 0
    ac3_speed_up_active = True
    if button_widget:
        button_widget.config(text="Speed: Max", state=tk.DISABLED, bg="grey") 
def animate_ac3_steps(log_iterator, ac3_window, initial_domains_for_log_build, speed_up_button):
    """
    Tạo hoạt ảnh cho các bước của thuật toán AC-3, cập nhật bảng và
    nhật ký (log) theo từng bước xử lý cung.
    """
    global ac3_log_text_widget, ac3_animation_delay, ac3_speed_up_active
    try:
        entry = next(log_iterator)
        
        arc_xi_name, arc_xj_name = entry['arc_processed']
        xi_idx = int(arc_xi_name[1:]) 
        xj_idx = int(arc_xj_name[1:])

        ac3_log_text_widget.config(state="normal")
        log_line_header = f"Xét cung: ({arc_xi_name} ← {arc_xj_name})\n"
        log_line_before = f"  Miền {arc_xi_name} trước: {entry['xi_domain_before']}\n" \
                          f"  Miền {arc_xj_name} (tham chiếu): {entry['xj_domain_before']}\n"
        ac3_log_text_widget.insert(tk.END, log_line_header + log_line_before)
        ac3_log_text_widget.see(tk.END)
        
        highlight_arc_cells(xi_idx, xj_idx, True)
        ac3_window.update_idletasks() 

        def after_highlight_and_revise():
            global ac3_speed_up_active 
            if hasattr(solver, 'current_ac3_domains_for_display') and solver.current_ac3_domains_for_display:
                 solver.current_ac3_domains_for_display[xi_idx] = set(entry['xi_domain_after_revise'])
                 update_ac3_board_display(solver.current_ac3_domains_for_display)
            
            log_line_after = f"  Miền {arc_xi_name} sau: {entry['xi_domain_after_revise']}\n"
            if entry['was_revised']: 
                log_line_after += f"  => Miền của {arc_xi_name} đã thay đổi.\n"
            else:
                log_line_after += f"  => Miền của {arc_xi_name} không thay đổi.\n"
            
            ac3_log_text_widget.insert(tk.END, log_line_after + "="*55 + "\n")
            ac3_log_text_widget.see(tk.END) 
            ac3_log_text_widget.config(state="disabled")

            highlight_arc_cells(xi_idx, xj_idx, False)
            ac3_window.update_idletasks()

            current_delay = 0 if ac3_speed_up_active else ac3_animation_delay
            ac3_window.after(current_delay, lambda: animate_ac3_steps(log_iterator, ac3_window, initial_domains_for_log_build, speed_up_button))

        current_delay_highlight = 0 if ac3_speed_up_active else ac3_animation_delay // 2
        ac3_window.after(current_delay_highlight, after_highlight_and_revise)

    except StopIteration:
        ac3_log_text_widget.config(state="normal")
        ac3_log_text_widget.insert(tk.END, "AC-3 hoàn thành.\n")
        if hasattr(solver, 'ac3_final_domains_global') and solver.ac3_final_domains_global is None: 
             ac3_log_text_widget.insert(tk.END, "Phát hiện không nhất quán (một miền rỗng).\n", "error_tag")
             ac3_log_text_widget.tag_config("error_tag", foreground="red")
        ac3_log_text_widget.config(state="disabled")
        if speed_up_button:
             speed_up_button.config(text="Speed Up", state=tk.NORMAL, bg="#f39c12")
        ac3_speed_up_active = False
        messagebox.showinfo("AC-3", "Quá trình AC-3 đã hoàn tất!")
    except Exception as e:
        ac3_log_text_widget.config(state="normal")
        ac3_log_text_widget.insert(tk.END, f"Lỗi trong quá trình animation: {e}\n", "error_tag")
        ac3_log_text_widget.tag_config("error_tag", foreground="red")
        ac3_log_text_widget.config(state="disabled")
        if speed_up_button:
            speed_up_button.config(text="Speed Up", state=tk.NORMAL, bg="#f39c12")
        ac3_speed_up_active = False
        messagebox.showerror("Lỗi AC-3", f"Đã xảy ra lỗi: {e}")


def display_ac3_visualization(final_domains, execution_log, initial_domains_for_ac3):
    """
    Tạo và hiển thị cửa sổ trực quan hóa cho thuật toán AC-3, bao gồm
    bảng trạng thái các miền và nhật ký thực thi.
    """
    global root, ac3_board_cell_frames, ac3_log_text_widget, ac3_animation_delay, ac3_speed_up_active
    
    ac3_speed_up_active = False 
    ac3_animation_delay = 400  

    ac3_window = tk.Toplevel(root)
    ac3_window.title("Trực quan hóa Thuật toán AC-3")
    win_width, win_height = 800, 800
    ac3_window.geometry(f"{win_width}x{win_height}")
    screen_width = ac3_window.winfo_screenwidth()
    screen_height = ac3_window.winfo_screenheight()
    x_pos = (screen_width // 2) - (win_width // 2)
    y_pos = (screen_height // 2) - (win_height // 2)
    ac3_window.geometry(f"+{x_pos}+{y_pos}")

    constraints_info_frame = tk.Frame(ac3_window, pady=5)
    constraints_info_frame.pack(fill=tk.X)
    tk.Label(constraints_info_frame, 
             text="Ràng buộc 1: Giá trị các ô phải khác nhau.",
             font=("Arial", 12, "italic")).pack(anchor="n", padx=10)
    tk.Label(constraints_info_frame, 
             text=f"Ràng buộc 2: {selected_constraint}",
             font=("Arial", 12, "italic")).pack(anchor="n", padx=10)

    top_frame = tk.Frame(ac3_window)
    top_frame.pack(pady=5)

    board_display_frame = tk.Frame(top_frame)
    board_display_frame.pack(side=tk.LEFT, padx=10)

    speed_up_button = tk.Button(top_frame, text="Speed Up", 
                                command=lambda: speed_up_ac3_animation_action(speed_up_button),
                                bg="#f39c12", fg="white", font=("Arial", 10, "bold"),
                                width=15, height=2)
    speed_up_button.pack(side=tk.LEFT, padx=10, pady=10, anchor="center")


    ac3_board_cell_frames = [[None for _ in range(3)] for _ in range(3)] 
    
    cell_pixel_width = AC3_CELL_PIXEL_WIDTH 
    cell_pixel_height = AC3_CELL_PIXEL_HEIGHT

    for r in range(3):
        for c in range(3):
            cell_idx = r * 3 + c
            domain = initial_domains_for_ac3[cell_idx] 
            
            sorted_domain = sorted(list(domain))
            text_to_display = f"{', '.join(map(str, sorted_domain[:3]))}\n" \
                              f"{', '.join(map(str, sorted_domain[3:6]))}\n" \
                              f"{', '.join(map(str, sorted_domain[6:]))}"
            initial_font_tuple = ("Arial", 8, "bold") 
            
            cell_container = tk.Frame(board_display_frame, 
                                      width=cell_pixel_width, 
                                      height=cell_pixel_height,
                                      borderwidth=1, relief="solid", bg="white") 
            cell_container.grid(row=r, column=c, padx=2, pady=2)
            cell_container.grid_propagate(False) 
            ac3_board_cell_frames[r][c] = cell_container 

            lbl = tk.Label(cell_container, text=text_to_display,
                           font=initial_font_tuple, 
                           bg="white", 
                           justify="center",
                           anchor="center") 
            lbl.place(relx=0.5, rely=0.5, anchor="center")
    
    log_frame = tk.Frame(ac3_window, pady=5)
    log_frame.pack(fill=tk.BOTH, expand=True)
    
    tk.Label(log_frame, text="Log Thực Thi AC-3:", font=("Arial", 12, "bold")).pack(anchor="w", padx=5)
    ac3_log_text_widget = scrolledtext.ScrolledText(log_frame, height=15, width=90, wrap=tk.WORD, font=("Courier New", 11))
    ac3_log_text_widget.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    ac3_log_text_widget.config(state="disabled")

    if final_domains is None:
        ac3_log_text_widget.config(state="normal")
        ac3_log_text_widget.insert(tk.END, "AC-3 phát hiện không nhất quán (một miền nào đó đã trở nên rỗng).\n", "error_tag")
        ac3_log_text_widget.tag_config("error_tag", foreground="red")
        ac3_log_text_widget.config(state="disabled")
        
        if not execution_log: 
            update_ac3_board_display(initial_domains_for_ac3)
        else:
            temp_domains_at_failure = copy.deepcopy(initial_domains_for_ac3)
            for entry_item in execution_log: 
                arc_xi_name_fail, _ = entry_item['arc_processed']
                xi_idx_fail = int(arc_xi_name_fail[1:])
                temp_domains_at_failure[xi_idx_fail] = set(entry_item['xi_domain_after_revise'])
                if not temp_domains_at_failure[xi_idx_fail] and entry_item['was_revised']:
                    break 
            update_ac3_board_display(temp_domains_at_failure)
        messagebox.showerror("AC-3", "Không tìm thấy lời giải nhất quán!")
    else:
        if hasattr(solver, 'current_ac3_domains_for_display'):
            solver.current_ac3_domains_for_display = copy.deepcopy(initial_domains_for_ac3) 
        else: 
            solver.current_ac3_domains_for_display = copy.deepcopy(initial_domains_for_ac3)
        log_iterator = iter(execution_log)
        animate_ac3_steps(log_iterator, ac3_window, initial_domains_for_ac3, speed_up_button) 

    ac3_window.transient(root)
    ac3_window.grab_set()



# --- HÀM MỚI CHO CỬA SỔ HIỆU SUẤT ---
performance_tree = None
performance_test_button = None

ALGO_FUNCTION_MAP = {
    "BFS": solver.bfs_solve, "DFS": solver.dfs_solve, "UCS": solver.ucs_solve, "IDS": solver.ids_solve,
    "Greedy": solver.greedy_solve, "A Star": solver.a_star_solve, "IDA Star": solver.ida_star_solve,
    "Simple Hill Climbing": solver.simple_hill_climbing_solve,
    "Hill Climbing": solver.hill_climbing_solve, 
    "Stochastic Hill Climbing": solver.Stochastic_hill_climbing_solve, 
    "Simulated Annealing": solver.Simulated_Annealing_solve,
    "Beam Search": solver.beam_search_solve,
}

PERFORMANCE_ALGO_GROUPS = {
    "Nhóm 1: Tìm kiếm không thông tin": ["BFS", "DFS", "UCS", "IDS"],
    "Nhóm 2: Tìm kiếm có thông tin (Heuristic)": ["Greedy", "A Star", "IDA Star"],
    "Nhóm 3: Tìm kiếm cục bộ & Metaheuristics": [
        "Simple Hill Climbing", "Hill Climbing", "Stochastic Hill Climbing",
        "Simulated Annealing", "Beam Search"
    ]
}

def run_all_performance_tests(current_start_state, current_goal_state, selected_group):
    """
    Chạy kiểm tra hiệu suất cho một nhóm các thuật toán đã chọn với
    trạng thái đầu và đích hiện tại, sau đó hiển thị kết quả (thời gian,
    số bước, số nút đã duyệt) trong một bảng (Treeview).
    """
    global performance_tree, performance_test_button
    if not performance_tree: 
        return

    performance_test_button.config(state=tk.DISABLED, text="Đang chạy kiểm tra...")
    root.update_idletasks()

    for item in performance_tree.get_children():
        performance_tree.delete(item)

    if selected_group not in PERFORMANCE_ALGO_GROUPS:
        messagebox.showerror("Lỗi", "Nhóm thuật toán không hợp lệ!")
        performance_test_button.config(state=tk.NORMAL, text="Chạy Kiểm tra")
        return

    algo_list = PERFORMANCE_ALGO_GROUPS[selected_group]
    group_id = performance_tree.insert("", tk.END, text=selected_group, open=True, tags=('group_header',))
    performance_tree.tag_configure('group_header', font=('Arial', 10, 'bold'))

    for algo_name in algo_list:
        if algo_name in ALGO_FUNCTION_MAP:
            solver_func = ALGO_FUNCTION_MAP[algo_name]
            try:
                start_run_time = time.time()
                path_result, nodes_val = solver_func(current_start_state, current_goal_state)
                time_val_num = time.time() - start_run_time
                time_val_str = f"{time_val_num:.4f}"
                
                steps_val = len(path_result) - 1 if path_result else "N/A"
                found_val = "Có" if path_result else "Không"

                performance_tree.insert(group_id, tk.END, values=(algo_name, time_val_str, steps_val, nodes_val if nodes_val is not None else "N/A", found_val))
            except Exception as e:
                performance_tree.insert(group_id, tk.END, values=(algo_name, "Lỗi", str(e), "N/A", "Không"))
            root.update_idletasks() 
        else:
            performance_tree.insert(group_id, tk.END, values=(algo_name, "Chưa cài đặt", "N/A", "N/A", "N/A"))

    performance_test_button.config(state=tk.NORMAL, text="Chạy Kiểm tra")
    messagebox.showinfo("Hoàn tất", f"Đã chạy xong các kiểm tra cho {selected_group}!")

def show_performance_window():
    """
    Tạo và hiển thị cửa sổ để đánh giá hiệu suất của các thuật toán
    giải đố 8-puzzle khác nhau.
    """
    global root, performance_tree, performance_test_button, start_entries, goal_entries
    
    perf_window = tk.Toplevel(root)
    perf_window.title("Đánh giá Hiệu suất Thuật toán")
    win_width, win_height = 900, 600
    perf_window.geometry(f"{win_width}x{win_height}")
    screen_width = perf_window.winfo_screenwidth()
    screen_height = perf_window.winfo_screenheight()
    x_pos = (screen_width // 2) - (win_width // 2)
    y_pos = (screen_height // 2) - (win_height // 2)
    perf_window.geometry(f"+{x_pos}+{y_pos}")

    try:
        current_start_for_test = get_state_from_entries(start_entries)
        current_goal_for_test = get_state_from_entries(goal_entries)
        if not is_valid_state(current_start_for_test) or not is_valid_state(current_goal_for_test):
            messagebox.showerror("Lỗi Trạng Thái", "Start State hoặc Goal State trên giao diện chính không hợp lệ.", parent=perf_window)
            perf_window.destroy()
            return
    except Exception as e:
        messagebox.showerror("Lỗi Đọc Trạng Thái", f"Không thể đọc Start/Goal State: {e}", parent=perf_window)
        perf_window.destroy()
        return

    top_controls_frame = tk.Frame(perf_window, pady=10)
    top_controls_frame.pack(fill=tk.X)

    # Thêm Combobox chọn nhóm thuật toán
    combo_label = tk.Label(top_controls_frame, text="Chọn Nhóm Thuật Toán:", font=("Arial", 11))
    combo_label.pack(side=tk.LEFT, padx=(0, 5))

    group_names = list(PERFORMANCE_ALGO_GROUPS.keys())
    selected_group_var = tk.StringVar(value=group_names[0])  # mặc định chọn nhóm đầu tiên

    group_combo = ttk.Combobox(top_controls_frame, values=group_names, textvariable=selected_group_var, state="readonly", width=20)
    group_combo.pack(side=tk.LEFT)

    performance_test_button = tk.Button(
        top_controls_frame, text="Chạy Kiểm tra", 
        command=lambda: run_all_performance_tests(current_start_for_test, current_goal_for_test, selected_group_var.get()),
        font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", width=20
    )
    performance_test_button.pack(side=tk.LEFT, padx=10)

    tree_frame = tk.Frame(perf_window)
    tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    columns = ("algo", "time", "steps", "nodes", "found")
    performance_tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
    performance_tree.heading("algo", text="Thuật toán")
    performance_tree.heading("time", text="Thời gian (s)")
    performance_tree.heading("steps", text="Số bước")
    performance_tree.heading("nodes", text="Số nút duyệt")
    performance_tree.heading("found", text="Tìm thấy?")
    performance_tree.column("algo", width=250, anchor="w")
    performance_tree.column("time", width=100, anchor="center")
    performance_tree.column("steps", width=100, anchor="center")
    performance_tree.column("nodes", width=120, anchor="center")
    performance_tree.column("found", width=100, anchor="center")
    vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=performance_tree.yview)
    performance_tree.configure(yscrollcommand=vsb.set)
    vsb.pack(side="right", fill="y")
    performance_tree.pack(side="left", fill="both", expand=True)

    initial_info_label = tk.Label(perf_window, text="Nhấn nút ở trên để chạy kiểm tra. Quá trình này có thể mất thời gian.", font=("Arial", 10, "italic"), fg="grey")
    initial_info_label.pack(pady=5)

    perf_window.transient(root)
    perf_window.grab_set()

def draw_board_labels(parent_frame, state_or_domain_list, is_domain_list=False):
    """
    Vẽ một bảng 8-puzzle nhỏ (sử dụng các nhãn - Label) để hiển thị
    một trạng thái ô chữ hoặc miền giá trị của các ô, thường dùng
    trong cửa sổ hiển thị kết quả chi tiết.
    """
    board_frame = tk.Frame(parent_frame, bd=2, relief=tk.SOLID, bg="#AAAAAA")
    for i in range(3):
        for j in range(3):
            cell_idx = i * 3 + j
            text_to_display = ""
            bg_color = "white"

            if is_domain_list: 
                domain = state_or_domain_list[cell_idx]
                max_display = 3
                display_values = sorted(list(domain))
                if len(display_values) > max_display:
                    text_to_display = ", ".join(map(str, display_values[:max_display])) + "..."
                else:
                    text_to_display = ", ".join(map(str, display_values))
                if not domain:
                    text_to_display = "Ø"
                    bg_color = "#FFCCCC"
                elif len(domain) == 1:
                     text_to_display = str(list(domain)[0])
                     bg_color = "#CCFFCC"

            else: 
                value = state_or_domain_list[i][j]
                text_to_display = str(value) if value != 0 else ""
                bg_color = "#CCFFFF" if value != 0 else "white"

            font_size = 10 if is_domain_list and len(text_to_display) > 5 else 14
            lbl = tk.Label(board_frame, text=text_to_display,
                           font=("Arial", font_size, "bold"), width=6 if is_domain_list else 4, height=2,
                           borderwidth=1, relief="ridge",
                           bg=bg_color)
            lbl.grid(row=i, column=j, padx=1, pady=1)
    return board_frame

def display_belief_search_results(results, algo_name, generated_starts, generated_goals): 
    """
    Hiển thị kết quả chi tiết của các thuật toán tìm kiếm trong không gian niềm tin
    (như No Observation Search, Partial Observation Search, Generate and Test)
    trong một cửa sổ mới. Cửa sổ này sẽ hiển thị các trạng thái đầu,
    trạng thái đích đã tạo và đường đi (nếu có) cho từng trường hợp.
    """
    global root
    result_window = tk.Toplevel(root)
    result_window.title(f"Kết quả chi tiết - {algo_name}")
    win_width, win_height = 750, 700
    result_window.geometry(f"{win_width}x{win_height}")
    screen_width = result_window.winfo_screenwidth()
    screen_height = result_window.winfo_screenheight()
    x_pos = (screen_width // 2) - (win_width // 2)
    y_pos = (screen_height // 2) - (win_height // 2)
    result_window.geometry(f"+{x_pos}+{y_pos}")

    main_scroll_frame = tk.Frame(result_window)
    main_scroll_frame.pack(fill=tk.BOTH, expand=True)
    canvas = tk.Canvas(main_scroll_frame)
    scrollbar_y = tk.Scrollbar(main_scroll_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar_y.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar_y.pack(side="right", fill="y")

    if algo_name != "Generate and Test":
        start_header_frame = tk.Frame(scrollable_frame, bg="#e6f7ff", bd=1, relief="raised", padx=5, pady=5)
        start_header_frame.pack(fill="x", pady=(5, 10), padx=5)
        tk.Label(start_header_frame, text="Các Trạng Thái Đầu Đã Tạo:", bg="#e6f7ff", font=("Arial", 13, "bold")).pack(anchor="w", pady=(0,5))
        starts_inner_frame = tk.Frame(start_header_frame, bg="#e6f7ff") 
        starts_inner_frame.pack(fill="x")

        for idx, start_state_item in enumerate(generated_starts):
            start_item_frame = tk.Frame(starts_inner_frame, bg="#e6f7ff")
            start_item_frame.pack(side=tk.LEFT, padx=30, anchor="n")
            tk.Label(start_item_frame, text=f"Trạng thái {idx+1}:", bg="#e6f7ff", font=("Arial", 11, "italic")).pack(anchor="w")
            start_board = draw_board_labels(start_item_frame, start_state_item)
            start_board.pack()

    goal_header_frame = tk.Frame(scrollable_frame, bg="#e6f7ff", bd=1, relief="raised", padx=5, pady=5)
    goal_header_frame.pack(fill="x", pady=(5, 10), padx=5)
    tk.Label(goal_header_frame, text="Các Trạng Thái Đích Đã Tạo:", bg="#e6f7ff", font=("Arial", 13, "bold")).pack(anchor="w", pady=(0,5))
    goals_inner_frame = tk.Frame(goal_header_frame, bg="#e6f7ff") 
    goals_inner_frame.pack(fill="x")

    for idx, goal_state_item in enumerate(generated_goals):
        goal_item_frame = tk.Frame(goals_inner_frame, bg="#e6f7ff")
        goal_item_frame.pack(side=tk.LEFT, padx=30, anchor="n")
        tk.Label(goal_item_frame, text=f"Mục tiêu {idx+1}:", bg="#e6f7ff", font=("Arial", 11, "italic")).pack(anchor="w")
        goal_board = draw_board_labels(goal_item_frame, goal_state_item)
        goal_board.pack()

    if not results:
        no_results_frame = tk.Frame(scrollable_frame, pady=20)
        no_results_frame.pack(fill="x", expand=True)
        tk.Label(no_results_frame, text="Không tìm thấy lời giải.",
                    font=("Arial", 14, "bold"), fg="red").pack(pady=10)
        tk.Label(no_results_frame, text="(Không có đích chung nào được tìm thấy cho tất cả các trạng thái bắt đầu)",
                    font=("Arial", 11, "italic"), fg="grey").pack()

    else:
        tk.Label(scrollable_frame, text="Kết Quả Từ Các Trạng Thái Bắt Đầu:", font=("Arial", 13, "bold")).pack(anchor="w", pady=(10,5), padx=5)

        for i, res in enumerate(results):
            start_s = res['start']
            goal_s = res['goal']
            path = res['path']

            row_frame = tk.Frame(scrollable_frame, bg="#e6f7ff", bd=1, relief="sunken", padx=5, pady=5)
            row_frame.pack(fill="x", pady=20, padx=5)

            start_frame_outer = tk.Frame(row_frame, bg="#e6f7ff")
            start_frame_outer.grid(row=0, column=0, padx=(0, 10), sticky="nw")
            tk.Label(start_frame_outer, text=f"Start {i+1}:", bg="#e6f7ff", font=("Arial", 12, "bold")).pack(anchor="w")
            start_board = draw_board_labels(start_frame_outer, start_s)
            start_board.pack(anchor="w")

            step_display_frame = tk.Frame(row_frame, bg="#e6f7ff")
            step_display_frame.grid(row=0, column=1, padx=5, sticky="nsew")
            tk.Label(step_display_frame, text="Detail Steps:", bg="#e6f7ff", font=("Arial", 12, "bold")).pack(anchor="nw")
            steps_text_widget = scrolledtext.ScrolledText(step_display_frame, height=10, width=25,
                                                        font=("Arial", 18), wrap=tk.NONE)
            steps_text_widget.pack(fill=tk.BOTH, expand=True)
            steps_text_widget.tag_configure("center", justify='center')
            steps_text_widget.tag_configure("bold_red", foreground="red", font=("Arial", 18, "bold"))

            goal_frame_outer = tk.Frame(row_frame, bg="#e6f7ff")
            if goal_s: # Chỉ tạo và grid nếu có goal đạt được
                goal_frame_outer.grid(row=0, column=2, padx=(10, 0), sticky="ne")
                tk.Label(goal_frame_outer, text="Reached Goal:", bg="#e6f7ff", font=("Arial", 12, "bold")).pack(anchor="w")
                goal_board = draw_board_labels(goal_frame_outer, goal_s)
                goal_board.pack(anchor="w")

            row_frame.grid_columnconfigure(1, weight=1)

            if path:
                step_count = len(path) - 1
                steps_text_widget.insert(tk.END, f"Số step: {step_count}\n", "bold_red")
                steps_text_widget.insert(tk.END, "----------\n", "center")
                for step_index, step in enumerate(path):
                    steps_text_widget.insert(tk.END, f"Bước {step_index}:\n", "center")
                    for row in step:
                        steps_text_widget.insert(tk.END, f"{row}\n", "center")
                    steps_text_widget.insert(tk.END, "----------\n", "center")
            else:
                steps_text_widget.insert(tk.END, "Không tìm thấy lời giải", "center")

            steps_text_widget.config(state="disabled")

    result_window.transient(root)
    result_window.grab_set()
    root.wait_window(result_window)

def display_solution():
    """
    Hiển thị từng bước của lời giải tìm được cho bài toán 8-puzzle
    trên giao diện chính, cập nhật lưới ô chữ và thông tin các bước.
    """
    global skip_requested
    skip_requested = False
    reset_app()

    step_text.config(state="normal")
    step_text.delete(1.0, tk.END)
    step_text.tag_configure("center", justify='center')

    if not solution:
        step_text.insert(tk.END, f"Không tìm thấy lời giải")
        step_text.config(state="disabled")
        return

    step_label.config(text=f"Step: {len(solution)}")

    start_time = time.time()

    for step_index, step in enumerate(solution):
        step_text.config(state="normal")
        step_text.insert(tk.END, f"Bước {step_index + 1}:\n", "center")
        for row in step:
            step_text.insert(tk.END, f"{row}\n", "center")
        step_text.insert(tk.END, "----------\n", "center")
        step_text.config(state="disabled")

        update_solution_grid(step)
        root.update()

        time_label.config(text=f"Time: {round(time.time() - start_time, 4)}")

        if skip_requested:
            continue
        time.sleep(0.2)

def reset_app():
    """
    Đặt lại các thành phần giao diện người dùng liên quan đến việc hiển thị
    lời giải (như ô văn bản các bước, lưới ô chữ lời giải, nhãn thời gian
    và số bước) về trạng thái ban đầu.
    """
    step_text.config(state="normal")
    step_text.delete(1.0, tk.END)
    step_text.config(state="disabled")
    for i in range(3):
        for j in range(3):
            solution_grid[i][j].config(text="", bg = "#CCFFFF")
    time_label.config(text="Time: 0.0000 s")
    step_label.config(text="Step: 0")

def skip_solution():
    """
    Đặt một cờ để bỏ qua hiệu ứng động khi hiển thị các bước giải,
    cho phép hiển thị ngay trạng thái cuối cùng của lời giải.
    """
    global skip_requested
    skip_requested = True

def update_solution_grid(state):
    """
    Cập nhật lưới ô chữ hiển thị lời giải trên giao diện chính
    với một trạng thái (state) cụ thể của ô chữ.
    """
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            solution_grid[i][j].config(text=str(value) if value != 0 else "", bg = "#CCFFFF" if value != 0 else "white")

def disable_buttons():
    """
    Vô hiệu hóa tất cả các nút chọn thuật toán và nút điều khiển
    (reset, speed up, performance), thường được gọi khi một thuật toán đang chạy.
    """

    reset_btn.config(state=tk.DISABLED)
    bfs_btn.config(state=tk.DISABLED)
    dfs_btn.config(state=tk.DISABLED)
    ucs_btn.config(state=tk.DISABLED)
    ids_btn.config(state=tk.DISABLED)
    greedy_btn.config(state=tk.DISABLED)
    a_star_btn.config(state=tk.DISABLED)
    ida_star_btn.config(state=tk.DISABLED)
    simple_hill_climbing_btn.config(state=tk.DISABLED)
    hill_climbing_btn.config(state=tk.DISABLED)
    stochastic_hill_climbing_btn.config(state=tk.DISABLED)
    simulated_annealing_btn.config(state=tk.DISABLED)
    beam_search_btn.config(state=tk.DISABLED)
    and_or_graph_search_btn.config(state=tk.DISABLED)
    genetic_algorithm_btn.config(state=tk.DISABLED)
    no_observation_btn.config(state=tk.DISABLED)
    partial_observation_btn.config(state=tk.DISABLED)
    generate_and_test_btn.config(state=tk.DISABLED)
    backtracking_search_btn.config(state=tk.DISABLED)
    ac3_btn.config(state=tk.DISABLED)
    q_learning_btn.config(state=tk.DISABLED)
    performance_btn.config(state=tk.DISABLED)

def enable_buttons():
    """
    Kích hoạt lại tất cả các nút chọn thuật toán và nút điều khiển,
    thường được gọi sau khi một thuật toán đã hoàn thành.
    """

    reset_btn.config(state=tk.NORMAL)
    bfs_btn.config(state=tk.NORMAL)
    dfs_btn.config(state=tk.NORMAL)
    ucs_btn.config(state=tk.NORMAL)
    ids_btn.config(state=tk.NORMAL)
    greedy_btn.config(state=tk.NORMAL)
    a_star_btn.config(state=tk.NORMAL)
    ida_star_btn.config(state=tk.NORMAL)
    simple_hill_climbing_btn.config(state=tk.NORMAL)
    hill_climbing_btn.config(state=tk.NORMAL)
    stochastic_hill_climbing_btn.config(state=tk.NORMAL)
    simulated_annealing_btn.config(state=tk.NORMAL)
    beam_search_btn.config(state=tk.NORMAL)
    and_or_graph_search_btn.config(state=tk.NORMAL)
    genetic_algorithm_btn.config(state=tk.NORMAL)
    no_observation_btn.config(state=tk.NORMAL)
    partial_observation_btn.config(state=tk.NORMAL)
    generate_and_test_btn.config(state=tk.NORMAL)
    backtracking_search_btn.config(state=tk.NORMAL)
    ac3_btn.config(state=tk.NORMAL)
    q_learning_btn.config(state=tk.NORMAL)
    performance_btn.config(state=tk.NORMAL)

root = tk.Tk()
root.title("Tran An Thien - 23110333")
root.geometry(f"{WIDTH}x{HEIGHT}")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_pos = (screen_width // 2) - (WIDTH // 2)
y_pos = (screen_height // 2) - (HEIGHT // 2)
root.geometry(f"+{x_pos}+{y_pos}")
root.resizable(False, False)

main_frame = tk.Frame(root, bg="#e6f7ff")
main_frame.pack(fill=tk.BOTH, expand=True)

state_frame = tk.Frame(main_frame, bg="#99CCFF", bd=2, relief="solid")
state_frame.grid(row=0, column=0, rowspan=4, padx=20, pady=10, sticky="w")

start_label = tk.Label(state_frame, bg="#99CCFF", text="Start State", font=("Arial", 14, "bold"))
start_label.grid(row=0, column=0, padx=20, pady=5)
start_frame = tk.Frame(state_frame, bd=2, relief=tk.SUNKEN)
start_frame.grid(row=1, column=0, padx=20, pady=5)

arrow_label = tk.Label(state_frame, bg="#99CCFF", text="⇓", font=("Arial", 50, "bold"))
arrow_label.grid(row=2, column=0, pady=5)

goal_label = tk.Label(state_frame, bg="#99CCFF", text="Goal State", font=("Arial", 14, "bold"))
goal_label.grid(row=3, column=0, padx=20, pady=5)
goal_frame = tk.Frame(state_frame, bd=2, relief=tk.SUNKEN)
goal_frame.grid(row=4, column=0, padx=20, pady=(5, 20))

draw_board(start_frame, start_state, start_entries)
draw_board(goal_frame, goal_state, goal_entries)


button_frame = tk.Frame(main_frame, bg="#F0FFF0", bd=2, relief="solid")
button_frame.grid(row=3, column=1, columnspan=3, pady=5, sticky="wn")
btn_width = 20

bfs_btn = tk.Button(button_frame, text="BFS", width=btn_width, command=lambda: run_algorithm("BFS"), bg="#7fbfff", fg="white", font=("Arial", 12, "bold"))
dfs_btn = tk.Button(button_frame, text="DFS", width=btn_width, command=lambda: run_algorithm("DFS"), bg="#ff9999", fg="white", font=("Arial", 12, "bold"))
ucs_btn = tk.Button(button_frame, text="UCS", width=btn_width, command=lambda: run_algorithm("UCS"), bg="#7ED957", fg="white", font=("Arial", 12, "bold"))
ids_btn = tk.Button(button_frame, text="IDS", width=btn_width, command=lambda: run_algorithm("IDS"), bg="#FFA500", fg="white", font=("Arial", 12, "bold"))
greedy_btn = tk.Button(button_frame, text="Greedy", width=btn_width, command=lambda: run_algorithm("Greedy"), bg="#7fbfff", fg="white", font=("Arial", 12, "bold"))
a_star_btn = tk.Button(button_frame, text="A*", width=btn_width, command=lambda: run_algorithm("A Star"), bg="#ff9999", fg="white", font=("Arial", 12, "bold"))
ida_star_btn = tk.Button(button_frame, text="IDA*", width=btn_width, command=lambda: run_algorithm("IDA Star"), bg="#7ED957", fg="white", font=("Arial", 12, "bold"))
simple_hill_climbing_btn = tk.Button(button_frame, text="Simple Hill Climbing", width=btn_width, command=lambda: run_algorithm("Simple Hill Climbing"), bg="#7fbfff", fg="white", font=("Arial", 12, "bold"))
hill_climbing_btn = tk.Button(button_frame, text="Hill Climbing", width=btn_width, command=lambda: run_algorithm("Hill Climbing"), bg="#ff9999", fg="white", font=("Arial", 12, "bold"))
stochastic_hill_climbing_btn = tk.Button(button_frame, text="Stochastic Hill Climbing", width=btn_width, command=lambda: run_algorithm("Stochastic Hill Climbing"), bg="#7ED957", fg="white", font=("Arial", 12, "bold"))
simulated_annealing_btn = tk.Button(button_frame, text="Simulated Annealing", width=btn_width, command=lambda: run_algorithm("Simulated Annealing"), bg="#FFA500", fg="white", font=("Arial", 12, "bold"))
beam_search_btn = tk.Button(button_frame, text="Beam Search", width=btn_width, command=lambda: run_algorithm("Beam Search"), bg="#FFA500", fg="white", font=("Arial", 12, "bold"))
and_or_graph_search_btn = tk.Button(button_frame, text="And-Or Graph Search", width=btn_width, command=lambda: run_algorithm("And-Or Graph Search"), bg="#ff9999", fg="white", font=("Arial", 12, "bold"))
genetic_algorithm_btn = tk.Button(button_frame, text="Genetic Algorithm", width=btn_width, command=lambda: run_algorithm("Genetic Algorithm"), bg="#7fbfff", fg="white", font=("Arial", 12, "bold"))
no_observation_btn = tk.Button(button_frame, text="No Observation Search", width=btn_width, command=lambda: run_algorithm("No Observation Search"), bg="#7ED957", fg="white", font=("Arial", 12, "bold"))
partial_observation_btn = tk.Button(button_frame, text="Partial Observation", width=btn_width, command=lambda: run_algorithm("Partial Observation Search"), bg="#FFA500", fg="white", font=("Arial", 12, "bold"))
backtracking_search_btn = tk.Button(button_frame, text="Backtracking search", width=btn_width, command = show_backtracking, bg="#ff9999", fg="white", font=("Arial", 12, "bold"))
generate_and_test_btn = tk.Button(button_frame, text="Generate and Test", width=btn_width, command=lambda: run_algorithm("Generate and Test"), bg="#7fbfff", fg="white", font=("Arial", 12, "bold"))
ac3_btn = tk.Button(button_frame, text="AC-3", width=btn_width, command=open_ac3_visualization_setup_form, bg="#7ED957", fg="white", font=("Arial", 12, "bold"))
q_learning_btn = tk.Button(button_frame, text="Q-Learning", width=btn_width, command=lambda: run_algorithm("Q-Learning"), bg="#FFA500", fg="white", font=("Arial", 12, "bold"))

reset_btn = tk.Button(button_frame, text="Reset", width=btn_width, command=reset_app, bg="#7f8c8d", fg="white", font=("Arial", 12, "bold"))
skip_btn = tk.Button(button_frame, text="Speed up", width=btn_width, command=skip_solution, bg="#34495e", fg="white", font=("Arial", 12, "bold"))
performance_btn = tk.Button(button_frame, text="Performance", width=btn_width, command=show_performance_window, bg="#34495e", fg="white", font=("Arial", 12, "bold"))

performance_btn.grid(row=0, column=0, pady=10)
reset_btn.grid(row=0, column=1, pady=10)
skip_btn.grid(row=0, column=2, pady=10)

bfs_btn.grid(row=1, column=0, padx=(15, 5), pady=10)
dfs_btn.grid(row=1, column=1, padx=5, pady=10)
ucs_btn.grid(row=1, column=2, padx=5, pady=10)
ids_btn.grid(row=1, column=3, padx=(5, 15), pady=10)

greedy_btn.grid(row=2, column=0, padx=(15, 5), pady=10)
a_star_btn.grid(row=2, column=1, padx=5, pady=10)
ida_star_btn.grid(row=2, column=2, padx=5, pady=10)

beam_search_btn.grid(row=2, column=3, padx=(5, 15), pady=10)
simple_hill_climbing_btn.grid(row=3, column=0, padx=(15, 5), pady=10)
hill_climbing_btn.grid(row=3, column=1, padx=5, pady=10)
stochastic_hill_climbing_btn.grid(row=3, column=2, padx=5, pady=10)
simulated_annealing_btn.grid(row=3, column=3, padx=(5, 15), pady=10)
genetic_algorithm_btn.grid(row=4, column=0, padx=(15, 5), pady=10)

and_or_graph_search_btn.grid(row=4, column=1, padx=5, pady=10)
no_observation_btn.grid(row=4, column=2, padx=5, pady=10)
partial_observation_btn.grid(row=4, column=3, padx=(5, 15), pady=10)

generate_and_test_btn.grid(row=5, column=0, padx=(15,5), pady=10)
backtracking_search_btn.grid(row=5, column=1, padx=5, pady=10)
ac3_btn.grid(row=5, column=2, padx=5, pady=10)

q_learning_btn.grid(row=5, column=3, padx=(5, 15), pady=10)

step_history_frame = tk.Frame(main_frame, bd=2, relief="solid")
step_history_frame.grid(row=1, column=3, padx=20, sticky="wn")

scrollbar = tk.Scrollbar(step_history_frame, width=20)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

step_text = tk.Text(step_history_frame, fg = "#33CC99", bg = "#EEE9E9", height=10, width=20, font=("Arial", 18), yscrollcommand=scrollbar.set)
step_text.pack(side=tk.TOP, fill=tk.BOTH, padx=10, pady=10)
step_text.config(state="disabled")

scrollbar.config(command=step_text.yview)

solution_frame = tk.Frame(main_frame, bd=2, relief="solid")
solution_frame.grid(row=1, column=1, columnspan = 2, sticky="n")

current_label = tk.Label(main_frame, bg = "#e6f7ff", text="Current State", font=("Arial", 14, "bold"))
current_label.grid(row=0, column=1, columnspan=2, padx=10)

detail_step_label = tk.Label(main_frame, bg = "#e6f7ff", text="Detail Steps", font=("Arial", 14, "bold"))
detail_step_label.grid(row=0, column=3, padx=125, sticky="w")

solution_grid = [[tk.Label(solution_frame, bg = "#CCFFFF", text="", font=("Arial", 16, "bold"),
                           width=8, height=4, borderwidth=1, relief="ridge")
                  for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        solution_grid[i][j].grid(row=i, column=j, padx=4, pady=4)

time_label = tk.Label(main_frame, text="Time: 0.0000 s", font=("Arial", 16, "bold"), fg="red", bg="#E0EEEE", width=15, relief="groove")
time_label.grid(row=2, column=3, padx=10, pady=5, sticky="w")

step_label = tk.Label(main_frame, text="Step: 0", font=("Arial", 16, "bold"), fg="red", bg="#E0EEEE", width=15, relief="groove")
step_label.grid(row=2, column=2, padx=10, pady=5, sticky="n")

root.mainloop()