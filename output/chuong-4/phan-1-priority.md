# Phần 1 — Priority Scheduling

Nguồn chính: **W04 slide 49–52**. Cần biết căn cứ độ ưu tiên, hai chế độ quyết định và cơ chế chống trì hoãn vô hạn.

## Các từ cần nhớ

| Khái niệm (English) | Định nghĩa/dấu hiệu | Nguồn |
|---|---|---|
| Định thời theo độ ưu tiên (priority scheduling) | Chọn tiến trình sẵn sàng có độ ưu tiên cao nhất. | W04 slide 49 |
| Độ ưu tiên (priority) | Giá trị biểu diễn mức ưu tiên; thường là số nhưng chiều lớn/nhỏ do quy ước. | W04 slide 49 |
| Theo độ ưu tiên, có trưng dụng (preemptive priority scheduling) | Tiến trình ưu tiên cao hơn trở nên ready có thể đoạt CPU. | W04 slide 49, đọc cùng slide 25 |
| Theo độ ưu tiên, không trưng dụng (non-preemptive priority scheduling) | Ưu tiên cao hơn không tự đoạt CPU giữa burst đang chạy; chọn khi CPU được nhường. | W04 slide 49, đọc cùng slide 25 |
| Đói tài nguyên/trì hoãn vô hạn (starvation / indefinite blocking) | Tiến trình ưu tiên thấp có thể không được chạy nếu công việc ưu tiên cao liên tục xuất hiện. | W04 slide 51; thuật ngữ starvation ở slide 44 |
| Làm mới/tăng ưu tiên theo thời gian chờ (aging) | Tăng dần độ ưu tiên của tiến trình chờ lâu để chống starvation. Slide gọi là “làm mới”. | W04 slide 51 |

W04 slide 50 nêu có thể gán ưu tiên theo CPU burst ước lượng, bộ nhớ, số file mở, tỉ lệ I/O/CPU hoặc yêu cầu bên ngoài. SJF có thể xem là dùng ưu tiên dựa trên burst: ngắn hơn được ưu tiên hơn.

## Dễ nhầm

- **Priority cao nhất** không mặc định là **số lớn nhất** hay **số nhỏ nhất**. W04 slide 49 nói rõ có thể theo hai chiều; khi làm bài phải dùng quy ước của đề.
- **Priority scheduling** có thể trưng dụng hoặc không. Không nhìn chữ priority rồi tự chọn một chế độ.
- **Aging** tăng độ ưu tiên theo thời gian chờ; nếu số nhỏ biểu thị ưu tiên cao thì “tăng ưu tiên” có thể là **giảm con số priority**.
- **Starvation** là chờ vô hạn vì cách phục vụ; không đồng nhất với deadlock (các tiến trình bế tắc do chờ nhau).
