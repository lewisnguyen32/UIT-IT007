# Chương 3 — Kết quả và điểm cần ôn

## C03-TN-20261104-02 — 10 câu trắc nghiệm tiếp theo — đã trả lời/chữa 04/11/2026

Bộ tự soạn theo yêu cầu tiếp tục trắc nghiệm sâu/rộng Ch3, bốn phương án A–D, một đáp án đúng nhất. Nguyên văn và nguồn theo câu tại [bộ trắc nghiệm Ch3](../output/chuong-3/trac-nghiem-on-tap.md#c03-tn-20261104-02--10-câu-tiếp-theo). Nội dung: concurrency/parallelism, chuỗi trạng thái, lời gọi hệ thống và chuyển ngữ cảnh, PC/ngữ cảnh thread, CPU-bound/I/O-bound, fork/exec/wait, giá trị trả về fork, IPC, giới hạn song song Many-to-Many và lợi ích đa tiểu trình. Câu 3–4 kiểm tra lại hai ý chưa chắc ở bộ trước. Đã rà độc lập bằng subagent và sửa cách diễn đạt câu 4C để rõ khôi phục con trỏ stack chứ không sao chép toàn bộ stack. Đã trả lời/chữa: 7/10 đúng (1, 2, 4, 5, 7, 8, 10), đúng định dạng A–D; chưa kết luận thành thạo hay ôn trọn mục.

Trả lời thực tế các câu đúng: `1. B; 2. D; 4. C; 5. B; 7. A; 8. C; 10. D`. Câu 4 kiểm tra lại PC/ngữ cảnh riêng của thread đã chọn đúng theo tình huống. Câu 3, 6, 9 chỉ lưu chi tiết câu hỏi/câu trả lời sai/lời chữa tại [CS-C03-013–015](cau-sai/chuong-3.md). Câu 3 người dùng nói chưa biết và đoán, không xem là có hiểu chắc từ bộ trước.

## C03-TN-20261104-01 — 10 câu trắc nghiệm sâu/rộng — đã trả lời/chữa 04/11/2026

Người dùng yêu cầu đổi sang trắc nghiệm giống cấu trúc đề thi và hỏi sâu/rộng Chương 3. Bộ tự soạn 10 câu, mỗi câu bốn phương án A–D, một đáp án đúng nhất; nguyên văn và nguồn theo câu tại [bộ trắc nghiệm Ch3](../output/chuong-3/trac-nghiem-on-tap.md#c03-tn-20261104-01--10-câu). Phủ mục 3.1–3.7, gồm hai câu chọn phát biểu sai, tình huống, ghép chức năng, phân loại IPC và đọc mã fork. Đã đối chiếu W03/bài soạn và được subagent rà độc lập. Đã trả lời/chữa: 10/10 đúng; câu 3 và 9 đúng nhưng người dùng chưa chắc, không ghi là sai hay kết luận thành thạo.

Trả lời thực tế ngoài câu 2: `1. C; 3. D (?); 4. A; 5. C; 6. B; 7. D; 8. A; 9. C (Không chắc khúc PC); 10. B`. Câu 2 ôn lại nội dung device queue theo tình huống; trả lời/kết quả kiểm tra lại chỉ lưu tại [CS-C03-004](cau-sai/chuong-3.md), chưa kiểm tra lại khả năng tự nhớ từ device. Đã giải thích riêng câu 3: ngắt/lời gọi hệ thống không bắt buộc đổi tiến trình (W03 slide 16, 27 và ghi chú bài soạn); câu 9: mỗi thread có PC riêng để theo dõi vị trí lệnh tiếp theo dù dùng chung code (W03 slide 50–51).

## C03-TS-20261104-01 — 10 câu cơ bản Chương 3 — đã trả lời/chữa 04/11/2026

Câu tự soạn từ `output/chuong-3/`, ngày 04/11/2026; mỗi câu trả lời một từ tiếng Anh hoặc một số. Đã trả lời/chữa: 9/10 đúng (câu 1–8, 10), đúng cả thuật ngữ và định dạng; câu 9 chưa nhớ, chưa đủ bằng chứng đánh giá hiểu khái niệm. Chưa kết luận thành thạo hay ôn trọn mục.

Trả lời thực tế các câu 1–7 (đều đúng): `1. program; 2. process; 3. heap; 4. stack; 5. ready; 6. waiting; 7. Control`. Chấp nhận chữ hoa ở Control. Kết quả kiểm tra lại câu 8–10 chỉ lưu tại [CS-C03-002, CS-C03-004, CS-C03-005](cau-sai/chuong-3.md).

1. Thực thể bị động, có thể được lưu trên đĩa dưới dạng tập tin thực thi, gọi là gì?
2. Một chương trình đang thực thi, được xem là thực thể chủ động, gọi là gì?
3. Vùng nhớ chứa bộ nhớ được cấp phát động, chẳng hạn vùng được cấp bởi malloc, gọi là gì?
4. Vùng nhớ chứa dữ liệu tạm của lời gọi hàm, như tham số hàm và địa chỉ trở về, gọi là gì?
5. Tiến trình đã sẵn sàng thực thi nhưng đang chờ được cấp CPU ở trạng thái nào?
6. Tiến trình đang chờ I/O hoàn tất hoặc chờ một sự kiện ở trạng thái nào?
7. Điền tên cấu trúc lưu thông tin quản lý của một tiến trình: Process _____ Block.
8. Điền tên bộ phận giữ địa chỉ lệnh sẽ thực thi tiếp theo: program _____.
9. Điền tên hàng đợi chứa các tiến trình đang chờ một thiết bị I/O: _____ queue.
10. Trong sơ đồ trạng thái của tài liệu, thao tác chuyển tiến trình từ ready sang running có nhãn gì?

Nguồn: W03 slide — câu 1–2: 5; câu 3: 6, 8; câu 4: 6; câu 5–6: 11; câu 7–8: 16; câu 9: 22–23; câu 10: 12.

Mốc hiện tại ở [memory.md](../memory.md); bài soạn ở [mục lục Ch3](../output/chuong-3/README.md).

- Mục 3.5 (01/11/2026), ảnh bài fork người dùng gửi: `x=24; f=fork();` rồi ba vòng `i=0..2`, mỗi vòng `fork(); x=x+i;`; sau vòng lặp, nhánh `f==0` in `x`, gọi `fork()` và cộng 2. Người dùng hỏi “8 tiến trình 27, 16 tiến trình 29 đúng không” — đúng nếu xét giá trị x cuối chương trình: 8 tiến trình x=27, 16 tiến trình x=29, tổng 24 (giả sử fork thành công). Đã giải thích lệnh in x nằm trước fork cuối và trước cộng 2 nên được gọi 8 lần với giá trị 27; không có lệnh in x=29. Chưa kết luận thành thạo.

- Phần 1, mục 3.1–3.2: câu tự soạn về chương trình đang thực thi, vùng cấp phát động, vùng dữ liệu tạm lời gọi hàm, trạng thái chờ CPU và trạng thái chờ I/O/sự kiện; trả lời `process`, `heap`, `stack`, `ready`, `waiting` — đều đúng, đã chữa (W03 slide 5–6, 11).
- Phần 1: câu tự soạn điền `control` trong process control block, trạng thái `ready` sau I/O và `switch` trong context switch — đúng, đã chữa (W03 slide 12, 16, 27). Nhầm ready queue với PCB: [CS-C03-001](cau-sai/chuong-3.md).
- Mục 3.3: chưa nhớ program counter: [CS-C03-002](cau-sai/chuong-3.md).
- Mục 3.1: câu tự soạn về thực thể bị động, vùng mã, vùng dữ liệu, trình liên kết và trình nạp; trả lời `program`, `text`, `data`, `linker`, `loader` — đều đúng, đã chữa (W03 slide 5–8).
- Mục 3.1: câu tự soạn về vùng cấp phát động, dữ liệu tạm lời gọi hàm và biến toàn cục, trả lời `heap`, `stack`, `global` — đúng, đã chữa (W03 slide 6). Program counter đã đúng lại [CS-C03-002](cau-sai/chuong-3.md); return address cần ôn [CS-C03-003](cau-sai/chuong-3.md).
- Câu tự soạn: trạng thái `terminated` và `control` trong Process Control Block — đúng (W03 slide 11, 16); `return` và `ready` đã đúng lại: [CS-C03-003 và CS-C03-001](cau-sai/chuong-3.md).
- Mục 3.5: câu tự soạn về lời gọi tạo tiến trình con trong Unix/Linux, trả lời `fork()` — đúng, đã chữa (W03 slide 29, 32–33).
- Câu tự soạn 3.1–3.5: `child`, `ID` trong process ID, `exec` — đúng (W03 slide 9, 29, 32, 38); `device` đúng từ nhưng người dùng nói chưa nhớ [CS-C03-004](cau-sai/chuong-3.md); nhầm nhãn dispatch [CS-C03-005](cau-sai/chuong-3.md).
- Câu tự soạn 3.1–3.5: `linker`, `interrupt` (nhãn running → ready), `parent`, `0` (fork trả về trong con), `exit` — đều đúng; đã chữa (W03 slide 7, 12, 29, 33, 38).
- Mục 3.6: `memory` trong shared memory và `mailbox` — đúng (W03 slide 42, 47); message passing, indirect communication và bounded capacity cần ôn: [CS-C03-006 đến 008](cau-sai/chuong-3.md).
- Mục 3.6: câu tự soạn về nhận có chặn và zero capacity, trả lời `blocking`, `0` — đúng (W03 slide 47–48); message passing, indirect communication và bounded capacity đã đúng lại: [CS-C03-006 đến 008](cau-sai/chuong-3.md).
- Mục 3.6: `direct`, `nonblocking`, `unbounded`, `send` — đúng (W03 slide 47–48); `synchronization` đúng từ nhưng người dùng nói chưa nhớ: [CS-C03-009](cau-sai/chuong-3.md).
- Phần 2: `exec` và `thread` — đúng (W03 slide 32, 50); synchronization đã đúng lại [CS-C03-009](cau-sai/chuong-3.md); stack và kernel thread cần ôn [CS-C03-010 và 011](cau-sai/chuong-3.md).
- Mục 3.7: `control` trong Thread Control Block, `user` trong user thread — đúng (W03 slide 51, 53); stack và kernel thread đã đúng lại [CS-C03-010 và 011](cau-sai/chuong-3.md); multithreading đúng ý nhưng chưa đúng dạng từ [CS-C03-012](cau-sai/chuong-3.md).
- Mục 3.7: `program counter`, `code`, `registers`, `one` — đúng về thông tin riêng/chung và mô hình many-to-one (W03 slide 50–51, 57); multithreading đã đúng lại [CS-C03-012](cau-sai/chuong-3.md).
