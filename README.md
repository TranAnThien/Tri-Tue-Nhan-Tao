## 📁 Danh sách thuật toán tìm kiếm

| **Nhóm Thuật Toán** | **Thuật Toán & Mô Tả** |
|---------------------|------------------------|
| 🧠 **1. Uninformed Search Algorithms** | 
🔸 **Breadth-First Search (BFS)**  
- Tìm kiếm theo từng lớp.  
- Đảm bảo tìm được đường đi ngắn nhất (nếu chi phí các bước bằng nhau).  
![BFS GIF](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/BFS.gif)

🔸 **Depth-First Search (DFS)**  
- Tìm theo chiều sâu đến khi đạt đích hoặc không còn gì để duyệt.  
- Có thể bị kẹt trong vòng lặp nếu không kiểm soát tốt.  
![DFS GIF](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/DFS.gif)

🔸 **Uniform Cost Search (UCS)**  
- Mở rộng nút có chi phí thấp nhất trước.  
- Đảm bảo tìm ra đường đi ngắn nhất (nếu có chi phí từng bước khác nhau).  
![UCS GIF](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/UCS.gif)

🔸 **Iterative Deepening Search (IDS)**  
- Kết hợp ưu điểm của DFS và BFS.  
- Tìm theo chiều sâu tăng dần.  
![IDS GIF](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/IDS.gif)
|
| 💡 **2. Informed Search Algorithms** |
🔸 **Greedy Best-First Search**  
- Luôn mở rộng nút gần đích nhất theo heuristic.  
- Không đảm bảo tối ưu.  
![Greedy GIF](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/Greedy.gif)

🔸 **A\* (A-star)**  
- Dựa trên tổng chi phí đã đi + ước lượng chi phí còn lại (`f(n) = g(n) + h(n)`).  
- Tối ưu và hoàn chỉnh nếu heuristic hợp lý.  
![A* GIF](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/A_Star.gif)

🔸 **IDA\* (Iterative Deepening A\*)**  
- Phiên bản tiết kiệm bộ nhớ của A\*.  
- Lặp lại A\* theo ngưỡng `f`.  
![IDA* GIF](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/IDA_Star.gif)

🔸 **Simple Hill Climbing**  
- Duyệt các trạng thái kề cận, chọn cái đầu tiên tốt hơn.  
- Dễ kẹt cực trị địa phương.  
![Simple Hill Climbing](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/SimpleHillClimbing.gif)

🔸 **Hill Climbing**  
- Luôn chọn trạng thái tốt hơn hiện tại.  
- Dễ kẹt cực trị địa phương.  
![Hill Climbing](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/HillClimbing.gif)

🔸 **Stochastic Hill Climbing**  
- Chọn ngẫu nhiên trong các nước đi tốt hơn.  
- Hạn chế kẹt cực trị địa phương.  
![Stochastic Hill Climbing](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/StochasticHillClimbing.gif)

🔸 **Simulated Annealing**  
- Giống Hill Climbing nhưng có thể "nhảy xuống" để thoát cực trị.  
- Dựa trên nhiệt độ giảm dần.  
![Simulated Annealing](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/SimulatedAnnealing.gif)

🔸 **Beam Search**  
- Giữ `k` trạng thái tốt nhất mỗi bước.  
- Không đảm bảo tối ưu.  
![Beam Search](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/BeamSearch.gif)
|
| 🧬 **3. Genetic Algorithm** |
🔸 **Genetic Algorithm**  
- Mô phỏng quá trình tiến hóa tự nhiên với chọn lọc, lai ghép, đột biến.  
- Phù hợp khi không gian tìm kiếm rộng, khó định hướng.  
![Genetic Algorithm](https://github.com/TranAnThien/Tri-Tue-Nhan-Tao/blob/main/Search%20Algorithm%20Gif/Genetic.gif)
|
