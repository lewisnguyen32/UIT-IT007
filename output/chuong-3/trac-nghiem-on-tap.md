# Trắc nghiệm tự soạn — Chương 3

## C03-TN-20261104-02 — 10 câu tiếp theo

Câu tự soạn, mỗi câu chọn một đáp án đúng nhất trong A–D. Chưa kèm đáp án. Câu 3–4 kiểm tra lại hai ý người dùng còn phân vân ở bộ trước bằng tình huống khác.

**Câu 1.** Trên máy chỉ có một lõi CPU, hai tiến trình P và Q được thực thi luân phiên; cả hai đều tiến triển trong cùng một khoảng thời gian. Nhận định nào đúng?

A. P và Q không có tính đồng thời vì máy chỉ có một lõi.
B. P và Q có tính đồng thời (concurrency), nhưng không thực thi song song tại cùng một thời điểm.
C. P và Q có tính song song (parallelism) vì cả hai đều chưa kết thúc.
D. Chỉ một trong hai là tiến trình; tiến trình còn lại là chương trình bị động.

**Câu 2.** Ban đầu P đang chờ I/O. Sau đó lần lượt xảy ra: I/O hoàn tất; P được cấp CPU; P bị thu hồi CPU để tiến trình khác chạy dù P chưa yêu cầu I/O hay kết thúc. Chuỗi trạng thái nào phù hợp?

A. waiting → running → ready → waiting.
B. waiting → ready → waiting → running.
C. waiting → new → running → terminated.
D. waiting → ready → running → ready.

**Câu 3.** P gọi một lời gọi hệ thống. Hệ điều hành xử lý xong yêu cầu rồi tiếp tục thực thi chính P; không có tiến trình khác được chọn chạy trong khoảng này. Kết luận nào đúng?

A. Đã có chuyển sang thực thi mã hệ điều hành, nhưng không có chuyển ngữ cảnh từ P sang tiến trình khác.
B. Vì thực thi mã hệ điều hành nên chắc chắn đã có chuyển ngữ cảnh từ P sang tiến trình khác.
C. Không thể có tình huống này vì lời gọi hệ thống luôn làm P chuyển sang waiting.
D. Sau lời gọi hệ thống, P phải quay lại trạng thái new trước khi chạy tiếp.

**Câu 4.** T1 và T2 thuộc cùng một tiến trình, dùng chung vùng mã nhưng đang dừng ở hai vị trí lệnh khác nhau. Khi chuyển từ T1 sang T2, nhóm thông tin riêng nào của T2 cần được khôi phục để tiếp tục đúng vị trí và đúng lời gọi hàm?

A. Chỉ vùng mã dùng chung; không cần khôi phục thông tin riêng của T2.
B. Chỉ vùng dữ liệu toàn cục; PC của T1 vẫn dùng được cho T2.
C. Program counter và các thanh ghi của T2, bao gồm con trỏ stack.
D. Chỉ PID của tiến trình vì các thread cùng tiến trình có cùng vị trí thực thi.

**Câu 5.** Khi chọn công việc được nhận vào hệ thống, bộ định thời dài cần xem xét sự kết hợp tiến trình hướng CPU và hướng I/O. Phát biểu nào mô tả đúng hai loại tiến trình này?

A. CPU-bound thường có CPU burst ngắn và chờ I/O nhiều; I/O-bound thường có CPU burst dài.
B. CPU-bound thường có CPU burst dài; I/O-bound thường xen kẽ CPU burst ngắn với nhiều thời gian chờ I/O.
C. CPU-bound chỉ được nhận bởi short-term scheduler; I/O-bound chỉ được nhận bởi medium-term scheduler.
D. CPU-bound không thể phát sinh I/O; I/O-bound không cần CPU để thực thi.

**Câu 6.** Xét đoạn mã trong `main`. Ban đầu chỉ có một tiến trình; `fork()`, `execlp()` và `wait(NULL)` đều thành công. Chương trình `worker` cuối cùng kết thúc bình thường. Nhận định nào đúng về hai lệnh `printf` trong đoạn mã này?

