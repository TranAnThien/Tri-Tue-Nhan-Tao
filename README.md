## 📁 Bài tập cá nhân: Giải Bài Toán 8-Puzzle với Các Nhóm Thuật Toán Tìm Kiếm

## 1. Mục tiêu
  * Nghiên cứu và cài đặt thuật toán tìm kiếm trong 6 nhóm thuật toán được học trên lớp vào bài toán 8 puzzle: Tiến hành nghiên cứu về lý thuyết và cơ chế hoạt động của 6 nhóm thuật toán, áp dụng các thuật toán này vào bài toán 8 puzzle nhằm kiểm tra tính đúng đắn và khả năng ứng dụng vào thực tế của các thuật toán.
  * Phân tích và so sánh hiệu quả (thời gian thực thi, số bước) của các thuật toán: Thực hiện chạy thử một số trường hợp trên bài toán 8 puzzle, thu thập dữ liệu hiệu suất để đánh giá từng thuật toán dựa trên thời gian tìm thấy đường đi, số bước di chuyển, chi phí đường đi, thời gian thực thi.
  * Trực quan hóa quá trình tìm kiếm của thuật toán: Xây dựng giao diện hiển thị trực quan các bước duyệt trạng thái và đường đi được tạo ra bởi từng thuật toán, giúp quan sát và so sánh các thuật toán. Giao diện này cho phép người dùng có thể dễ dàng nhập trạng thái bắt đầu, trạng thái kết thúc và dễ dang chọn thuật toán để áp dụng vào bài toán.
  * Hiểu rõ được bản chất, ưu điểm và nhược điểm của từng thuật toán.
## 2. Nội dung
> Trình bày về khái niệm, các thành phần chính và giải pháp của từng nhóm thuật toán và việc áp dụng, đánh giá 6 nhóm thuật toán đã học vào bài toán 8 puzzle.
### 🧠 2.1. Uninformed Search Algorithms (Tìm kiếm không có thông tin)

> Các thành phần chính của bài toán
  * Trạng thái đầu: Trạng thái xuất phát của bài toán để tìm kiếm lời giải (gồm 9 ô, trong đó có 8 ô chứa các giá trị khác nhau từ 1->8 và 1 ô trống).
  * Trạng thái đích: Trạng thái mong muốn đạt được khi áp dụng thuật toán tìm kiếm vào trạng thái ban đầu (gồm 9 ô, trong đó có 8 ô chứa các giá trị khác nhau từ 1->8 và 1 ô trống).
  * Không gian trạng thái: Tập hợp tất cả các trạng thái có thể có của bài toán 8 puzzle.
  * Hành động: Mô tả các hành động để chuyển từ trạng thái này sang trạng thái khác (di chuyển ô trống lên, xuống, trái, phải)
  * Chi phí đường đi: Mỗi hành động (di chuyển 1 ô) sẽ có chi phí là 1.
> Giải pháp: Chuỗi các hành động dẫn từ trạng thái đầu đến trạng thái đích.

🔸 Breadth-First Search (BFS)
     - BFS sử dụng cấu trúc hàng đợi (queue) để lưu các trạng thái đang chờ xét.
     - Thuật toán bắt đầu từ trạng thái ban đầu, đẩy nó vào queue. Sau đó lặp lại các bước: lấy trạng thái đầu tiên trong queue ra, mở rộng ra tất cả các trạng thái kế tiếp hợp lệ (điều kiện: di chuyển một ô trống, không trùng trạng thái đã duyệt trước đó), rồi đưa các trạng thái mới này vào cuối queue.
> Ảnh gif minh họa thuật toán BFS


🔸 Depth-First Search (DFS)
     - DFS sử dụng cấu trúc ngăn xếp (stack) để lưu các trạng thái.
     - Di chuyển lần lượt từng bước đi hợp lệ và đi sâu vào một chuỗi di chuyển, đến khi không còn bước đi nào hợp lệ hoặc đạt trạng thái đích thì dừng hoặc quay lui. 
> Ảnh gif minh họa thuật toán DFS


