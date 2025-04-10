import tkinter as tk
from tkinter import ttk, messagebox
import solver
import time
from collections import Counter

WIDTH, HEIGHT = 1300, 700

#Climbing: Start: ((2, 3, 6)
            #   ,(1, 5, 0)
            #   ,(4, 7, 8))
start_state = ((2, 3, 6)
              ,(1, 5, 0)
              ,(4, 7, 8))
goal_state = ((1, 2, 3)
             ,(4, 5, 6)
             ,(7, 8, 0))
start_entries = []
goal_entries = []


solution = []
running_algorithm = False
skip_requested = False

def is_valid_state(state):
    flat = [num for row in state for num in row]
    counter = Counter(flat)
    if set(flat) != set(range(9)):
        return False
    for val in range(9):
        if counter[val] != 1:
            return False
    return True
          
def draw_board(frame, state, entries_list):
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
    state = []
    for row in entries:
        current_row = []
        for entry in row:
            value = entry.get()
            current_row.append(int(value) if value.isdigit() else 0)
        state.append(tuple(current_row))
    return tuple(state)


def run_algorithm(algo):
    global solution, running_algorithm, start_state, goal_state
    if running_algorithm:
        return
    
    start_state = get_state_from_entries(start_entries)
    goal_state = get_state_from_entries(goal_entries)
    if not is_valid_state(start_state):
        messagebox.showerror("Lỗi", "START STATE không hợp lệ. Phải chứa đủ các số từ 1 đến 8, không lặp và có đúng 1 ô trống.")
        return
    if not is_valid_state(goal_state):
        messagebox.showerror("Lỗi", "GOAL STATE không hợp lệ. Phải chứa đủ các số từ 1 đến 8, không lặp và có đúng 1 ô trống.")
        return

    running_algorithm = True
    disable_buttons()
    
    start_time = time.time()
    
    if algo == "BFS":
        solution = solver.bfs_solve(start_state, goal_state)
    elif algo == "DFS":
        solution = solver.dfs_solve(start_state, goal_state)
    elif algo == "UCS":
        solution = solver.ucs_solve(start_state, goal_state)
    elif algo == "IDS":
        solution = solver.ids_solve(start_state, goal_state)
    elif algo == "Greedy":
        solution = solver.greedy_solve(start_state, goal_state)
    elif algo == "A Star":
        solution = solver.a_star_solve(start_state, goal_state)
    elif algo == "IDA Star":
        solution = solver.ida_star_solve(start_state, goal_state)
    elif algo == "Simple Hill Climbing":
        solution = solver.simple_hill_climbing_solve(start_state, goal_state)
    elif algo == "Hill Climbing":
        solution = solver.hill_climbing_solve(start_state, goal_state)
    elif algo == "Stochastic Hill Climbing":
        solution = solver.Stochastic_hill_climbing_solve(start_state, goal_state)
    elif algo == "Simulated Annealing":
        solution = solver.Simulated_Annealing_solve(start_state, goal_state)
    elif algo == "Beam Search":
        solution = solver.beam_search_solve(start_state, goal_state)
    elif algo == "And-Or Graph Search":
        solution = solver.and_or_graph_search(start_state, goal_state)
    elif algo == "Genetic Algorithm":
        solution = solver.genetic_algorithm_solve(start_state, goal_state)

    # elapsed_time = time.time() - start_time
    # time_label.config(text=f"Time: {elapsed_time:.4f} s")
    
    display_solution()
    
    enable_buttons()
    running_algorithm = False

def display_solution():
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
    step_text.config(state="normal")
    step_text.delete(1.0, tk.END)
    step_text.config(state="disabled")
    for i in range(3):
        for j in range(3):
            solution_grid[i][j].config(text="", bg = "#CCFFFF")
    time_label.config(text="Time: 0.0000 s")
    step_label.config(text="Step: 0")

def skip_solution():
    global skip_requested
    skip_requested = True

def update_solution_grid(state):
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            solution_grid[i][j].config(text=str(value) if value != 0 else "", bg = "#CCFFFF" if value != 0 else "white")

def disable_buttons():
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
    # and_or_graph_search_btn.config(state=tk.DISABLED)
    genetic_algorithm_btn.config(state=tk.DISABLED)

def enable_buttons():
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
    # and_or_graph_search_btn.config(state=tk.NORMAL)
    genetic_algorithm_btn.config(state=tk.NORMAL)

