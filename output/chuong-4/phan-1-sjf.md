# Phần 1 — Shortest-Job-First (SJF)

Nguồn chính: **W04 slide 35–39**, nhận xét chung ở **slide 44–47**. Bài này tập trung SJF không trưng dụng; biến thể trưng dụng là [SRTF](phan-1-srtf.md).

## Các từ cần nhớ

| Khái niệm (English) | Định nghĩa/dấu hiệu | Nguồn |
|---|---|---|
| Công việc ngắn nhất trước (Shortest-Job-First / SJF) | Chọn tiến trình có CPU burst kế tiếp ngắn nhất trong các tiến trình sẵn sàng. | W04 slide 35 |
| SJF không trưng dụng (non-preemptive SJF) | Khi CPU rảnh, chọn burst ngắn nhất; sau khi đã chọn, tiến trình giữ CPU đến hết burst hoặc kết thúc, không bị công việc mới đến đoạt CPU. | W04 slide 36; đọc cùng slide 25 |
| Đợt CPU (CPU burst) | Lượng CPU của đợt cần thực thi được dùng làm tiêu chí “ngắn nhất”. | W04 slide 35 |
| Đói tài nguyên (starvation) | Tiến trình có burst dài có thể bị trì hoãn vô hạn nếu công việc ngắn cứ liên tục được ưu tiên. | W04 slide 44 |
| Ước lượng CPU burst (CPU-burst prediction) | Cần dự đoán độ dài đợt CPU tiếp theo vì thường chưa biết chính xác trước khi chạy. | W04 slide 45–47 |

Slide 35 nói SJF có cả hai chiến lược trưng dụng và không trưng dụng; slide 40 đặt tên biến thể trưng dụng là SRTF. Vì vậy khi đề chỉ viết “SJF”, phải xem chế độ quyết định hoặc quy ước được nêu.

## Dễ nhầm

- **Shortest** xét CPU burst kế tiếp, không phải thời gian đã đợi hoặc thời điểm đến sớm nhất.
- Chỉ chọn trong tập **đã đến và sẵn sàng**, không chạy một tiến trình chưa xuất hiện chỉ vì nó có burst nhỏ.
- Không trưng dụng: công việc ngắn hơn mới đến phải chờ tới khi CPU được nhường; SRTF thì có thể đoạt CPU.
- Nhận xét “tối ưu thời gian đợi trung bình” của slide 40/45 cần đúng giả thiết. Trường hợp cơ bản: các tiến trình sẵn sàng cùng lúc và biết đúng độ dài burst, xếp burst tăng dần cho thời gian đợi trung bình nhỏ nhất. Không suy rộng SJF không trưng dụng tối ưu cho mọi bộ thời điểm đến khác nhau.
- Kỹ thuật trung bình hàm mũ dùng chung cho dự đoán burst SJF/SRTF được giữ ở [bài SRTF, phần bổ trợ](phan-1-srtf.md).