🔸 Uniform Cost Search (UCS)
     - UCS dùng hàng đợi ưu tiên (priority queue), ưu tiên chọn các trạng thái có tổng chi phí nhỏ nhất.
     - Với mỗi bước di chuyển có chi phí bằng 1, UCS sẽ chọn trạng thái có tổng chi phí thấp nhất để mở rộng, từ đó tìm ra lời giải tối ưu.
> Ảnh gif minh họa thuật toán UCS


🔸 Iterative Deepening Search (IDS)
     - IDS kết hợp DFS và BFS bằng cách thực hiện DFS nhiều lần với giới hạn độ sâu tăng dần.
     - IDS bắt đầu duyệt giống như DFS nhưng chỉ đến độ sâu nhất định. Nếu chưa tìm thấy trạng thái đích, tăng giới hạn lên và duyệt lại từ đầu. 
> Ảnh gif minh họa thuật toán IDS


> Hình ảnh so sánh hiệu suất các thuật toán
![Screenshot 2025-05-12 170153](https://github.com/user-attachments/assets/a0991968-e8c0-4ee6-a344-2fdbf146070b)

> Một số nhận xét khi áp dụng vào bài toán 8 puzzle
  * BFS: Tìm thấy được đường đi ngắn nhất, nhưng khá chậm, rất tốn bộ nhớ.
  * DFS: Đường đi tì thấy được có thể không phải là đường đi ngắn nhất. Khi chạy thuật toán, số nút được xét rất lớn và kết quả trả về thường là một đường đi dài, tốn ít bộ nhớ.
  * UCS: Tối ưu về chi phí đường đi, nếu tất cả đường đi có chi phí là 1 (đang áp dụng vào bài toán) thì nó cũng sẽ trả về đường đi ngắn nhất giống thuật toán BFS.
  * IDS: Kết hợp ưu điểm của BFS và DFS, tốn thời gian vì lặp lại nhiều lần.

---

### 💡 2.2. Informed Search Algorithms (Tìm kiếm có thông tin)

> Các thành phần chính của bài toán
  * Trạng thái đầu: Trạng thái xuất phát của bài toán để tìm kiếm lời giải (gồm 9 ô, trong đó có 8 ô chứa các giá trị khác nhau từ 1->8 và 1 ô trống).
  * Trạng thái đích: Trạng thái mong muốn đạt được khi áp dụng thuật toán tìm kiếm vào trạng thái ban đầu (gồm 9 ô, trong đó có 8 ô chứa các giá trị khác nhau từ 1->8 và 1 ô trống).
  * Không gian trạng thái: Tập hợp tất cả các trạng thái có thể có của bài toán 8 puzzle.
  * Hành động: Mô tả các hành động để chuyển từ trạng thái này sang trạng thái khác (di chuyển ô trống lên, xuống, trái, phải
  * Chi phí đường đi: Mỗi hành động (di chuyển 1 ô) sẽ có chi phí là 1.
  * Giá trị manhattan: Ước lượng chi phí từ trạng thái hiện tại đến trạng thái đích (tổng số sai lệch của các ô giữa trạng thái đầu và trạng thái đích).
> Giải pháp: Chuỗi các hành động dẫn từ trạng thái đầu đến trạng thái đích.

🔸 Greedy Best-First Search
     - Greedy Best-First Search sử dụng hàng đợi ưu tiên (priority queue), mở rộng trạng thái dựa trên giá trị manhattan.
     - Tại mỗi bước đi, thuật toán sẽ chọn trạng thái có giá trị manhattan (h(n) nhỏ nhất để mở rộng, không quan tâm đến số bước đi (g(n).
> Ảnh gif minh họa thuật toán Greedy Best-First Search


🔸  A* (A-Star Search)
     - Mỗi trạng thái được đánh giá bởi hàm chi phí: f(n) = h(n) + g(n). Trong đó h(n) là giá trị manhattan và g(n) là tổng chi phí đường đi.
     - Tại mỗi bước đi, thuật toán sẽ chọn trạng thái có giá trị f(n) nhỏ nhất.
> Ảnh gif minh họa thuật toán A*


🔸  IDA* (Iterative Deepening A-Star)
     - Là sự kết hợp giữa A* và DFS lặp sâu (IDS). Thay vì sử dụng hàng đợi ưu tiên lớn, IDA* sử dụng một ngưỡng giới hạn f(n) (giống A*) trong mỗi lần tìm kiếm. 
     - Chỉ mở rộng các trạng thái có f(n) nhỏ hơn ngưỡng giới hạn. Nếu không thấy lời giải thì sẽ tăng ngưỡng giới hạn lên và tiếp tục lặp lại.
> Ảnh gif minh họa thuật toán IDA*


> Hình ảnh so sánh hiệu suất các thuật toán
![Screenshot 2025-05-12 170153](https://github.com/user-attachments/assets/c56d606a-8dd3-4e09-a26f-b426d3e4e4c1)

> Một số nhận xét khi áp dụng vào bài toán 8 puzzle
  * Greedy: Nhanh chóng tìm ra đường đi nếu có giá trị manhattan tốt nhưng đường đi thường không phải ngắn nhất.
  * A*: Hiệu quả cao khi áp dụng vào bài toán 8 puzzle, thời gian tìm thấy lời giải nhanh.
  * IDA*: Kết hợp tính tối ưu của A* và hiệu quả bộ nhớ của IDS, tốn thời gian do lặp lại nhiều lần. 
    
---

### 🧬 2.3. Local Search (Tìm kiếm cục bộ)

> Các thành phần chính của bài toán
  * Trạng thái đầu: Trạng thái xuất phát của bài toán để tìm kiếm lời giải (gồm 9 ô, trong đó có 8 ô chứa các giá trị khác nhau từ 1->8 và 1 ô trống).
  * Trạng thái đích: Trạng thái mong muốn đạt được khi áp dụng thuật toán tìm kiếm vào trạng thái ban đầu (gồm 9 ô, trong đó có 8 ô chứa các giá trị khác nhau từ 1->8 và 1 ô trống).
  * Không gian trạng thái: Tập hợp tất cả các trạng thái có thể có của bài toán 8 puzzle.
  * Hành động: Mô tả các hành động để chuyển từ trạng thái này sang trạng thái khác (di chuyển ô trống lên, xuống, trái, phải
  * Chi phí đường đi: Mỗi hành động (di chuyển 1 ô) sẽ có chi phí là 1.
  * Giá trị manhattan: Ước lượng chi phí từ trạng thái hiện tại đến trạng thái đích.
> Giải pháp: Chuỗi các hành động dẫn từ trạng thái đầu đến trạng thái đích.

🔸 Simple Hill Climbing
     - Đây là phiên bản cơ bản nhất của thuật toán Hill Climbing.
     - Tại mỗi trạng thái, duyệt qua các trạng thái lân cận và chọn trạng thái đầu tiên tốt hơn (giá trị h(n) nhỏ hơn) để di chuyển. Vì thế thuật toán dễ bị mắc kẹt.
> Ảnh gif minh họa thuật toán Simple Hill Climbing


🔸 Hill Climbing
     - Giống như Simple Hill Climbing, nhưng thay vì chọn trạng thái đầu tiên tốt hơn để di chuyển thì thuật toán này sẽ chọn trạng thái tốt nhất trong các trạng thái lân cận để di chuyển. Thuật toán này tốt hơn phiên bản Simple Hill Climbing nhưng vẫn có khả năng bị mắc kẹt.
> Ảnh gif minh họa thuật toán Hill Climbing


🔸 Stochastic Hill Climbing
     - Đây cũng là một biến thể của Hill Climbing, nhưng thay vì lựa chọn trạng thái tốt nhất hay là trạng thái tốt hơn đầu tiên thì thuật toán này sẽ chọn ngẫu nhiên. Thuật toán duyệt quá các trạng thái lân cận và chọn ngẫu nhiên một trạng thái tốt hơn để di chuyển. 
> Ảnh gif minh họa thuật toán Stochastic Hill Climbing


🔸 Simulated Annealing
     - IDS kết hợp DFS và BFS bằng cách thực hiện DFS nhiều lần với giới hạn độ sâu tăng dần.
     - IDS bắt đầu duyệt giống như DFS nhưng chỉ đến độ sâu nhất định. Nếu chưa tìm thấy trạng thái đích, tăng giới hạn lên và duyệt lại từ đầu. 
> Ảnh gif minh họa thuật toán Simulated Annealing


🔸 Iterative Deepening Search (IDS)
     - IDS kết hợp DFS và BFS bằng cách thực hiện DFS nhiều lần với giới hạn độ sâu tăng dần.
     - IDS bắt đầu duyệt giống như DFS nhưng chỉ đến độ sâu nhất định. Nếu chưa tìm thấy trạng thái đích, tăng giới hạn lên và duyệt lại từ đầu. 
> Ảnh gif minh họa thuật toán DFS


🔸 Iterative Deepening Search (IDS)
     - IDS kết hợp DFS và BFS bằng cách thực hiện DFS nhiều lần với giới hạn độ sâu tăng dần.
     - IDS bắt đầu duyệt giống như DFS nhưng chỉ đến độ sâu nhất định. Nếu chưa tìm thấy trạng thái đích, tăng giới hạn lên và duyệt lại từ đầu. 
> Ảnh gif minh họa thuật toán DFS


> Hình ảnh so sánh hiệu suất các thuật toán
![Screenshot 2025-05-12 170410](https://github.com/user-attachments/assets/80c6bcee-ec50-4ca5-aebd-4cb5dcc94a5e)

> Một số nhận xét khi áp dụng vào bài toán 8 puzzle
  * Hill Climbing và các biến thể (Simple Hill Climbing, Stochastic): Ít tốn bộ nhớ vì chỉ xét trạng thái hiện tại nhưng dễ bị mắc kẹt trước khi đến được trạng thái đích.
  * Simulated Anealing: Có khả năng không bị mắc kẹt vì nó cho phép đi đến các trạng thái xấu hơn.

---

### 🌌 2.4. Online Search Algorithms (Tìm kiếm trong môi trường phức tạp)

> Các thành phần chính của bài toán
  * Trạng thái đầu: Trạng thái xuất phát của bài toán để tìm kiếm lời giải.
      - Đối với thuật toán AND-OR: Trạng thái xuất phát đã có sẵn dữ liệu.
      - Đối với thuật toán No Observation và Partial Observation: Trạng thái đầu sẽ là tập hợp một hoặc nhiều trạng thái ngẫu nhiên.
  * Trạng thái đích: Trạng thái mong muốn đạt được khi áp dụng thuật toán tìm kiếm vào trạng thái ban đầu.
      - Đối với thuật toán AND-OR: Trạng thái đích đã có sẵn dữ liệu.
      - Đối với thuật toán No Observation: Trạng thái đích sẽ là tập hợp một hoặc nhiều trạng thái ngẫu nhiên.
      - Đối với thuật toán Partial Observation: Trạng thái đích sẽ là tập hợp một hoặc nhiều trạng thái được tạo ngẫu nhiên dựa trên một phần nhìn thấy được của trạng thái đích.
  * Không gian trạng thái: Tập hợp tất cả các trạng thái có thể có của bài toán 8 puzzle.
  * Hành động: Mô tả các hành động để chuyển từ trạng thái này sang trạng thái khác (di chuyển ô trống lên, xuống, trái, phải
  * Chi phí đường đi: Mỗi hành động (di chuyển 1 ô) sẽ có chi phí là 1.
  * Giá trị manhattan: Ước lượng chi phí từ trạng thái hiện tại đến trạng thái đích.
> Giải pháp: Chuỗi các hành động có điều kiện dẫn từ trạng thái đầu đến trạng thái đích (AND-OR) hoặc là đường đi trong không gian trạng thái niềm tin.

| Thuật toán |   GIF minh họa   |
|------------|------------------|
| 🔸 **AND-OR**<br> - Phân rã bài toán thành những vấn đề con.<br> - Nút AND: Đại diện cho một vấn đề mà tất cả các vấn đề con của nó phải được giải quyết.<br> - Đại diện cho một vấn đề mà chỉ cần chọn một trong những vấn đề con của nó để giải quyết. | ![Simple Hill Climbing](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/And-Or.gif) |
| 🔸 **No Observation**<br> - Tìm kiếm trạng thái đích chung từ những trạng thái đầu ngẫu nhiên.<br> - Giải thử tất cả các trạng thái đầu bằng một thuật toán tìm kiếm (BFS, DFS, A*, ...).<br> - Nếu tìm thấy đích chung mà tất cả trạng thái đầu đều đi tới thì kết quả là tập hợp tất cả đường đi đó. | ![Hill Climbing](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/No_Observation.gif) |
| 🔸 **Partial Observation**<br> - Tương tự như thuật toasnNo Observation.<br> - Vì nhìn thấy một phần nên những trạng thái đích được tạo sẽ giống với trạng thái đích mong muốn hơn. | ![Stochastic Hill Climbing](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/Partial_Observation.gif) |

---

### 🧩 2.5. Constraint Satisfaction Problems (CSPs) (Tìm kiếm trong môi trường có ràng buộc)

> Các thành phần chính của bài toán
  * Trạng thái đầu: Trạng thái xuất phát của bài toán để tìm kiếm lời giải.
  * Trạng thái đích: Trạng thái mong muốn đạt được khi áp dụng thuật toán tìm kiếm vào trạng thái ban đầu.
  * Không gian trạng thái: Tập hợp tất cả các trạng thái có thể có của bài toán 8 puzzle.
  * Hành động: Mô tả các hành động để chuyển từ trạng thái này sang trạng thái khác (di chuyển ô trống lên, xuống, trái, phải
  * Chi phí đường đi: Mỗi hành động (di chuyển 1 ô) sẽ có chi phí là 1.
  * Giá trị manhattan: Ước lượng chi phí từ trạng thái hiện tại đến trạng thái đích.
  * Biến đại diện cho các thành phần của bài toán (vị trí của ô).
  * Miền giá trị: Tập giá trị mà biến có thể nhận được.
  * Ràng buộc: Những quy tắc áp dụng vào bài toán để thu hẹp miền giá trị của các biến.
> Giải pháp:
  * Chuỗi các hành động từ trạng thái đầu đến trạng thái đích.
  * Thu hẹp miền giá trị của các biến để tạo ra trạng thái cuối cùng thỏa mãn các ràng buộc.

| Thuật toán |   GIF minh họa   |
|------------|------------------|
| 🔸 **Generate and Test**<br> - Tạo ra một trạng thái mới ngẫu nhiên và kiêm tra xem trạng thái đó có đường đi đến trạng thái đích hay không.<br>  + Nếu đi được đến đích thì sẽ trả về tập các đường đi.<br>  + Nếu không thì sẽ tạo lại một trạng thái mới khác và tiếp tục kiểm tra cho đến khi có trạng thái có đường đi đến trạng thái đích. | ![Simple Hill Climbing](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/Generate_And_Test.gif) |
| 🔸 **Backtracking**<br> - Tương tự như thuật toán DFS, thuật toán này sẽ đi sâu xuống hết mức có thể của một nhánh:<br>  + Nếu tìm thấy đường đi thì trả về tập các hành động.<br>  + Nếu không thì sẽ quay lui lại trạng thái trước đó, đồng thời hoàn tác việc đánh dấu đã thăm. | ![Hill Climbing](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/Backtracking.gif) |
---
  🔸 **AC-3**<br> - Tạo ra những ràng buộc áp đặt vào bài toắn hoặc sử dụng những ràng buộc có sẵn.<br> - Khởi tạo miền giá trị cho từng biến và một tập các cung dùng để kiểm tra các ràng buộc và thu hẹp miền giá trị của các biến.<br> - Duyệt qua từng cung, xét từng giá trị nằm trong miền giá trị của biến thứ nhất trong cung:<br>  + Nếu trong miền giá trị của biến thứ hai có ít nhất một giá trị thỏa mãn các ràng buộc thì miền giá trị của biến thứ nhất sẽ không đổi.<br>  + Nếu không có giá trị nào trong miền giá trị của biến thứ hai thỏa mãn các ràng buộc thì miền giá trị của biến thứ nhất sẽ xóa giá trị đang xét.<br>  + Nếu có sự thu hẹp miền giá trị xảy ra thì các cung liền kề với biến thứ nhất sẽ được thêm lại vào hàng đợi các cung.
  ![Stochastic Hill Climbing](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/AC_3.gif)

---
