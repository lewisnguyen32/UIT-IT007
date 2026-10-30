# Phần 1 — Các tiêu chuẩn định thời CPU

Nguồn chính: **W04 slide 20–22**. Công thức ở slide 21 đã đối chiếu trực tiếp với bản ảnh công thức trong PPTX, không suy từ chữ phẳng của cache.

## Các tiêu chuẩn

| Tiêu chuẩn (English) | Định nghĩa/dấu hiệu | Mục tiêu | Nguồn |
|---|---|---|---|
| Thời gian đáp ứng (response time) | Từ lúc gửi yêu cầu đến lần được đáp ứng đầu tiên. Trong bài định thời CPU, tính từ lúc đến đến lần đầu được chạy. | Giảm | W04 slide 20–21 |
| Thời gian hoàn thành (turnaround time) | Khoảng thời gian từ lúc tiến trình đến/được nạp vào hệ thống đến khi kết thúc. | Giảm | W04 slide 20–21 |
| Thời gian đợi (waiting time) | Tổng thời gian tiến trình ở trong ready queue để chờ CPU. | Giảm | W04 slide 20 |
| Hiệu suất sử dụng CPU (CPU utilization / processor utilization) | Mức độ CPU được giữ bận. Slide dùng tên `processor utilization`. | Tăng | W04 slide 22 |
| Thông lượng (throughput) | Số tiến trình hoàn tất trong một đơn vị thời gian. | Tăng | W04 slide 22 |
| Tính công bằng (fairness) | Đối xử công bằng giữa các tiến trình theo chính sách hệ thống; không phải lúc nào cũng chia CPU thành các phần bằng nhau. | Bảo đảm theo chính sách | W04 slide 22; diễn giải giới hạn |

Slide 20 xếp ba tiêu chuẩn thời gian vào hướng người dùng (**user-oriented**); slide 22 xếp utilization, fairness, throughput vào hướng hệ thống (**system-oriented**).

## Thời điểm khác thời lượng

| Thuật ngữ (English) | Ký hiệu của W04 slide 21 | Ý nghĩa |
|---|---|---|
| Thời điểm đến (arrival time / release time) | `r` | Lúc tiến trình xuất hiện trong hệ thống. |
| Thời điểm chạy lần đầu (first execution time) | `t₀` | Lúc tiến trình được thực thi lần đầu; tên tiếng Anh là diễn giải. |
| Thời điểm kết thúc (finishing time) | `f` | Mốc tiến trình hoàn tất. |
| Tổng thời gian CPU yêu cầu (total CPU burst time) | `E` | Tổng thời lượng các đợt CPU, slide minh họa `E = E₁ + E₂ + E₃`. |

Theo W04 slide 21:

- Response time: `R = t₀ − r`.
- Turnaround time: `F = f − r`.
- Waiting time trong mô hình chỉ có chạy CPU và đợi CPU: `W = f − r − E = F − E`.

**Giới hạn công thức waiting:** nếu tiến trình còn có khoảng bị blocked để chờ I/O, `F − E` có thể bao gồm cả thời gian chờ I/O, nên không tự coi toàn bộ là waiting time. Định nghĩa chuẩn trong W04 slide 20 vẫn là **thời gian ở ready queue**; bài có I/O phải theo đúng mô hình và dữ kiện. Slide 21 không nói rõ điều kiện này, nên ghi riêng để tránh áp dụng sai.

## Dễ nhầm

- **Finishing time `f`** là một mốc; **turnaround time `F`** là một khoảng. Từ tiếng Việt “thời gian hoàn thành” trong đề cần đọc theo định nghĩa và ký hiệu kèm theo.
- **Response** dừng ở lần đầu được phục vụ; **turnaround** kéo dài đến khi hoàn tất.
- **Waiting** chỉ tính chờ CPU trong ready queue, không phải mọi thời gian tiến trình không chạy.
- **Throughput** đo số việc hoàn tất/đơn vị thời gian; **CPU utilization** đo mức CPU bận. Hai đại lượng khác nhau.
