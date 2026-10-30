# Phần 1 — Các khái niệm cơ bản về định thời

Nguồn chính: **W04 slide 5–8**. Bổ trợ về khung giải thuật/chế độ quyết định: **W04 slide 24–27**. Tiêu đề theo chủ đề LMS, không tự đặt số mục 4.x mới.

## Định thời và chu kỳ CPU–I/O

| Khái niệm (English) | Định nghĩa/dấu hiệu | Nguồn |
|---|---|---|
| Định thời (scheduling) | Chiến lược lựa chọn công việc/tiến trình phù hợp để thực thi theo mục tiêu hệ thống. | W04 slide 5 |
| Định thời CPU (CPU scheduling) | Chọn tiến trình trong ready queue để sử dụng CPU kế tiếp. Với nhân hỗ trợ luồng, đối tượng được chọn có thể là kernel thread. | W04 slide 16 |
| Đa nhiệm (multitasking) | Cho nhiều chương trình cùng tiến triển bằng cách phân chia khả năng xử lý. | W04 slide 5 |
| Chu kỳ CPU–I/O (CPU–I/O burst cycle) | Quá trình thực thi xen kẽ các đợt dùng CPU và chờ I/O. | W04 slide 6 |
| Đợt thực thi CPU (CPU burst) | Một đợt tiến trình sử dụng CPU trước khi chuyển sang chờ I/O hoặc kết thúc. | W04 slide 6 |
| Thời gian phục vụ/thời lượng đợt CPU (service time / burst time) | Thời gian CPU cần cho một đợt thực thi trong mô hình slide; không phải toàn bộ thời gian từ lúc đến đến lúc hoàn tất. | W04 slide 6 |
| Tiến trình hướng CPU (CPU-bound process) | Nặng tính toán; thời gian hoàn thành chịu ảnh hưởng lớn bởi tốc độ CPU, thường có CPU burst dài. | W04 slide 6–7 |
| Tiến trình hướng I/O (I/O-bound process) | Nặng I/O; dành nhiều thời gian chờ thao tác nhập/xuất, thường có các CPU burst ngắn. | W04 slide 8 |

Câu “tại mỗi thời điểm, chỉ có một tiến trình được thực thi” ở W04 slide 5 được hiểu trong **mô hình một CPU/đơn vị xử lý** của phần cơ bản. Hệ thống nhiều lõi có thể chạy nhiều luồng/tiến trình song song; không dùng câu đó để phủ nhận Ch4 phần đa bộ xử lý.

## Khung của giải thuật định thời

| Khái niệm (English) | Dấu hiệu nhận biết | Nguồn |
|---|---|---|
| Giải thuật định thời (scheduling algorithm) | Quy tắc chọn công việc được chạy và thời điểm áp dụng quy tắc đó. | W04 slide 24 |
| Hàm chọn lựa (selection function) | Trả lời “chọn ai?” dựa vào độ ưu tiên, CPU burst, tài nguyên,… | W04 slide 24 |
| Chế độ quyết định (decision mode) | Trả lời “lúc nào chọn lại?” | W04 slide 24–25 |
| Không trưng dụng (non-preemptive) | Khi đã được CPU, tiến trình giữ CPU tới khi kết thúc hoặc tự phải chờ, chẳng hạn I/O. | W04 slide 25 |
| Trưng dụng (preemptive) | Hệ điều hành có thể lấy lại CPU của tiến trình còn chạy được, đưa nó về ready. | W04 slide 25 |

W04 slide 26 nêu các thời điểm xét chọn: running → waiting, running → ready, waiting/new → ready, tiến trình kết thúc. Khi tiến trình đang chạy đã chờ hoặc kết thúc, phải xét ai chạy tiếp; khi một tiến trình khác trở nên ready, có đoạt CPU ngay hay không còn tùy chế độ/giải thuật. Không phải cứ có tiến trình mới đến là mọi giải thuật đều trưng dụng.

## Dễ nhầm

- **CPU burst/service time** đo lượng CPU cần; **turnaround time** còn tính thời gian chờ từ lúc đến đến lúc hoàn tất.
- **Preemption** đưa một tiến trình còn chạy được về ready; **blocking** làm nó phải chờ I/O/sự kiện.
- **Selection function** nói căn cứ chọn, **decision mode** nói thời điểm chọn. “Ưu tiên cao nhất” là căn cứ, chưa đủ kết luận preemptive hay non-preemptive.
