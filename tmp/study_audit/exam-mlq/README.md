# Kiểm MLQ/MLFQ trong đề cũ — 31/10/2026

Lý do: người dùng hỏi “đề thi có MLQ hoặc MLFQ không”. Trước đó chưa có cache chữ cho bốn PDF đề cũ trong `Giữa Kỳ/22-24/`. GPT-6.1 Terra đã trích chữ và tìm từ khóa; agent chính kiểm lại hai trang gốc liên quan. Không chỉnh PDF nguồn, không dùng đáp án riêng để kết luận.

## Bằng chứng đã kiểm trang gốc

- `[BHT CNPM] HDH 2024-2025 GK1.pdf`: trang PDF 2, câu 10 hỏi chọn phát biểu đúng về Multilevel Feedback Queue. Ảnh đối chiếu: `2024-question-page2.png`.
- `[BHT CNPM] HDH 2023-2024 GK2.pdf`: trang PDF 2, câu 6 hỏi chọn phát biểu sai về các giải thuật định thời; Multilevel Feedback Queue và Multilevel Queue đều có trong phương án. Ảnh đối chiếu: `2023-gk2-question-page2.png`.

Đủ kết luận MLFQ đã được hỏi trực tiếp và MLQ xuất hiện trong nội dung trắc nghiệm của đề cũ. Không suy ra tần suất hay phạm vi đề sắp tới; không giải các câu này tại lần tra này.

## Cache và giới hạn

- `manifest.json`: đường dẫn nguồn, SHA-256, số trang, số ký tự từng trang, đường dẫn cache và các đoạn có từ khóa.
- Các tệp `.txt` là cache chữ theo trang; `audit.py` là lệnh trích và tìm từ khóa. Chỉ tái trích khi nguồn đổi hoặc cache có lỗi cụ thể.
- Terra còn tìm được tên Multilevel Queue ở đề 2022–2023 GK1, trang PDF 3, câu 15, trong một phương án; chưa kiểm ảnh trang đó, không dùng làm bằng chứng chính trong câu trả lời.
- Đề 2023–2024 GK1 (Có đáp án) không có lớp chữ trên cả 4 trang, chưa OCR/kiểm ảnh và chưa kết luận nội dung đề đó. Đề 2024–2025 GK1 không có lớp chữ ở trang 5–8; lần tra này không kiểm phần đó. Không coi việc không tìm thấy chữ là bằng chứng không có thuật ngữ.
- Các ảnh trích cũ ngoài thư mục này có lẫn trang lời giải. Hai ảnh `sched-2024-6.png`, `sched-2024-7.png` đã được mở nhầm trước khi xác định loại trang; đã dừng dùng và không lấy làm căn cứ.
