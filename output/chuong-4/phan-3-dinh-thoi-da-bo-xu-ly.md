# Phần 3 — Định thời đa bộ xử lý

Nguồn chính: **W05 slide 19–28**, dừng đúng giới hạn đang dùng. Hình slide 28 đã được đối chiếu: cửa sổ Processor affinity chọn tập CPU được phép chạy một tiến trình. Không thêm thuật ngữ thời gian thực hay định thời OS ở slide 29 trở đi.

## Phần cứng và hai cách tiếp cận

| Khái niệm (English) | Định nghĩa/dấu hiệu | Nguồn |
|---|---|---|
| Định thời đa bộ xử lý (multiple-processor scheduling) | Phân việc thực thi khi có nhiều đơn vị xử lý khả dụng; phức tạp hơn mô hình một CPU. | W05 slide 19 |
| CPU đa lõi (multicore CPUs) | Có nhiều lõi vật lý. | W05 slide 19 |
| Lõi đa luồng (multithreaded cores) | Một lõi hỗ trợ nhiều luồng xử lý phần cứng; không đồng nhất với có nhiều lõi vật lý. | W05 slide 19 |
| Truy cập bộ nhớ không đồng nhất (non-uniform memory access / NUMA) | Thời gian truy cập bộ nhớ có thể khác nhau tùy bộ xử lý và vùng nhớ. | W05 slide 19; đối chiếu định nghĩa ở C01 trang 39 |
| Đa xử lý không đồng nhất (heterogeneous multiprocessing) | Hệ thống có các đơn vị xử lý khác nhau về đặc tính/khả năng. | W05 slide 19; diễn giải tên |
| Đa xử lý bất đối xứng (asymmetric multiprocessing) | Trong mô hình nguồn, một bộ xử lý chủ làm định thời/I/O; các bộ xử lý còn lại chạy user code. | W05 slide 21 |
| Bộ xử lý chủ (master server) | Bộ xử lý đảm nhiệm các công việc hệ thống tập trung trong mô hình bất đối xứng của slide. | W05 slide 21 |
| Nghẽn cổ chai (bottleneck) | Một điểm tập trung công việc hạn chế hiệu năng chung, chẳng hạn master quá tải. | W05 slide 21 |
| Đa xử lý đối xứng (symmetric multiprocessing / SMP) | Mỗi bộ xử lý tự định thời; có thể dùng ready queue chung hoặc hàng riêng cho từng CPU. | W05 slide 23 |
| Khóa (lock) | Cơ chế kiểm soát truy cập dữ liệu chung, tránh nhiều CPU chọn cùng một tiểu trình khi dùng queue chung. | W05 slide 24 |

## Cân bằng tải

| Khái niệm (English) | Định nghĩa/dấu hiệu | Nguồn |
|---|---|---|
| Tải công việc (workload) | Khối lượng công việc cần được xử lý. | W05 slide 25 |
| Cân bằng tải (load balancing) | Phân phối tải giữa các CPU, tránh CPU quá bận trong khi CPU khác rỗi. | W05 slide 25 |
| Di chuyển kiểu đẩy (push migration) | Tác vụ kiểm tra tải và đẩy công việc từ CPU quá tải sang CPU khác. | W05 slide 25 |
| Di chuyển kiểu kéo (pull migration) | CPU rỗi kéo công việc đang chờ từ CPU bận. | W05 slide 25 |

## Liên kết với bộ xử lý

| Khái niệm (English) | Định nghĩa/dấu hiệu | Nguồn |
|---|---|---|
| Tính liên kết với bộ xử lý (processor affinity) | Xu hướng giữ tác vụ trên CPU đã chạy nó để tận dụng dữ liệu còn trong cache, giảm phí chuyển CPU. | W05 slide 26 |
| Liên kết mềm (soft affinity) | Hệ thống cố giữ tác vụ ở CPU cũ nhưng không bảo đảm. | W05 slide 27 |
| Liên kết cứng (hard affinity) | Ràng buộc tập CPU mà tiến trình được phép chạy. Tập có thể gồm một hoặc nhiều CPU. | W05 slide 27–28 |

## Dễ nhầm

- **Asymmetric:** một CPU chủ đảm nhiệm công việc hệ thống theo mô hình slide. **Symmetric:** các CPU tự định thời, không có một CPU chủ cố định cho mọi việc đó.
- **Push:** công việc được đẩy khỏi CPU bận. **Pull:** CPU rỗi chủ động kéo việc về.
- **Load balancing** có thể cần dời việc sang CPU khác; **affinity** khuyến khích giữ CPU để tận dụng cache. Hệ thống phải cân nhắc hai mục tiêu.
- Chuyển CPU có thể làm mất lợi ích cache cũ và cần nạp dữ liệu vào cache mới. Không học câu mô tả ở slide 26 thành quy tắc mọi lần di chuyển đều phải xóa toàn bộ cache CPU cũ.
- **Hard affinity** không bắt buộc ghim vào đúng một CPU; hình slide 28 cho thấy có thể chọn nhiều CPU trong tập được phép.
