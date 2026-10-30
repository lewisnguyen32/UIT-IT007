# Phần 2 — Highest Response Ratio Next (HRRN)

Nguồn chính: **W05 slide 4**. Công thức nằm trong ảnh của slide, đã được đối chiếu trực tiếp trên nền trắng để đọc đủ tử/mẫu.

## Các từ cần nhớ

| Khái niệm (English) | Định nghĩa/dấu hiệu | Nguồn |
|---|---|---|
| Tỉ số đáp ứng cao nhất kế tiếp (Highest Response Ratio Next / HRRN) | Chọn tiến trình kế tiếp có response ratio lớn nhất. | W05 slide 4 |
| Tỉ số đáp ứng (response ratio) | Tỉ số giữa thời gian đợi cộng thời gian phục vụ dự kiến với thời gian phục vụ dự kiến. | W05 slide 4, ảnh công thức |
| Thời gian đã đợi (time spent waiting) | Thời gian chờ của tiến trình được đưa vào tử số khi xét chọn. | W05 slide 4, ảnh công thức |
| Thời gian phục vụ dự kiến (expected service time) | Lượng thời gian CPU dự kiến cần cho công việc/burst đang xét. | W05 slide 4, ảnh công thức; W04 slide 6 |

Công thức theo ảnh gốc:

`RR = (time spent waiting + expected service time) / expected service time`.

Đặt `w` là thời gian đã đợi, `s > 0` là thời gian phục vụ dự kiến: `RR = (w + s)/s = 1 + w/s`. Chữ `w`, `s` là ký hiệu rút gọn ở bài ôn này, không phải ký hiệu in trong nguồn.

## Dễ nhầm

- HRRN chọn tỉ số **lớn nhất**, không chọn tỉ số nhỏ nhất.
- Với cùng thời gian chờ **dương**, công việc có service time nhỏ hơn có tỉ số cao hơn; khi thời gian chờ bằng 0, mọi tỉ số đều bằng 1. Khi một công việc chờ thêm với service time dự kiến không đổi, tỉ số của chính nó tăng. Không bỏ thành phần thời gian chờ để biến HRRN thành SJF.
- **Response ratio** là một tỉ số, **response time** là một khoảng thời gian. Hai tên không thay thế nhau.
- `RR` trong công thức là **response ratio**; `RR` là tên giải thuật ở bài trước lại có nghĩa **Round Robin**.
- Slide 4 gợi ý so sánh với **aging**: cả hai làm lợi thế của công việc đang chờ tăng theo thời gian, nhưng aging là điều chỉnh độ ưu tiên, còn HRRN xét tỉ số nêu trên. Slide không ghi riêng chế độ quyết định; bảng terms này không lấy việc thiếu nhãn đó làm căn cứ suy ra một biến thể trưng dụng.
