# Phần 1 — First-Come, First-Served (FCFS)

Nguồn chính: **W04 slide 29–33**. Tập trung nhận diện thuật ngữ và quy tắc chọn; chưa giải các bảng ví dụ.

## Các từ cần nhớ

| Khái niệm (English) | Định nghĩa/dấu hiệu | Nguồn |
|---|---|---|
| Đến trước, phục vụ trước (First-Come, First-Served / FCFS) | Tiến trình yêu cầu CPU trước được phục vụ trước, theo thứ tự hàng đợi. | W04 slide 29 |
| Vào trước, ra trước (First-In, First-Out / FIFO) | Nguyên tắc hàng đợi dùng để hiện thực FCFS: thêm cuối, lấy đầu. | W04 slide 29 |
| Đầu hàng đợi (head) | Vị trí lấy tiến trình kế tiếp trong cách hiện thực FCFS. | W04 slide 29; nhãn head còn có ở W03 slide 22 |
| Cuối hàng đợi (tail) | Vị trí thêm tiến trình mới vào hàng đợi. | W04 slide 29; nhãn tail ở W03 slide 22 |
| Không trưng dụng (non-preemptive) | Tiến trình giữ CPU đến khi kết thúc hoặc bị blocked do I/O. | W04 slide 29 |
| Giản đồ Gantt (Gantt chart) | Trục thời gian biểu diễn tiến trình nào chạy trên từng khoảng CPU. | W04 slide 30–33 |

## Dễ nhầm

- **FCFS** là giải thuật định thời; **FIFO** là nguyên tắc thứ tự hàng đợi mà nó sử dụng. Đọc đúng đối tượng đề hỏi.
- FCFS không tự chọn công việc có CPU burst ngắn nhất và không tự ưu tiên số priority nhỏ nhất.
- Tiến trình mới đến không đoạt CPU của tiến trình đang chạy trong FCFS không trưng dụng.
- Với tiến trình quay lại ready sau I/O, xét vị trí nó được đưa lại vào hàng đợi, không mặc định nó đứng trước mọi tiến trình chỉ vì đã được tạo sớm hơn.