```c
pid_t pid = fork();
if (pid == 0) {
    execlp("/bin/worker", "worker", NULL);
    printf("X\n");
} else {
    wait(NULL);
    printf("Y\n");
}
```

A. Tiến trình con thực thi `printf("X\n")` sau khi `worker` kết thúc, rồi cha thực thi `printf("Y\n")`.
B. Cha thực thi `printf("X\n")`, còn con thực thi `printf("Y\n")`.
C. Cha thực thi `printf("Y\n")` trước khi con kết thúc vì đối số NULL làm `wait` không chờ.
D. Lệnh in X không được thực thi; cha thực thi lệnh in Y sau khi con kết thúc.

**Câu 7.** Sau `pid = fork()` thành công, một tiến trình kiểm tra thấy `pid == 0`. Phát biểu nào đúng?

A. Đó là tiến trình con; 0 là giá trị trả về của `fork`, không phải PID thật của tiến trình con.
B. Đó là tiến trình cha; 0 cho biết tiến trình con đã kết thúc.
C. Đó là tiến trình con và PID thật của nó bắt buộc bằng 0.
D. Không có tiến trình con nào được tạo vì `fork` trả về 0 khi thất bại.

**Câu 8.** P gửi bằng `send(Q, msg)`, trong đó Q là tên tiến trình nhận. Ở Q, nếu chưa có thông điệp phù hợp thì thao tác nhận trả về ngay. Hàng đợi thông điệp được mô hình hóa là không giới hạn sức chứa. Tổ hợp nào đúng?

A. Indirect communication — blocking receive — bounded capacity.
B. Direct communication — blocking receive — unbounded capacity.
C. Direct communication — nonblocking receive — unbounded capacity.
D. Indirect communication — nonblocking receive — zero capacity.

**Câu 9.** Theo mô hình Many-to-Many, một tiến trình có 12 user thread được ghép lên 4 kernel thread. Máy có 8 lõi CPU. Giả sử cả 4 kernel thread đều sẵn sàng, không có hạn chế khác và mỗi kernel thread chỉ thực thi một user thread tại một thời điểm. Tối đa bao nhiêu user thread của tiến trình có thể thực sự chạy cùng lúc?

A. 1.
B. 4.
C. 8.
D. 12.

**Câu 10.** Chọn phát biểu **SAI** về lợi ích và điều kiện sử dụng đa tiểu trình.

A. Các tiểu trình cùng tiến trình có thể chia sẻ code, data và tài nguyên như tập tin.
B. Tạo và chuyển ngữ cảnh tiểu trình thường ít tốn chi phí hơn tạo và chuyển ngữ cảnh tiến trình.
C. Khả năng chạy song song phụ thuộc cả phần cứng và mô hình ánh xạ user thread lên kernel thread.
D. Đa tiểu trình bảo đảm các tiểu trình còn lại luôn tiếp tục chạy khi một tiểu trình bị chặn, bất kể mô hình ánh xạ.

### Nguồn đối chiếu bộ C03-TN-20261104-02

W03 slide tính từ 1: câu 1: 31, 52, 57–58; câu 2: 11–12; câu 3: 27 và ghi chú giới hạn trong bài 3.4; câu 4: 50–51; câu 5: 25; câu 6: 32–33 và giới hạn API đã đối chiếu trong bài 3.5.2; câu 7: 33 và ghi chú giá trị trả về trong bài 3.5.2; câu 8: 47–48; câu 9: vận dụng mô hình slide 59 với giả thiết trong đề; câu 10: 50, 52, 57–59.

## C03-TN-20261104-01 — 10 câu

