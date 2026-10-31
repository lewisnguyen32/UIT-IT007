# Nguồn và phạm vi ôn Hệ điều hành

## Tài liệu gốc

| Mã | Tệp trong `Lý thuyết/` | Số trang/slide | Bản đọc trong `Lý thuyết/pdf/` |
|---|---|---:|---|
| C01 | `[BHT CNPM] HDH _Chuong1.pdf` | 57 trang PDF | C01.md, C01-index.md, C01-manifest.json |
| W01 | `#Week01-Chapter0 2024.pptx` | 9 slide | W01.md |
| W02 | `#Week02-Chapter2 2024.pptx` | 57 slide | W02.md |
| W03 | `#Week03-Chapter3 2024.pptx` | 64 slide | W03.md |
| W04 | `#Week04-Chapter4-1 2024.pptx` | 74 slide | W04.md |
| W05 | `#Week05-Chapter4-2 2024.pptx` | 59 slide | W05.md |

W01 là Chương 0 giới thiệu môn, không thay Chương 1. C01 được người dùng thêm ngày 30/10/2026. Số slide theo thứ tự trình chiếu trong PPTX, số trang PDF từ 1. Số mục LMS có thể khác số đề mục in trong nguồn.

## Cấu trúc người dùng chỉ định

Ảnh giữ tại `memory/anh-cau-truc/`: `chuong-1.png`, `chuong-2.png`, `chuong-3-tong-quan.png`, `chuong-3-phan-1.png`, `chuong-3-phan-2.png`, `chuong-4.png`. Danh mục đã ghi lại ở `output/THU_TU_HOC_HDH.md` và README từng chương, không cần đọc lại ảnh mỗi lần.

Ch3 dùng ảnh chi tiết: 3.1–3.4, 3.5.1–3.5.3, 3.6 IPC, 3.7 tiểu trình; phần cộng tác nằm cùng ngữ cảnh IPC, không tự đánh thành mục 3.6 rồi đẩy số IPC/tiểu trình lên. Nhãn Done/To do trên ảnh không phải kết quả tự kiểm tại đây.

## Phạm vi

- Đã soạn terms/lý thuyết ngắn Ch1–4; Ch3–4 theo yêu cầu ngày 30/10/2026, chia đúng mục/chủ đề trong ảnh LMS và giữ giới hạn W05 bên dưới. Các bài mới chỉ là bản ôn, chưa phải bằng chứng đã giảng/tự kiểm/chữa/thành thạo hay bộ lời giải bài tính.
- W05 tạm dùng slide 1–28 theo lời người dùng “hình như chỉ tới slide 28”. Slide 29 thực tế ghi “ĐỊNH THỜI THEO THỜI GIAN THỰC (ĐỌC THÊM)”. Từ 29–59 giữ cache để tra, không đưa vào học/tự kiểm/% cơ sở khi chưa đổi phạm vi. Ảnh mục lục Ch4 có thời gian thực/định thời trên một số OS không tự hủy giới hạn này.
- Ch1 1.2 mở rộng tách riêng theo LMS; chưa có xác nhận không thi.
- Các đề cũ nằm trong `Giữa Kỳ/22-24/` (có đề năm 2024–2025). Người dùng cho biết cấu trúc đề mới thay đổi một chút và thêm 3 câu như trong `Giữa Kỳ/User/`. Ảnh `vi-du-tu-luan-mot-tu.png` cho thấy ba ý a–c của một câu tự luận ngắn, đáp án là một số hoặc một từ tiếng Anh; ảnh chỉ là đoạn trích, chưa xác nhận tổng số ý hay điểm của đề mới. Chữ viết tay chưa là đáp án chính thức.
- Chưa chọn bộ đề đầy đủ để luyện hoặc thống kê; không tự đọc file đáp án riêng.
- Tra riêng theo câu hỏi người dùng ngày 31/10/2026 về MLQ/MLFQ: **2024–2025 GK1, trang PDF 2, câu 10** hỏi trực tiếp về Multilevel Feedback Queue; **2023–2024 GK2, trang PDF 2, câu 6** có Multilevel Feedback Queue và Multilevel Queue trong các phương án. Đã đối chiếu cả hai trang gốc và rà độc lập; đây là bằng chứng xuất hiện trong đề cũ, không phải thống kê đầy đủ hay xác nhận đề sắp tới. Cache/hash và giới hạn kiểm tra ở [audit MLQ/MLFQ](../tmp/study_audit/exam-mlq/README.md); không cần trích lại nguồn không đổi.

