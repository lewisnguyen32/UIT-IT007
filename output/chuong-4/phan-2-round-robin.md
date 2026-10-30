# Phần 2 — Round Robin (RR)

Nguồn chính: **W04 slide 54–63**. Dấu hiệu chính là luân phiên theo một lát thời gian, không chọn công việc theo CPU burst ngắn nhất.

## Các từ cần nhớ

| Khái niệm (English) | Định nghĩa/dấu hiệu | Nguồn |
|---|---|---|
| Luân phiên (Round Robin / RR) | Mỗi tiến trình đến lượt nhận CPU tối đa một quantum; nếu vẫn còn cần CPU khi hết quantum thì bị trưng dụng và về cuối ready queue. | W04 slide 54 |
| Lát thời gian (time slice) | Khoảng CPU cấp cho một lượt chạy. | W04 slide 54 |
| Đơn vị/lượng tử thời gian (time quantum / quantum time / quantum) | Tên gọi của độ dài lát thời gian; thường ký hiệu `q`. Slide dùng `quantum time`. | W04 slide 54 |
| Trưng dụng (preemption) | Lấy lại CPU khi quantum hết mà tiến trình chưa nhường/kết thúc. | W04 slide 54 |
| Chuyển ngữ cảnh (context switch) | Đổi ngữ cảnh thực thi khi chuyển sang tiến trình khác; phát sinh chi phí. | W04 slide 58–59, 62 |
| Phí tổn hệ điều hành (OS overhead) | Trong phần này, thời gian CPU dành cho việc chuyển ngữ cảnh thay vì thực thi công việc người dùng. | W04 slide 62–63 |

Tiến trình có thể dùng **ít hơn** một quantum nếu burst hoàn tất hoặc nó phải chờ I/O. Quantum là giới hạn cho một lượt, không phải lượng CPU mà mọi tiến trình bắt buộc phải dùng hết.

## Nhận diện ảnh hưởng của quantum

| Dấu hiệu | Kết luận cần nhớ | Nguồn |
|---|---|---|
| Quantum rất lớn, đủ để mọi burst được phục vụ xong trong một lượt | RR hoạt động như FCFS theo thứ tự hàng đợi. | W04 slide 58, 62 |
| Quantum quá nhỏ so với chi phí chuyển ngữ cảnh | Nhiều lần chuyển, tăng OS overhead. | W04 slide 58, 62–63 |
| Cần đáp ứng tương tác nhanh | Quantum nhỏ thường giúp luân phiên sớm hơn, nhưng phải cân bằng với overhead. | W04 slide 62–63 |

Ví dụ nguồn: quantum 20 ms, chuyển ngữ cảnh 5 ms → phần thời gian overhead trong chu kỳ `20 + 5` là `5/25 = 20%` (W04 slide 63). Đây là ví dụ một chu kỳ đầy quantum rồi chuyển, không phải công thức áp dụng nguyên xi cho mọi workload.

## Dễ nhầm

- **RR** là Round Robin trong bài này; trong bài HRRN, nguồn cũng dùng `RR` để viết tắt **response ratio**. Phải đọc theo ngữ cảnh.
- “Hết quantum” → về **ready**, không phải waiting, nếu tiến trình vẫn chạy được.
- Quantum lớn không bảo đảm turnaround trung bình luôn tốt hơn; W04 slide 60 cũng nhấn mạnh điều này.
- RR cơ bản phục vụ luân phiên, không có tiêu chí “CPU burst dài nhất trước”. Dòng nhận xét “ưu tiên CPU-bound” ở slide 58 không dùng thay định nghĩa lựa chọn của RR.