Mô phỏng cách trình bày trắc nghiệm của đề giữa kỳ: bốn phương án A–D, chọn một đáp án đúng nhất; có câu chọn phát biểu sai, nhận diện tình huống và đọc mã. Đây là câu tự soạn từ lý thuyết W03, không phải câu đề thật. Không gán nhãn chuẩn đầu ra G1/G2 khi chưa xác nhận quy tắc gán nhãn. Chưa kèm đáp án.

**Câu 1.** Trong một hàm C, biến con trỏ cục bộ `p` nhận địa chỉ do `malloc` trả về. Theo mô hình bộ nhớ trong bài, cách xác định vị trí lưu trữ nào sau đây đúng?

A. Bản thân `p` và vùng được cấp phát đều nằm trong stack.
B. Bản thân `p` và vùng được cấp phát đều nằm trong heap.
C. Bản thân `p` nằm trong stack, vùng được cấp phát nằm trong heap.
D. Bản thân `p` nằm trong data section, vùng được cấp phát nằm trong text section.

**Câu 2.** Tiến trình P đang bị chặn để chờ một thiết bị I/O. Khi I/O hoàn tất, CPU vẫn đang chạy tiến trình Q. Theo sơ đồ trạng thái và hàng đợi trong bài, điều gì xảy ra với P?

A. P chuyển từ waiting sang running và thay Q ngay lập tức.
B. P chuyển từ waiting sang ready và được đưa vào ready queue.
C. P tiếp tục nằm trong device queue cho đến khi Q kết thúc.
D. P chuyển từ waiting sang new để được chấp nhận lại vào hệ thống.

**Câu 3.** Chọn phát biểu **SAI** về PCB và chuyển ngữ cảnh (context switch).

A. PCB có thể lưu trạng thái tiến trình, program counter và các thanh ghi CPU.
B. Khi đổi từ tiến trình P sang Q, hệ điều hành lưu ngữ cảnh P và khôi phục ngữ cảnh Q.
C. PID là số định danh tiến trình, còn PCB là cấu trúc lưu thông tin quản lý tiến trình.
D. Mỗi lần xảy ra ngắt hoặc lời gọi hệ thống, CPU bắt buộc phải chuyển sang một tiến trình khác.

**Câu 4.** Cách ghép bộ định thời với chức năng nào sau đây đúng?

A. Long-term: nhận công việc vào hệ thống; short-term: chọn tiến trình chạy CPU tiếp theo; medium-term: đưa tiến trình ra khỏi hoặc trở lại bộ nhớ.
B. Long-term: chọn tiến trình chạy CPU tiếp theo; short-term: nhận công việc vào hệ thống; medium-term: đưa tiến trình ra khỏi hoặc trở lại bộ nhớ.
C. Long-term: nhận công việc vào hệ thống; short-term: đưa tiến trình ra khỏi hoặc trở lại bộ nhớ; medium-term: chọn tiến trình chạy CPU tiếp theo.
D. Long-term: đưa tiến trình ra khỏi hoặc trở lại bộ nhớ; short-term: chọn tiến trình chạy CPU tiếp theo; medium-term: nhận công việc vào hệ thống.

**Câu 5.** Chọn phát biểu **SAI** về các tác vụ đối với tiến trình trong Unix/Linux.

A. Sau `fork()` thành công, cha và con tiếp tục từ sau lời gọi với giá trị trả về khác nhau.
B. `wait(NULL)` có thể trả về ngay nếu đã có một tiến trình con kết thúc đang chờ được thu nhận.
C. `exec` thành công tạo thêm một tiến trình mới, trong khi tiến trình gọi tiếp tục chạy chương trình cũ.
D. `exit()` kết thúc tiến trình gọi; hệ điều hành thu hồi các tài nguyên của tiến trình theo cơ chế kết thúc.

**Câu 6.** Xét đoạn mã bên dưới trong hàm `main`. Ban đầu chỉ có một tiến trình; mọi `fork()` đều thành công, không có tiến trình nào kết thúc trước lệnh `printf`. Xét các giá trị được truyền cho `printf`, không xét thứ tự xuất hiện. Phương án nào đúng?

