# Câu từng sai — Chương 3

## CS-C03-013 | 3.4 | cần ôn | 2026-11-04
- Nguồn: [Bài 3.4](../../output/chuong-3/3.4-dinh-thoi-tien-trinh.md), W03 slide 27 và ghi chú giới hạn trong bài soạn; câu tự soạn C03-TN-20261104-02 câu 3; nguyên văn phương án lấy từ bộ câu đã giao.
- Câu hỏi: "**Câu 3.** P gọi một lời gọi hệ thống. Hệ điều hành xử lý xong yêu cầu rồi tiếp tục thực thi chính P; không có tiến trình khác được chọn chạy trong khoảng này. Kết luận nào đúng?\n\nA. Đã có chuyển sang thực thi mã hệ điều hành, nhưng không có chuyển ngữ cảnh từ P sang tiến trình khác.\nB. Vì thực thi mã hệ điều hành nên chắc chắn đã có chuyển ngữ cảnh từ P sang tiến trình khác.\nC. Không thể có tình huống này vì lời gọi hệ thống luôn làm P chuyển sang waiting.\nD. Sau lời gọi hệ thống, P phải quay lại trạng thái new trước khi chạy tiếp."
- Trả lời sai đầu tiên (2026-11-04): Không biết, tôi đoán là C
- Đáp án: A — Chuyển sang thực thi mã hệ điều hành nhưng không chuyển ngữ cảnh từ P sang tiến trình khác.
- Lỗi: Chọn C khi chưa biết và đoán; chưa phân biệt lời gọi hệ thống với việc bắt buộc chờ I/O/đổi tiến trình. Đã chọn đúng nhưng còn phân vân ở bộ trước, nay kiểm tra tình huống chưa đúng.

## CS-C03-014 | 3.5.2 | cần ôn | 2026-11-04
- Nguồn: [Bài 3.5.2](../../output/chuong-3/3.5.2-vi-du-tao-tien-trinh.md), W03 slide 32–33 và ghi chú API đã đối chiếu trong bài soạn; câu tự soạn C03-TN-20261104-02 câu 6; nguyên văn phương án lấy từ bộ câu đã giao.
- Câu hỏi: "**Câu 6.** Xét đoạn mã trong `main`. Ban đầu chỉ có một tiến trình; `fork()`, `execlp()` và `wait(NULL)` đều thành công. Chương trình `worker` cuối cùng kết thúc bình thường. Nhận định nào đúng về hai lệnh `printf` trong đoạn mã này?\n\n```c\npid_t pid = fork();\nif (pid == 0) {\n    execlp(\"/bin/worker\", \"worker\", NULL);\n    printf(\"X\\n\");\n} else {\n    wait(NULL);\n    printf(\"Y\\n\");\n}\n```\n\nA. Tiến trình con thực thi `printf(\"X\\n\")` sau khi `worker` kết thúc, rồi cha thực thi `printf(\"Y\\n\")`.\nB. Cha thực thi `printf(\"X\\n\")`, còn con thực thi `printf(\"Y\\n\")`.\nC. Cha thực thi `printf(\"Y\\n\")` trước khi con kết thúc vì đối số NULL làm `wait` không chờ.\nD. Lệnh in X không được thực thi; cha thực thi lệnh in Y sau khi con kết thúc."
- Trả lời sai đầu tiên (2026-11-04): C
- Đáp án: D — Lệnh in X không thực thi vì exec thành công thay chương trình và không trở lại mã cũ; cha in Y sau khi con kết thúc. NULL chỉ bỏ việc lưu trạng thái kết thúc, không bỏ chờ.
- Lỗi: Chọn phương án cho rằng NULL làm wait không chờ; chưa đủ bằng chứng riêng để kết luận người dùng hiểu/sai phần exec. Đã chữa cả exec và wait.

## CS-C03-015 | 3.7 | cần ôn | 2026-11-04
- Nguồn: [Bài 3.7](../../output/chuong-3/3.7-tieu-trinh.md), W03 slide 59, vận dụng với giả thiết cố định trong câu hỏi; câu tự soạn C03-TN-20261104-02 câu 9; nguyên văn phương án lấy từ bộ câu đã giao.
- Câu hỏi: "**Câu 9.** Theo mô hình Many-to-Many, một tiến trình có 12 user thread được ghép lên 4 kernel thread. Máy có 8 lõi CPU. Giả sử cả 4 kernel thread đều sẵn sàng, không có hạn chế khác và mỗi kernel thread chỉ thực thi một user thread tại một thời điểm. Tối đa bao nhiêu user thread của tiến trình có thể thực sự chạy cùng lúc?\n\nA. 1.\nB. 4.\nC. 8.\nD. 12."
- Trả lời sai đầu tiên (2026-11-04): C
- Đáp án: B — 4; số user thread chạy cùng lúc tối đa min(12 user thread, 4 kernel thread, 8 lõi) = 4 theo giả thiết.
- Lỗi: Chọn 8, mới xét số lõi mà chưa xét giới hạn 4 kernel thread được dùng để thực thi các user thread của tiến trình.

