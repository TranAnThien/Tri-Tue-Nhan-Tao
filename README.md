## 📁 Danh sách thuật toán tìm kiếm

### 🧠 1. Uninformed Search Algorithms (Tìm kiếm không có thông tin)

> Các thuật toán này **không sử dụng bất kỳ kiến thức nào về đích**, chỉ dựa trên cấu trúc không gian trạng thái.

| Thuật toán | GIF minh họa |
|------------|--------------|
| 🔸 **Breadth-First Search (BFS)**  <br> - Tìm kiếm theo từng lớp.<br> - Đảm bảo tìm được đường đi ngắn nhất (nếu chi phí các bước bằng nhau). | ![BFS GIF](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/BFS.gif) |
| 🔸 **Depth-First Search (DFS)**<br> - Tìm theo chiều sâu đến khi đạt đích hoặc không còn gì để duyệt.<br> - Có thể bị kẹt trong vòng lặp nếu không kiểm soát tốt. | ![DFS GIF](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/DFS.gif) |
| 🔸 **Uniform Cost Search (UCS)**<br> - Mở rộng nút có chi phí thấp nhất trước.<br> - Đảm bảo tìm ra đường đi ngắn nhất (nếu có chi phí từng bước khác nhau). | ![UCS GIF](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/UCS.gif) |
| 🔸 **Iterative Deepening Search (IDS)**<br> - Kết hợp ưu điểm của DFS và BFS.<br> - Tìm theo chiều sâu tăng dần. | ![IDS GIF](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/IDS.gif) |

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
