# Phần 1 — Shortest-Remaining-Time-First (SRTF)

Nguồn chính: **W04 slide 40–47**. Slide 40 định nghĩa SRTF; slide 44–47 có nhận xét và ước lượng CPU burst dùng chung cho SJF/SRTF, không phải một giải thuật riêng.

## Các từ cần nhớ

| Khái niệm (English) | Định nghĩa/dấu hiệu | Nguồn |
|---|---|---|
| Thời gian còn lại ngắn nhất trước (Shortest-Remaining-Time-First / SRTF) | Biến thể SJF trưng dụng: chọn tiến trình có thời gian CPU còn lại nhỏ nhất trong tập đã đến và còn chạy được, kể cả tiến trình đang chạy. | W04 slide 40 |
| SJF trưng dụng (preemptive SJF) | Tên mô tả khác của SRTF. | W04 slide 40 |
| Thời gian còn lại (remaining time) | Thời gian CPU của burst đang xét chưa được thực hiện; phải trừ phần đã chạy. | W04 slide 40 |
| Trưng dụng (preemption) | Khi công việc sẵn sàng khác có thời gian ngắn hơn phần còn lại của công việc đang chạy, có thể dừng công việc hiện tại và đưa về ready. | W04 slide 40 |

## Bổ trợ chung: dự đoán CPU burst

Nguồn: **W04 slide 45–47**. Công thức ở slide 46 đã đối chiếu ảnh công thức gốc:

`τₙ₊₁ = αtₙ + (1 − α)τₙ`, với `0 ≤ α ≤ 1`.

| Thuật ngữ/ký hiệu | Nhận diện |
|---|---|
| Trung bình hàm mũ (exponential averaging) | Kết hợp burst vừa đo với ước lượng trước để dự đoán burst tiếp theo. |
| `tₙ` | Độ dài CPU burst vừa đo được. |
| `τₙ` | Độ dài đã dự đoán cho burst thứ n. |
| `τₙ₊₁` | Dự đoán cho burst tiếp theo. |
| `α` | Trọng số của số đo vừa có; `1 − α` là trọng số của dự đoán trước. |

Khi `α = 1/2`, hai thành phần có trọng số bằng nhau, như W04 slide 46. `tₙ` ở đây là **thời lượng burst**, không phải ký hiệu thời điểm chạy lần đầu trong bài tiêu chuẩn định thời.

## Dễ nhầm

- **SJF không trưng dụng:** chọn burst ngắn khi CPU rảnh. **SRTF:** có thể chọn lại và đoạt CPU khi tiến trình ngắn hơn đến.
- So **remaining time**, không so mãi CPU burst ban đầu của tiến trình đã chạy một phần.
- “Có tiến trình mới” chưa đủ để đổi CPU; phải có thời gian nhỏ hơn phần còn lại theo tiêu chí SRTF. Trường hợp bằng nhau theo quy ước xử lý hòa của đề.
- **Exponential averaging** là cách dự đoán burst, không phải tên một chính sách chọn CPU thay cho SJF/SRTF.