## CS-C03-001 | 3.4 | đã đúng lại | 2026-10-31
- Nguồn: [3.4 Định thời tiến trình](../../output/chuong-3/3.4-dinh-thoi-tien-trinh.md), W03 slide 22–23; câu tự soạn.
- Câu hỏi: Trong _____ queue, các tiến trình sẵn sàng chờ CPU.
- Trả lời sai đầu tiên (2026-10-31): PCB
- Đáp án: ready.
- Lỗi: Nhầm tên hàng đợi sẵn sàng với khối điều khiển tiến trình.
CS-C03-001 | 2026-10-31 | trả lời khi kiểm tra lại: ready | đúng.

## CS-C03-002 | 3.3 | đã đúng lại | 2026-11-04
- Nguồn: [3.3 Process Control Block](../../output/chuong-3/3.3-process-control-block.md), W03 slide 16; câu tự soạn.
- Câu hỏi: Trong program _____, từ nào hoàn thành tên bộ phận giữ địa chỉ lệnh sẽ thực thi tiếp theo?
- Trả lời sai đầu tiên (2026-10-31): không biết
- Đáp án: counter.
- Lỗi: Chưa nhớ thuật ngữ program counter.
CS-C03-002 | 2026-10-31 | trả lời khi kiểm tra lại: counter | đúng.
CS-C03-002 | 2026-11-04 | trả lời khi kiểm tra lại: counter | đúng; C03-TS-20261104-01 câu 8.

## CS-C03-003 | 3.1 | đã đúng lại | 2026-10-31
- Nguồn: [3.1 Khái niệm cơ bản](../../output/chuong-3/3.1-khai-niem-co-ban.md), W03 slide 6; câu tự soạn.
- Câu hỏi: Trong _____ address, từ nào hoàn thành tên địa chỉ cho biết nơi tiếp tục thực thi sau khi hàm được gọi kết thúc?
- Trả lời sai đầu tiên (2026-10-31): không biết
- Đáp án: return.
- Lỗi: Chưa nhớ thuật ngữ return address.
CS-C03-003 | 2026-10-31 | trả lời khi kiểm tra lại: return | đúng.

## CS-C03-004 | 3.4 | cần ôn | 2026-11-04
- Nguồn: [3.4 Định thời tiến trình](../../output/chuong-3/3.4-dinh-thoi-tien-trinh.md), W03 slide 22–23; câu tự soạn.
- Câu hỏi: _____ queue chứa các tiến trình đang chờ một thiết bị I/O.
- Trả lời sai đầu tiên (2026-10-31): device (coi như chưa nhớ)
- Đáp án: device.
- Lỗi: Trả lời đúng từ nhưng người dùng yêu cầu xem là chưa nhớ; cần kiểm tra lại độc lập.

CS-C03-004 | 2026-11-04 | trả lời khi kiểm tra lại: không biết | sai; chưa nhớ thuật ngữ; C03-TS-20261104-01 câu 9.
CS-C03-004 | 2026-11-04 | trả lời khi kiểm tra lại: B | đúng tình huống waiting → ready/ready queue sau khi hoàn tất I/O (C03-TN-20261104-01 câu 2); chưa kiểm tra lại khả năng tự nhớ từ device nên giữ trạng thái cần ôn thuật ngữ.

## CS-C03-005 | 3.2 | đã đúng lại | 2026-11-04
- Nguồn: [3.2 Trạng thái tiến trình](../../output/chuong-3/3.2-trang-thai-tien-trinh.md), W03 slide 12; câu tự soạn.
- Câu hỏi: Trong sơ đồ trạng thái, thao tác chuyển tiến trình từ ready sang running có nhãn gì?
- Trả lời sai đầu tiên (2026-10-31): admited
- Đáp án: dispatch.
- Lỗi: Nhầm chuyển ready → running với admit (new → ready); từ trả lời cũng sai chính tả nếu định viết admitted.

CS-C03-005 | 2026-11-04 | trả lời khi kiểm tra lại: dispatch | đúng; C03-TS-20261104-01 câu 10.