## Cache và đối chiếu đã có

Extraction do GPT‑6.1 Terra thực hiện. PPTX có `index.md` và `manifest.json`; PDF C01 có chỉ mục/manifest riêng. Hash SHA256, size/mtime, fingerprint script và số trang/slide giúp tái dùng bản đọc. Chạy công cụ chỉ khi thiếu/đổi nguồn hoặc lỗi cụ thể; không tự chạy mỗi phiên. Script dùng Python, PDF cần pypdf. Đường dẫn nguồn mặc định lấy theo gốc thư mục chứa `tools/`.

- PPTX: giữ chữ, bảng theo hàng/cột; đánh dấu ảnh, ô gộp, nội dung nhúng và Office Math. Toán được giữ chữ phẳng, chưa bảo toàn cấu trúc phân số/lũy thừa; phải xem công thức gốc khi tính.
- C01: có chỗ chữ dính, tiêu đề tự động đôi khi lẫn copyright. Trang 26/29/38/49/57 ít chữ; các trang nhiều chữ vẫn có thể thiếu nhãn trong hình. Dùng mục lục bài ôn để định vị thay vì nạp cả cache.
- Đã kiểm hình C01 trang 22 (tháp lưu trữ), 26 (I/O), 29 (Von Neumann/DMA), 38 (dual-core), 39 (NUMA), 52–53 (user/kernel mode, mode bit). Nhãn còn thiếu trong trích chữ đã được dùng đúng trong bài soạn; tái dùng phần đó, chỉ mở nguồn khi có nghi vấn mới.
- C01 trang 27 nói DMA “không cần CPU”; đọc cùng hình 29, không học thành CPU hoàn toàn không tham gia. C01 trang 36 mô tả SMP khái quát; bài ôn tránh hiểu mọi CPU phải chạy cùng một công việc.
- Đã kiểm bổ sung để soạn terms Ch3–4: hình W03 slide 7 (compiler/linker/loader), 8 (layout bộ nhớ C), 16 (PCB), 22–23 (hàng đợi), 27 (context switch); chiều/nhãn 6 mũi tên slide 12 đối chiếu XML gốc. Không cần trích lại các hình này khi không có nghi vấn mới.
- Đã kiểm ảnh công thức W04 slide 21 (`R=t₀−r`, `F=f−r`, `W=f−r−E`), 46 (exponential averaging); W05 slide 4 (HRRN) và hình slide 28 (Task Manager chọn tập CPU affinity). Công thức `W=F−E` cần điều kiện mô hình không có thời gian chờ I/O; bài ôn đã ghi giới hạn. W04 slide 47 là hình minh họa dự đoán, chưa dùng số liệu của hình để tính. Bản đọc không thay được sơ đồ/mũi tên.
- W03 slide 35–36 có `if(fork() = 0)` không hợp lệ trong C; slide 38 nhập nhằng `abort` nhận PID; slide 47 ví dụ nhận qua mailbox không nhất quán ký hiệu. Đã xác nhận các chữ này từ XML gốc, không phải lỗi cache. Bài ôn ghi ngay tại mục liên quan; nguồn gốc giữ nguyên. Đối chiếu GNU C Library làm rõ fork/exec/abort, Linux man-pages làm rõ wait(NULL), nguồn OS-book Ch5 trang PDF 7–8 làm rõ scheduler/dispatcher (W04 slide 18 gộp hai vai trò). Link ngoài nằm tại bài liên quan.

Đã có rà soát độc lập cache, số trang/slide, mốc28/29 và bài soạn Ch1–2. Ngày 30/10/2026 đã rà độc lập đủ 22 bài terms Ch3–4 và hai README, sửa các điểm tìm được; kiểm liên kết nội bộ/bảng và hash W03–W05 đều khớp. Không cần rà/trích lại toàn bộ nếu chưa có thay đổi hay nghi vấn mới.
