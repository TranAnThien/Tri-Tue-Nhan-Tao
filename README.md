## 📁 Bài tập cá nhân: Giải Bài Toán 8-Puzzle với Các Nhóm Thuật Toán Tìm Kiếm

## 1. Mục tiêu
  * Nghiên cứu và cài đặt thuật toán tìm kiếm trong 6 nhóm thuật toán được học trên lớp vào bài toán 8 puzzle: Tiến hành nghiên cứu về lý thuyết và cơ chế hoạt động của 6 nhóm thuật toán, áp dụng các thuật toán này vào bài toán 8 puzzle nhằm kiểm tra tính đúng đắn và khả năng ứng dụng vào thực tế của các thuật toán.
  * Phân tích và so sánh hiệu quả (thời gian thực thi, số bước) của các thuật toán: Thực hiện chạy thử một số trường hợp trên bài toán 8 puzzle, thu thập dữ liệu hiệu suất để đánh giá từng thuật toán dựa trên thời gian tìm thấy đường đi, số bước di chuyển, chi phí đường đi, thời gian thực thi.
  * Hiểu rõ được bản chất, ưu điểm và nhược điểm của từng thuật toán.
## 2. Nội dung
> Trình bày về khái niệm, các thành phần chính và giải pháp của từng nhóm thuật toán và việc áp dụng, đánh giá 6 nhóm thuật toán đã học vào bài toán 8 puzzle.
### 🧠 1. Uninformed Search Algorithms (Tìm kiếm không có thông tin)

> Các thành phần chính của bài toán
  * Trạng thái đầu: Trạng thái xuất phát của bài toán để tìm kiếm lời giải.
  * Trạng thái đích: Trạng thái mong muốn đạt được khi áp dụng thuật toán tìm kiếm vào trạng thái ban đầu.
  * Không gian trạng thái: Tập hợp tất cả các trạng thái có thể có của bài toán 8 puzzle.
  * Hành động: Mô tả các hành động để chuyển từ trạng thái này sang trạng thái khác (di chuyển ô trống lên, xuống, trái, phải
  * Chi phí đường đi: Mỗi hành động (di chuyển 1 ô) sẽ có chi phí là 1.
> Giải pháp: Chuỗi các hành động dẫn từ trạng thái đầu đến trạng thái đích.

| Thuật toán | GIF minh họa |
|------------|--------------|
| 🔸 **Breadth-First Search (BFS)**  <br> - Sử dụng cấu trúc hàng đợi (queue).<br> - Duyết tất cả các trạng thái ở cùng một độ sâu trước khi chuyển sang các trạng thái ở độ sâu tiếp theo. | ![BFS GIF](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/BFS.gif) |
| 🔸 **Depth-First Search (DFS)**<br> - Sử dụng cấu trúc ngăn xếp (Stack).<br> - Duyệt sâu xuống một nhánh hết sức có thể trước khi quay lui để thử các nhánh khác. | ![DFS GIF](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/DFS.gif) |
| 🔸 **Uniform Cost Search (UCS)**<br> - Sử dụng hàng đợi ưu tiên (Prority Queue).<br> - Mở rộng các trạng thái chưa đuyệt có chi phí đường đi nhỏ nhất. | ![UCS GIF](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/UCS.gif) |
| 🔸 **Iterative Deepening Search (IDS)**<br> - Là một biến thể của thuật toán DFS.<br> - Có thể một giới hạn về độ sâu tối đa mà thuật toán được phép duyệt. | ![IDS GIF](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/IDS.gif) |

---

### 💡 2. Informed Search Algorithms (Tìm kiếm có thông tin)

> Sử dụng **hàm heuristic** để ước lượng khoảng cách đến mục tiêu, giúp tìm kiếm nhanh hơn.

| Thuật toán | GIF minh họa |
|------------|--------------|
| 🔸 **Greedy Best-First Search**<br> - Luôn mở rộng nút gần đích nhất theo heuristic.<br> - Không đảm bảo tối ưu. | ![Greedy](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/Greedy.gif) |
| 🔸 **A\*** (A-star)<br> - Dựa trên tổng chi phí đã đi + ước lượng chi phí còn lại (`f(n) = g(n) + h(n)`).<br> - Tối ưu và hoàn chỉnh nếu heuristic hợp lý. | ![A\*](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/A_Star.gif) |
| 🔸 **IDA\*** (Iterative Deepening A\*)<br> - Phiên bản tiết kiệm bộ nhớ của A\*.<br> - Lặp lại A\* theo ngưỡng `f`. | ![IDA\*](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/IDA_Star.gif) |
| 🔸 **Simple Hill Climbing**<br> - Ở mỗi bước, duyệt các trạng thái kề cận và chọn trạng thái đầu tiên có heuristic tốt hơn hiện tại.<br> - Đơn giản, nhanh, nhưng dễ kẹt tại điểm cực trị địa phương vì không kiểm tra hết tất cả lựa chọn. | ![Simple Hill Climbing](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/SimpleHillClimbing.gif) |
| 🔸 **Hill Climbing**<br> - Luôn đi đến trạng thái có heuristic tốt hơn.<br> - Có thể bị kẹt tại điểm cực trị địa phương. | ![Hill Climbing](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/HillClimbing.gif) |
| 🔸 **Stochastic Hill Climbing**<br> - Biến thể của Hill Climbing, chọn ngẫu nhiên trong các nước đi tốt hơn.<br> - Hạn chế kẹt tại cực trị địa phương hiệu quả hơn. | ![Stochastic Hill Climbing](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/StochasticHillClimbing.gif) |
| 🔸 **Simulated Annealing**<br> - Giống hill climbing nhưng có khả năng "nhảy xuống" để thoát cực trị địa phương.<br> - Dựa trên nhiệt độ giảm dần. | ![Simulated Annealing](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/SimulatedAnnealing.gif) |
| 🔸 **Beam Search**<br> - Mỗi bước chỉ giữ `k` trạng thái tốt nhất.<br> - Giảm chi phí bộ nhớ nhưng không đảm bảo tối ưu. | ![Beam Search](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/BeamSearch.gif) |

---

### 🧬 3. Genetic Algorithm (Thuật toán di truyền)

> Mô phỏng quá trình tiến hóa tự nhiên với các thao tác lai ghép, đột biến, và chọn lọc.

| Thuật toán | GIF minh họa |
|------------|--------------|
| 🔸 **Genetic Algorithm**<br> - Dùng quần thể, chọn lọc cá thể tốt, sinh ra thế hệ mới.<br> - Phù hợp khi không gian tìm kiếm rộng, khó định hướng. | ![Genetic Algorithm](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/Genetic.gif) |