## CS-C03-006 | 3.6 | đã đúng lại | 2026-10-31
- Nguồn: [3.6 Giao tiếp liên tiến trình](../../output/chuong-3/3.6-giao-tiep-lien-tien-trinh.md), W03 slide 42, 47; câu tự soạn.
- Câu hỏi: Message _____ là mô hình trao đổi dữ liệu bằng thao tác gửi và nhận thông điệp.
- Trả lời sai đầu tiên (2026-10-31): communication
- Đáp án: passing.
- Lỗi: Chưa nhớ tên mô hình message passing; message communication không phải tên được dùng trong nguồn.
CS-C03-006 | 2026-10-31 | trả lời khi kiểm tra lại: passing | đúng.

## CS-C03-007 | 3.6 | đã đúng lại | 2026-10-31
- Nguồn: [3.6 Giao tiếp liên tiến trình](../../output/chuong-3/3.6-giao-tiep-lien-tien-trinh.md), W03 slide 47; câu tự soạn.
- Câu hỏi: Trong _____ communication, các tiến trình gửi và nhận thông điệp qua hộp thư hoặc cổng trung gian.
- Trả lời sai đầu tiên (2026-10-31): interprocess
- Đáp án: indirect.
- Lỗi: Nêu phạm vi liên tiến trình thay vì cách giao tiếp gián tiếp qua trung gian.
CS-C03-007 | 2026-10-31 | trả lời khi kiểm tra lại: indirect | đúng.

## CS-C03-008 | 3.6 | đã đúng lại | 2026-10-31
- Nguồn: [3.6 Giao tiếp liên tiến trình](../../output/chuong-3/3.6-giao-tiep-lien-tien-trinh.md), W03 slide 48; câu tự soạn.
- Câu hỏi: Hàng đợi thông điệp có giới hạn sức chứa được gọi là _____ capacity.
- Trả lời sai đầu tiên (2026-10-31): message
- Đáp án: bounded.
- Lỗi: Chưa nhớ từ chỉ sức chứa hữu hạn.
CS-C03-008 | 2026-10-31 | trả lời khi kiểm tra lại: bounded | đúng.

## CS-C03-009 | 3.6 | đã đúng lại | 2026-10-31
- Nguồn: [3.6 Giao tiếp liên tiến trình](../../output/chuong-3/3.6-giao-tiep-lien-tien-trinh.md), W03 slide 40, 42, 45, 47; câu tự soạn.
- Câu hỏi: Thuật ngữ nào chỉ việc phối hợp thứ tự hoặc điều kiện thực thi, truy cập dữ liệu giữa các tiến trình?
- Trả lời sai đầu tiên (2026-10-31): synchronization (coi như chưa nhớ)
- Đáp án: synchronization.
- Lỗi: Trả lời đúng từ nhưng người dùng yêu cầu xem là chưa nhớ; cần kiểm tra lại độc lập.
CS-C03-009 | 2026-10-31 | trả lời khi kiểm tra lại: synchronization | đúng.

## CS-C03-010 | 3.7 | đã đúng lại | 2026-10-31
- Nguồn: [3.7 Tiểu trình](../../output/chuong-3/3.7-tieu-trinh.md), W03 slide 50–51; câu tự soạn.
- Câu hỏi: Mỗi tiểu trình có một vùng ngăn xếp riêng gọi là gì?
- Trả lời sai đầu tiên (2026-10-31): TCB
- Đáp án: stack.
- Lỗi: Nhầm ngăn xếp riêng với khối điều khiển tiểu trình.
CS-C03-010 | 2026-10-31 | trả lời khi kiểm tra lại: stack | đúng.

## CS-C03-011 | 3.7 | đã đúng lại | 2026-10-31
- Nguồn: [3.7 Tiểu trình](../../output/chuong-3/3.7-tieu-trinh.md), W03 slide 54; câu tự soạn.
- Câu hỏi: _____ thread được hệ điều hành hỗ trợ và quản lý ở mức nhân.
- Trả lời sai đầu tiên (2026-10-31): multi
- Đáp án: kernel.
- Lỗi: Chưa nhớ thuật ngữ kernel thread.
CS-C03-011 | 2026-10-31 | trả lời khi kiểm tra lại: kernel | đúng.

## CS-C03-012 | 3.7 | đã đúng lại | 2026-10-31
- Nguồn: [3.7 Tiểu trình](../../output/chuong-3/3.7-tieu-trinh.md), W03 slide 50–52; câu tự soạn.
- Câu hỏi: Thuật ngữ nào chỉ việc một tiến trình có nhiều tiểu trình?
- Trả lời sai đầu tiên (2026-10-31): multithread
- Đáp án: multithreading.
- Lỗi: Nhận diện đúng ý đa luồng nhưng thiếu dạng danh từ tên khái niệm.
CS-C03-012 | 2026-10-31 | trả lời khi kiểm tra lại: multithreading | đúng.
