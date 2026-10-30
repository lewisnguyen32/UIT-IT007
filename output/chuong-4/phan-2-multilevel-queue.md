# Phần 2 — Multilevel Queue

Nguồn chính: **W05 slide 6–9**. Dấu hiệu phân biệt quan trọng: tiến trình được **gán cố định** vào một hàng đợi.

## Các từ cần nhớ

| Khái niệm (English) | Định nghĩa/dấu hiệu | Nguồn |
|---|---|---|
| Hàng đợi đa mức (Multilevel Queue) | Chia ready queue thành nhiều hàng riêng theo đặc điểm/loại tiến trình; mỗi hàng có thể dùng giải thuật riêng. | W05 slide 6 |
| Tiền cảnh (foreground) | Nhóm công việc tương tác (interactive) trong ví dụ phân loại của nguồn. | W05 slide 6–7 |
| Hậu cảnh (background) | Nhóm công việc nền, được tách khỏi nhóm tương tác trong ví dụ. | W05 slide 6–7 |
| Định thời ưu tiên cố định (fixed-priority scheduling) | Giữa các hàng đợi: phục vụ từ hàng ưu tiên cao đến thấp; hàng thấp có thể bị starvation. | W05 slide 7 |
| Phân chia lát thời gian (time slice) | Giữa các hàng đợi: phân một phần thời gian CPU cho từng hàng, rồi mỗi hàng phục vụ các tiến trình bên trong. | W05 slide 7 |
| Đói tài nguyên (starvation) | Hàng ưu tiên thấp có thể chờ vô hạn nếu hàng trên luôn có việc và được ưu tiên tuyệt đối. | W05 slide 7 |
| Phản hồi (feedback) | Cơ chế cho phép chuyển tiến trình giữa các hàng; dùng để khắc phục hạn chế gán cố định, dẫn tới Multilevel Feedback Queue. | W05 slide 9 |

Ví dụ W05 slide 7: foreground được 80% thời gian và dùng RR; background được 20% và dùng FCFS. **80/20 là một ví dụ**, không phải tỉ lệ bắt buộc của Multilevel Queue.

## Dễ nhầm

- **Trong một hàng đợi** có giải thuật riêng; **giữa các hàng đợi** cũng phải có chính sách chọn/phân CPU. Đừng chỉ nêu RR/FCFS rồi bỏ qua bước chọn hàng.
- **Multilevel Queue:** không chuyển hàng trong mô hình này. **Multilevel Feedback Queue:** được chuyển hàng theo quy tắc.
- “Có nhiều hàng đợi” chưa đủ để kết luận feedback; cần dấu hiệu **di chuyển tiến trình giữa các hàng**.
