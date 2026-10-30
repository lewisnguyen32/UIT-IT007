# Phần 2 — Multilevel Feedback Queue

Nguồn chính: **W05 slide 11–13**; ý tưởng feedback ở **slide 9**, nhận xét so sánh giải thuật ở **slide 15**.

## Các từ cần nhớ

| Khái niệm (English) | Định nghĩa/dấu hiệu | Nguồn |
|---|---|---|
| Hàng đợi đa mức phản hồi (Multilevel Feedback Queue / MLFQ) | Nhiều hàng đợi, cho phép tiến trình chuyển hàng theo đặc tính thực thi/thời gian chờ và quy tắc của hệ thống. MLFQ là viết tắt thông dụng để nhớ tên đầy đủ. | W05 slide 9, 11–13 |
| Phản hồi (feedback) | Dùng hành vi thực thi để điều chỉnh hàng đợi của tiến trình; không gán cố định như Multilevel Queue. | W05 slide 9, 11 |
| Trưng dụng (preemptive) | Chế độ quyết định được nguồn nêu cho MLFQ. | W05 slide 11 |
| Làm mới/tăng ưu tiên (aging) | Tiến trình đợi quá lâu ở hàng thấp có thể được chuyển lên hàng có độ ưu tiên cao hơn. | W05 slide 11 |
| Tiến trình tương tác (interactive process) | Nhóm được mô hình trong nguồn có xu hướng phục vụ ở hàng ưu tiên cao, cùng các tiến trình hướng I/O. | W05 slide 11 |
| Tiến trình hướng CPU (CPU-bound process) | Trong mô hình nguồn, có xu hướng xuống các hàng ưu tiên thấp hơn sau một thời gian. | W05 slide 11 |

W05 slide 12 cho ví dụ ba hàng: Q0 dùng RR quantum 8 ms, Q1 dùng RR quantum 16 ms, Q2 dùng FCFS. Đây là **tham số của ví dụ**; không định nghĩa mọi MLFQ phải có đúng ba hàng hoặc quantum 8/16 ms. Muốn vẽ lịch chạy phải biết thêm quy tắc vào hàng, lên/xuống hàng và ưu tiên giữa các hàng.

## Chọn chính sách và so sánh

W05 slide 13 yêu cầu xác định số hàng, giải thuật mỗi hàng, điều kiện chuyển lên/xuống và hàng ban đầu. Không đủ các quy tắc này thì chưa có một cấu hình MLFQ hoàn chỉnh để tính.

W05 slide 15 nêu việc đánh giá phụ thuộc **tải công việc (system workload)**, hỗ trợ phần cứng cho dispatcher, trọng số các tiêu chuẩn và phương pháp so sánh định lượng. Không có một giải thuật luôn tốt nhất với mọi tải và mọi tiêu chuẩn.

## Dễ nhầm

- **Multilevel Queue:** hàng cố định. **Multilevel Feedback Queue:** có thể đổi hàng.
- **Aging** không bắt buộc chỉ có trong priority scheduling; nguồn cũng dùng nó để đưa tiến trình chờ lâu lên hàng cao trong MLFQ.
- Nhiều hàng dùng RR không tự động thành feedback nếu tiến trình không được chuyển hàng.