```c
int x = 1;
pid_t pid = fork();
if (pid == 0) {
    x += 2;
    fork();
} else {
    x += 4;
}
printf("%d\n", x);
```

A. Có 2 lần gọi `printf`: một lần với 3, một lần với 5.
B. Có 3 lần gọi `printf`: hai lần với 3, một lần với 5.
C. Có 3 lần gọi `printf`: một lần với 3, hai lần với 5.
D. Có 4 lần gọi `printf`: hai lần với 3, hai lần với 5.

**Câu 7.** Phát biểu nào đúng về hai mô hình giao tiếp liên tiến trình?

A. Shared memory yêu cầu mỗi lần trao đổi dữ liệu đều phải dùng thao tác gửi/nhận thông điệp của message passing.
B. Khi các tiến trình dùng shared memory, mọi truy cập đồng thời đã tự động được đồng bộ đúng.
C. Shared memory có nghĩa hệ điều hành không tham gia thiết lập hoặc quản lý vùng nhớ dùng chung.
D. Shared memory trao đổi qua vùng nhớ chung và cần đồng bộ truy cập; message passing trao đổi qua thao tác gửi/nhận thông điệp.

**Câu 8.** Hai tiến trình trao đổi thông điệp qua một mailbox. Hàng đợi của mailbox chỉ giữ được tối đa N thông điệp, với N là số nguyên dương hữu hạn. Khi chưa có thông điệp phù hợp, thao tác nhận phải chờ. Tổ hợp phân loại nào đúng?

A. Indirect communication — blocking receive — bounded capacity.
B. Direct communication — blocking receive — bounded capacity.
C. Indirect communication — nonblocking receive — bounded capacity.
D. Indirect communication — blocking receive — unbounded capacity.

**Câu 9.** Hai tiểu trình T1 và T2 thuộc cùng một tiến trình. Theo mô hình trong bài, cách phân chia thông tin nào đúng?

A. Chung program counter và registers; riêng code, data và stack.
B. Chung stack và code; riêng program counter, registers và data.
C. Chung code, data và các tài nguyên như tập tin; riêng program counter, registers và stack.
D. Chung code, data, program counter và stack; riêng registers và các tập tin đang mở.

**Câu 10.** Một tiến trình có nhiều user thread được ánh xạ lên đúng một kernel thread theo mô hình Many-to-One. Máy có nhiều lõi CPU. Nếu kernel thread duy nhất bị chặn bởi một lời gọi hệ thống, nhận định nào đúng?

A. Các user thread khác vẫn chạy song song trên các lõi còn lại vì máy có nhiều lõi.
B. Cả nhóm user thread không thể tiếp tục thực thi khi kernel thread đó bị chặn; mô hình này cũng không cho các user thread của nhóm chạy song song trên nhiều lõi.
C. Hệ điều hành tự động chuyển mô hình thành One-to-One để mỗi user thread có một kernel thread riêng.
D. Chỉ user thread gọi lời gọi hệ thống bị chặn; các user thread khác tiếp tục chạy trên chính kernel thread đang bị chặn.

### Nguồn đối chiếu

Nguồn chính: W03, số slide tính từ 1. Câu 1: slide 6, 8; câu 2: slide 11–12, 22–23; câu 3: slide 16, 27 và ghi chú giới hạn trong bài soạn; câu 4: slide 25–26; câu 5: slide 32–33, 38, với các giới hạn API đã được đối chiếu trong bài soạn; câu 6: vận dụng slide 32–33; câu 7: slide 42, 45, 47; câu 8: slide 47–48; câu 9: slide 50–51; câu 10: slide 57.

Mẫu trình bày tham khảo: ảnh cache trang 1 đề giữa kỳ 1 (2023–2024), `tmp/study_audit/exam-page-1.png`; chỉ dùng khuôn A–D và cách hỏi, không dùng dấu chọn trên ảnh làm đáp án chuẩn.
