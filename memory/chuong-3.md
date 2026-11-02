# Chương 3 — Kết quả và điểm cần ôn

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
