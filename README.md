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

🔸 Breadth-First Search (BFS)<br>
     - BFS sử dụng cấu trúc hàng đợi (queue) để lưu các trạng thái đang chờ xét.<br>
     - Thuật toán bắt đầu từ trạng thái ban đầu, đẩy nó vào queue. Sau đó lặp lại các bước: lấy trạng thái đầu tiên trong queue ra, mở rộng ra tất cả các trạng thái kế tiếp hợp lệ (điều kiện: di chuyển một ô trống, không trùng trạng thái đã duyệt trước đó), rồi đưa các trạng thái mới này vào cuối queue.
> Ảnh gif minh họa thuật toán BFS


🔸 Depth-First Search (DFS)<br>
     - DFS sử dụng cấu trúc ngăn xếp (stack) để lưu các trạng thái.<br>
     - Di chuyển lần lượt từng bước đi hợp lệ và đi sâu vào một chuỗi di chuyển, đến khi không còn bước đi nào hợp lệ hoặc đạt trạng thái đích thì dừng hoặc quay lui. 
> Ảnh gif minh họa thuật toán DFS


🔸 Uniform Cost Search (UCS)<br>
     - UCS dùng hàng đợi ưu tiên (priority queue), ưu tiên chọn các trạng thái có tổng chi phí nhỏ nhất.<br>
     - Với mỗi bước di chuyển có chi phí bằng 1, UCS sẽ chọn trạng thái có tổng chi phí thấp nhất để mở rộng, từ đó tìm ra lời giải tối ưu.
> Ảnh gif minh họa thuật toán UCS


🔸 Iterative Deepening Search (IDS)<br>
     - IDS kết hợp DFS và BFS bằng cách thực hiện DFS nhiều lần với giới hạn độ sâu tăng dần.<br>
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