root = tk.Tk()
root.title("Tran An Thien - 23110333")
root.geometry(f"{WIDTH}x{HEIGHT}")
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
button_frame.grid(row=3, column=1, columnspan=3, pady=20, sticky="wn")
btn_width = 20

bfs_btn = tk.Button(button_frame, text="BFS", width=btn_width, command=lambda: run_algorithm("BFS"), bg="#7fbfff", fg="white", font=("Arial", 12, "bold"))
dfs_btn = tk.Button(button_frame, text="DFS", width=btn_width, command=lambda: run_algorithm("DFS"), bg="#ff9999", fg="white", font=("Arial", 12, "bold"))
ucs_btn = tk.Button(button_frame, text="UCS", width=btn_width, command=lambda: run_algorithm("UCS"), bg="#7ED957", fg="white", font=("Arial", 12, "bold"))
ids_btn = tk.Button(button_frame, text="IDS", width=btn_width, command=lambda: run_algorithm("IDS"), bg="#FFA500", fg="white", font=("Arial", 12, "bold"))
greedy_btn = tk.Button(button_frame, text="Greedy", width=btn_width, command=lambda: run_algorithm("Greedy"), bg="#B57EDC", fg="white", font=("Arial", 12, "bold"))
a_star_btn = tk.Button(button_frame, text="A*", width=btn_width, command=lambda: run_algorithm("A Star"), bg="#CCCC66", fg="white", font=("Arial", 12, "bold"))
ida_star_btn = tk.Button(button_frame, text="IDA*", width=btn_width, command=lambda: run_algorithm("IDA Star"), bg="#CCCCFF", fg="white", font=("Arial", 12, "bold"))
simple_hill_climbing_btn = tk.Button(button_frame, text="Simple Hill Climbing", width=btn_width, command=lambda: run_algorithm("Simple Hill Climbing"), bg="#FF33FF", fg="white", font=("Arial", 12, "bold"))
hill_climbing_btn = tk.Button(button_frame, text="Hill Climbing", width=btn_width, command=lambda: run_algorithm("Hill Climbing"), bg="#999999", fg="white", font=("Arial", 12, "bold"))
stochastic_hill_climbing_btn = tk.Button(button_frame, text="Stochastic Hill Climbing", width=btn_width, command=lambda: run_algorithm("Stochastic Hill Climbing"), bg="#6699FF", fg="white", font=("Arial", 12, "bold"))
simulated_annealing_btn = tk.Button(button_frame, text="Simulated Annealing", width=btn_width, command=lambda: run_algorithm("Simulated Annealing"), bg="#FF0066", fg="white", font=("Arial", 12, "bold"))
beam_search_btn = tk.Button(button_frame, text="Beam Search", width=btn_width, command=lambda: run_algorithm("Beam Search"), bg="#CC9999", fg="white", font=("Arial", 12, "bold"))
and_or_graph_search_btn = tk.Button(button_frame, text="And-Or Graph Search", width=btn_width, command=lambda: run_algorithm("And-Or Graph Search"), bg="#CC9999", fg="white", font=("Arial", 12, "bold"))
genetic_algorithm_btn = tk.Button(button_frame, text="Genetic Algorithm", width=btn_width, command=lambda: run_algorithm("Genetic Algorithm"), bg="#CC9999", fg="white", font=("Arial", 12, "bold"))

reset_btn = tk.Button(button_frame, text="Reset", width=btn_width, command=reset_app, bg="#7f8c8d", fg="white", font=("Arial", 12, "bold"))
skip_btn = tk.Button(button_frame, text="Speed up", width=btn_width, command=skip_solution, bg="#34495e", fg="white", font=("Arial", 12, "bold"))

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

# and_or_graph_search_btn.grid(row=4, column=0, padx=(15, 5), pady=10)
genetic_algorithm_btn.grid(row=4, column=0, padx=(15, 5), pady=10)

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
        solution_grid[i][j].grid(row=i, column=j)

time_label = tk.Label(main_frame, text="Time: 0.0000 s", font=("Arial", 16, "bold"), fg="red", bg="#E0EEEE", width=15, relief="groove")
time_label.grid(row=2, column=3, padx=10, pady=0, sticky="w")

step_label = tk.Label(main_frame, text="Step: 0", font=("Arial", 16, "bold"), fg="red", bg="#E0EEEE", width=15, relief="groove")
step_label.grid(row=2, column=2, padx=10, pady=0, sticky="e")

root.mainloop()