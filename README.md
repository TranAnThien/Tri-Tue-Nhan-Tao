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

### 💡 2.2. Informed Search Algorithms (Tìm kiếm có thông tin)

> Các thành phần chính của bài toán
  * Trạng thái đầu: Trạng thái xuất phát của bài toán để tìm kiếm lời giải.
  * Trạng thái đích: Trạng thái mong muốn đạt được khi áp dụng thuật toán tìm kiếm vào trạng thái ban đầu.
  * Không gian trạng thái: Tập hợp tất cả các trạng thái có thể có của bài toán 8 puzzle.
  * Hành động: Mô tả các hành động để chuyển từ trạng thái này sang trạng thái khác (di chuyển ô trống lên, xuống, trái, phải
  * Chi phí đường đi: Mỗi hành động (di chuyển 1 ô) sẽ có chi phí là 1.
  * Giá trị manhattan: Ước lượng chi phí từ trạng thái hiện tại đến trạng thái đích.
> Giải pháp: Chuỗi các hành động dẫn từ trạng thái đầu đến trạng thái đích.

| Thuật toán | GIF minh họa |
|------------|--------------|
| 🔸 **Greedy Best-First Search**<br> - Sử dụng hàng đợi ưu tiên (Priority Queue).<br> - Chọn trạng thái có giá trị manhattan nhỏ nhất (được xem là trạng thái gần đích nhất). | ![Greedy](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/Greedy.gif) |
| 🔸 **A\*** (A-star)<br> - Sử dụng hàng đợi ưu tiên (Priority Queue) để lưu trữ các trạng thái.<br> - Chọn trạng trái có giá trị f(n) nhỏ nhất với công thức (`f(n) = g(n) + h(n)`), trong đó h(n) là giá trị manhattan và g(n) là chi phí đường đi.| ![A\*](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/A_Star.gif) |
| 🔸 **IDA\*** (Iterative Deepening A\*)<br> - Phiên bản tiết kiệm bộ nhớ của A\*.<br> - Hoạt động dựa trên một ngưỡng của giá trị f(n) cho mỗi lượt tìm kiếm theo chiều sâu, ngưỡng này tăng dần qua mỗi lần lặp. | ![IDA\*](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/IDA_Star.gif) |

---

### 🧬 3. Local Search (Tìm kiếm cục bộ)

> Các thành phần chính của bài toán
  * Trạng thái đầu: Trạng thái xuất phát của bài toán để tìm kiếm lời giải.
  * Trạng thái đích: Trạng thái mong muốn đạt được khi áp dụng thuật toán tìm kiếm vào trạng thái ban đầu.
  * Không gian trạng thái: Tập hợp tất cả các trạng thái có thể có của bài toán 8 puzzle.
  * Hành động: Mô tả các hành động để chuyển từ trạng thái này sang trạng thái khác (di chuyển ô trống lên, xuống, trái, phải
  * Chi phí đường đi: Mỗi hành động (di chuyển 1 ô) sẽ có chi phí là 1.
  * Giá trị manhattan: Ước lượng chi phí từ trạng thái hiện tại đến trạng thái đích.
> Giải pháp: Chuỗi các hành động dẫn từ trạng thái đầu đến trạng thái đích.

| Thuật toán | GIF minh họa |
|------------|--------------|
| 🔸 **Simple Hill Climbing**<br> - Dùng giá trị manhattan để kiểm tra xem trạng thái lân cận có tốt hơn trạng thái hiện tại hay không.<br> - Duyệt qua các trạng thái lân cận và chọn trạng thái đầu tiên tốt hơn trạng thái hiện tại để di chuyển. | ![Simple Hill Climbing](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/SimpleHillClimbing.gif) |
| 🔸 **Hill Climbing**<br> - Dùng giá trị manhattan để kiểm tra xem trạng thái lân cận có tốt hơn trạng thái hiện tại hay không.<br> - Duyệt qua các trạng thái lân cận và chọn trạng thái lân cận tốt nhất để di chuyển. | ![Hill Climbing](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/HillClimbing.gif) |
| 🔸 **Stochastic Hill Climbing**<br> - Dùng giá trị manhattan để kiểm tra xem trạng thái lân cận có tốt hơn trạng thái hiện tại hay không.<br> - Duyệt qua các trạng thái lân cận để tìm các trạng thái tốt hơn trạng thái hiện tại, sau đó chọn ngẫu nhiên 1 trong các trạng thái đó để di chuyển. | ![Stochastic Hill Climbing](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/StochasticHillClimbing.gif) |
| 🔸 **Simulated Annealing**<br> - Dùng giá trị manhattan để kiểm tra xem trạng thái lân cận tốt hơn hay xấu hơn trạng thái hiện tại, có thêm 1 giá trị nhiệt độ giảm dần sau mỗi bước, 1 giá trị xác suất được tính khi trạng thái lân cận xấu hơn được xem xét.<br> - Duyệt qua các trạng thái lân cận, nếu trạng thái đó tốt hơn trạng thái hiện tại thì sẽ chọn trang thái đó để di chuyển, nếu trạng thái đó xấu hơn thì sẽ tính xác suất xem có dùng trạng thái đó để di chuyển hay không. | ![Simulated Annealing](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/SimulatedAnnealing.gif) |
| 🔸 **Beam Search**<br> - Dùng giá trị manhattan để kiểm tra xem trạng thái lân cận có tốt hơn trạng thái hiện tại hay không.<br> - Duy trì song song k trạng thái thay vì chỉ một trạng thái.<br> - Tại mỗi bước, nó sẽ tạo ra tất cả các trạng thái lân cận từ k trạng thái, sau đó chọn ra k trạng thái tốt nhất để thực hiện cho bước tiếp theo. | ![Beam Search](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/BeamSearch.gif) |
| 🔸 **Genetic Algorithm**<br> - Dùng quần thể, chọn lọc cá thể tốt, sinh ra thế hệ mới.<br> - Cách chọn đường đi:<br>  + Khởi tạo quần thể.<br>  + Đánh giá độ thích nghi.<br>  + Lựa chọn cá thể.<br>  + Lai ghép.<br>  + Đột biến.<br>  + Sinh ra cá thể mới. | ![Genetic Algorithm](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/Genetic.gif) |

---