🔸 Greedy Best-First Search<br>
     - Greedy Best-First Search sử dụng hàng đợi ưu tiên (priority queue), mở rộng trạng thái dựa trên giá trị manhattan.<br>
     - Tại mỗi bước đi, thuật toán sẽ chọn trạng thái có giá trị manhattan (h(n) nhỏ nhất để mở rộng, không quan tâm đến số bước đi (g(n).
> Ảnh gif minh họa thuật toán Greedy Best-First Search


🔸  A* (A-Star Search)<br>
     - Mỗi trạng thái được đánh giá bởi hàm chi phí: f(n) = h(n) + g(n). Trong đó h(n) là giá trị manhattan và g(n) là tổng chi phí đường đi.<br>
     - Tại mỗi bước đi, thuật toán sẽ chọn trạng thái có giá trị f(n) nhỏ nhất.
> Ảnh gif minh họa thuật toán A*


🔸  IDA* (Iterative Deepening A-Star)<br>
     - Là sự kết hợp giữa A* và DFS lặp sâu (IDS). Thay vì sử dụng hàng đợi ưu tiên lớn, IDA* sử dụng một ngưỡng giới hạn f(n) (giống A*) trong mỗi lần tìm kiếm.<br>
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

🔸 Simple Hill Climbing<br>
     - Đây là phiên bản cơ bản nhất của thuật toán Hill Climbing.<br>
     - Tại mỗi trạng thái, duyệt qua các trạng thái lân cận và chọn trạng thái đầu tiên tốt hơn (giá trị h(n) nhỏ hơn) để di chuyển. Vì thế thuật toán dễ bị mắc kẹt.
> Ảnh gif minh họa thuật toán Simple Hill Climbing


🔸 Hill Climbing<br>
     - Giống như Simple Hill Climbing, nhưng thay vì chọn trạng thái đầu tiên tốt hơn để di chuyển thì thuật toán này sẽ chọn trạng thái tốt nhất trong các trạng thái lân cận để di chuyển. Thuật toán này tốt hơn phiên bản Simple Hill Climbing nhưng vẫn có khả năng bị mắc kẹt.
> Ảnh gif minh họa thuật toán Hill Climbing


🔸 Stochastic Hill Climbing<br>
     - Đây cũng là một biến thể của Hill Climbing, nhưng thay vì lựa chọn trạng thái tốt nhất hay là trạng thái tốt hơn đầu tiên thì thuật toán này sẽ chọn ngẫu nhiên. Thuật toán duyệt quá các trạng thái lân cận và chọn ngẫu nhiên một trạng thái tốt hơn để di chuyển. 
> Ảnh gif minh họa thuật toán Stochastic Hill Climbing


🔸 Simulated Annealing<br>
     - Thuật toán này cho phép di chuyển đến các trạng thái xấu hơn với xác suất phụ thuộc vào nhiệt độ.<br>
     - Từ trạng thái hiện tại, chọn ngẫu nhiên mộ trạng thái. Nếu trạng thái đó tốt hơn thì di chuyển, nếu không thì tính xác suất nhận nó bằng công thức: 'P = exp(-Δh / T)'. Trong đó Δh là độ chênh lệch giá trị manhattan, T là nhiệt độ hiện tại. Sau mỗi bước thì nhiệt độ sẽ giảm dần.
> Ảnh gif minh họa thuật toán Simulated Annealing


🔸 Beam Search<br>
     - Khởi đầu bằng một trạng thái ban đầu, sau đó xét qua các trạng thái lân cận và lấy ra 'k' trạng thái có giá trị h(n) nhỏ nhất.<br>
     - Tại mỗi vòng lặp, thuật toán tạo ra tất cả trạng thái lân cận từ 'k' trạng thái hiện tại. Sau đó chọn ra 'k' trạng thái có giá trị h(n) nhỏ nhất để thực hiện vòng lặp tiếp theo. Tiếp tục lặp lại cho đến khi tìm đến đích.
> Ảnh gif minh họa thuật toán Beam Search


🔸 Genetic Algorithm<br>
     - Khởi tạo quần thể gồm nhiều chuỗi hành động ngẫu nhiên.<br>
     - Đánh giá độ thích nghi (fitness) bằng cách áp dụng chuỗi hành động vào trạng thái ban đầu và tính h(n) của kết quả.<br>
     - Chọn lọc các cá thể tốt để sinh sản.<br>
     - Lai ghép (crossover) các cặp cá thể để tạo ra cá thể con.<br>
     - Đột biến (mutation) một số điểm trong chuỗi hành động để đa dạng hóa quần thể.<br>
     - Lặp lại các bước trên qua nhiều thế hệ cho đến khi tìm được lời giải (h(n) = 0).
> Ảnh gif minh họa thuật toán Genetic Algorithm


> Hình ảnh so sánh hiệu suất các thuật toán
![Screenshot 2025-05-12 170410](https://github.com/user-attachments/assets/80c6bcee-ec50-4ca5-aebd-4cb5dcc94a5e)

> Một số nhận xét khi áp dụng vào bài toán 8 puzzle
  * Simple Hill Climbing: Nhanh nhưng dễ bị kẹt vì không xét hết tất cả các trạng thái tốt hơn.
  * Hill Climbing: Tốt hơn Simple Hill climbing nhưng vẫn có khả năng bị mắc kẹt.
  * tochastic Hill Climbing: Có thể thoát khỏi mắc kẹt nhwof sự lựa chọn ngẫu nhiên.
  * Simulated Anealing: Có khả năng thoát khỏi mắc kẹt và tìm thấy lời giải vì nó có xác suất nhận các trường hợp xấu hơn.
  * Beam Search: Hoạt động tương tự như BFS nhưng chỉ giữ lại 'k' trạng thái thay vì mở rộng toàn bộ.
  * Genetic Algorithm: Có khả năng tìm thấy lời giải mà không cần duyệt toàn bộ không gian.

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

🔸 AND-OR Search<br>
     - Phân rã bài toàn thành nhiều vấn đề con nhỏ hơn.<br>
     - Nút AND: Đại diện cho một vấn đề mà tất cả các vấn đề con của nó phải được giải quyết.<br>
     - Nút OR: Đại diện cho một vấn đề mà chỉ cần chọn một trong những vấn đề con của nó để giải quyết.<br>
     - Trong bài toán 8-Puzzle, với mỗi nút OR (1 trạng thái) thì ta có thể lựa chọn 1 trong 4 hành động để di chuyển (lên, xuống, trái, phải). Sau khi lựa chọn hành động sẽ có 2 trường hợ xảy ra:<br>     
       + Trường hợp thứ nhất: Tỉ lệ xảy ra là 70%, sau khi thực hiện hành động chỉ di chuyển 1 ô và sinh ra một trạng thái duy nhất.<br>
       + Trường hợp thứ hai: Thỉ lệ xảy ra là 30%, sau khi thực hiện hành động thì sẽ di chuyển xa hơn bình thường, sau khi di chuyển 1 ô thì lại tiếp tục di chuyển sang 1 ô khác.<br>
     - Và để giải quyết được nút AND (nút điều kiện) thì các trạng thái sinh ra sau khi nút OR lựa chọn hành động đều phải có đường đi đến đích. Nếu 1 trong các trạng thái không thỏa mã thì nút AND sẽ không được giải quyết và nút OR phải lựa chọn hành động khác để tiếp tục.
> Ảnh gif minh họa thuật toán AND-OR Search


🔸 No Observation<br>
     - Ban đầu sẽ khỏi tọa một tập các trạng đầu và một tập các trạng thái đích một cách ngẫu nhiên.<br>
     - Kiểm tra tất cả các trạng thái đầu xem có đường đi để đến được đích hay không bằng các thuật toán tìm kiếm ở nhóm trước (BFS, DFS, A*, ...)<br>
     - Nếu có một trạng thái đích chung mà tất cả các trạng thái đầu đều có đường đi đến nó thì kết quả trả về sẽ là tập tất cả đường đi đó.
> Ảnh gif minh họa thuật toán No Observation


🔸 Partial Observation<br>
     - Tập hợp các trạng thái ban đầu vẫn tạo một cách ngẫu nhiên giống No Observation, nhưng tập các trạng thái đích được tạo ngẫu nhiên dựa trên một phần nhìn thấy được của trạng thái đích thực sự.<br>
     - Sau đó thực hiện tương tự No Observation, kiểm tra các trạng thái đầu và tìm ra trạng thái đích chung.
> Ảnh gif minh họa thuật toán Partial Observation


---

### 🧩 2.5. Constraint Satisfaction Problems (CSPs) (Tìm kiếm trong môi trường có ràng buộc)

> Các thành phần chính của bài toán
  * Đối với thuật toán Generate and Test
     * Trạng thái đầu: Trạng thái xuất phát của bài toán để tìm kiếm lời giải.
     * Trạng thái đích: Trạng thái mong muốn đạt được khi áp dụng thuật toán tìm kiếm vào trạng thái ban đầu.
     * Không gian trạng thái: Tập hợp tất cả các trạng thái có thể có của bài toán 8 puzzle.
     * Hành động: Mô tả các hành động để chuyển từ trạng thái này sang trạng thái khác (di chuyển ô trống lên, xuống, trái, phải
     * Chi phí đường đi: Mỗi hành động (di chuyển 1 ô) sẽ có chi phí là 1.
     * Giá trị manhattan: Ước lượng chi phí từ trạng thái hiện tại đến trạng thái đích.
  * Đối với thuật toán Backtracking và AC-3
     * Biến đại diện cho các thành phần của bài toán (vị trí của ô).
     * Miền giá trị: Tập giá trị mà biến có thể nhận được, miền giá trị có từng ô là {0, 1, 2, ..., 8}.
     * Ràng buộc: Những quy tắc áp dụng vào bài toán để thu hẹp miền giá trị của các biến.
> Giải pháp:
  * Chuỗi các hành động từ trạng thái đầu đến trạng thái đích.
  * Thu hẹp miền giá trị của các biến để tạo ra trạng thái cuối cùng thỏa mãn các ràng buộc.

🔸 Generate and Test<br>
     - Tạo ra một trạng thái mới ngẫu nhiên và kiêm tra xem trạng thái đó có đường đi đến trạng thái đích hay không.<br>  
        + Nếu đi được đến đích thì sẽ trả về tập các đường đi.<br>  
        + Nếu không thì sẽ tạo lại một trạng thái mới khác và tiếp tục kiểm tra cho đến khi có trạng thái có đường đi đến trạng thái đích.
> Ảnh gif minh họa thuật toán Generate and Test


🔸 Backtracking<br>
     - Ràng buộc được sử dụng trong bài toán:<br>
        + Giá trị của từng ô phải khác nhau.<br>
        + Giá trị của ô phía trước sẽ lớn hơn giá trị của ô phía sau.<br>
     - Miền giá trị ban đầu của 9 ô là {0, 1, ..., 8}.<br>
     - Ban đầu sẽ xét ô 0, với mỗi giá trị trong miền, kiểm tra tính hợp lệ:<br>
        + Nếu chưa tồn tại trong dãy đã gán → không trùng lặp.<br>
        + Nếu nhỏ hơn giá trị ô trước đó (nếu có) → thỏa ràng buộc thứ hai.<br>
     - Nếu hợp lệ, gán giá trị đó cho ô hiện tại và đệ quy tiếp sang ô tiếp theo.<br>
     - Nếu không còn giá trị nào hợp lệ cho một ô, thực hiện quay lui (backtrack) về ô trước để thử giá trị khác.<br>
     - Kết thúc khi gán đủ 9 ô và thỏa mãn các ràng buộc.
> Ảnh gif minh họa thuật toán Backtracking


🔸 AC-3<br>
     - Ràng buộc được sử dụng trong bài toán:<br>
        + Giá trị của từng ô phải khác nhau.<br>
        + Giá trị của ô phía trước sẽ nhỏ hơn giá trị của ô phía sau.<br>
     - Miền giá trị ban đầu của 9 ô là {0, 1, ..., 8}.<br>
     - Duyệt qua từng cung, xét từng giá trị nằm trong miền giá trị của biến thứ nhất trong cung:<br>   
        + Nếu trong miền giá trị của biến thứ hai có ít nhất một giá trị thỏa mãn các ràng buộc thì miền giá trị của biến thứ nhất sẽ không đổi.<br> 
        + Nếu không có giá trị nào trong miền giá trị của biến thứ hai thỏa mãn các ràng buộc thì miền giá trị của biến thứ nhất sẽ xóa giá trị đang xét.<br> 
        + Nếu có sự thu hẹp miền giá trị xảy ra thì các cung liền kề với biến thứ nhất sẽ được thêm lại vào hàng đợi các cung.
> Ảnh gif minh họa thuật toán AC-3


---

### 🧠 2.6. Reinforcement Learning (Học tăng cường)

> Các thành phần chính của bài toán:
  * Trạng thái đầu: Trạng thái xuất phát của bài toán để tìm kiếm lời giải (gồm 9 ô, trong đó có 8 ô chứa các giá trị khác nhau từ 1->8 và 1 ô trống).
  * Trạng thái đích: Trạng thái mong muốn đạt được khi áp dụng thuật toán tìm kiếm vào trạng thái ban đầu (gồm 9 ô, trong đó có 8 ô chứa các giá trị khác nhau từ 1->8 và 1 ô trống).
  * Phần thưởng (Reward):
     * Thường nhận giá trị -1 cho mỗi bước di chuyển để tối ưu đường đi ngắn nhất.
     * Nhận giá trị +100 khi đạt trạng thái đích.
  * Chính sách (Policy): Chiến lược chọn hành động dựa trên trạng thái hiện tại, thường sử dụng chính sách ε-greedy.
  * Hàm giá trị Q(s, a): Ước lượng giá trị kỳ vọng khi thực hiện hành động a tại trạng thái s.
> Giải pháp:
  * Một dãy các trạng thái từ đầu đến đích đại diện cho đường đi tối ưu theo chính sách đã học từ Q-table.

🔸 Q-Learning<br>
  * Chiến lược huấn luyện:<br>
     - Với mỗi episode:<br>
       + Chạy tối đa max_steps bước hoặc đến khi đạt trạng thái đích.<br>
       + Tại mỗi bước:<br>
          Chọn hành động theo epsilon-greedy.  
          Cập nhật Q-value cho trạng thái hiện tại. 
          Di chuyển đến trạng thái tiếp theo.
     - Sau mỗi episode, epsilon được giảm dần (epsilon_decay) để tăng khả năng khai thác tri thức đã học.
  * Trích xuất đường đi:<br>
     - Sau khi huấn luyện, sử dụng Q-table để tái tạo đường đi từ trạng thái đầu đến trạng thái đích:<br>
       + Ở mỗi bước, chọn hành động có Q-value cao nhất.<br>
       + Tránh lặp lại trạng thái để không rơi vào vòng lặp vô tận.<br>
 > Ảnh gif minh họa thuật toán Q-Learning
