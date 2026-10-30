# Phần 1 — Các loại định thời

Nguồn chính: **W04 slide 10–18**, liên hệ **W03 slide 25–27**. Chọn đúng bộ định thời theo việc nó quyết định, không theo độ dài CPU burst của công việc.

## Ba loại định thời

| Loại (English) | Quyết định gì? | Nguồn |
|---|---|---|
| Định thời dài (long-term scheduling) | Công việc/chương trình nào được chấp nhận vào hệ thống để thực thi; điều khiển mức độ đa chương, phối hợp CPU-bound và I/O-bound. | W04 slide 12 |
| Định thời vừa (medium-term scheduling) | Tiến trình nào được đưa ra khỏi hoặc đưa trở lại bộ nhớ chính trong quá trình thực thi. | W04 slide 14 |
| Định thời ngắn/CPU (short-term scheduling / CPU scheduling) | Tiến trình nào trong ready queue được sử dụng CPU kế tiếp; trong nhân đa luồng là chọn kernel thread. | W04 slide 16 |
| Bộ định thời công việc (job scheduler) | Tên khác của long-term scheduler. | W03 slide 25 |
| Bộ định thời CPU (CPU scheduler) | Tên khác của short-term scheduler. | W03 slide 25; W04 slide 16 |
| Mức độ đa chương (degree of multiprogramming) | Số tiến trình trong bộ nhớ để có thể luân phiên thực thi; chịu điều chỉnh bởi khâu nhận vào/swap. | W04 slide 12, 14; W03 slide 26 |
| Đưa vào (swap in) / đưa ra (swap out) | Đưa tiến trình từ đĩa vào bộ nhớ / từ bộ nhớ ra đĩa theo mô hình hoán đổi trong slide. | W04 slide 14; W03 slide 26 |

## Chọn tiến trình và chuyển quyền CPU

| Khái niệm (English) | Dấu hiệu nhận biết | Nguồn |
|---|---|---|
| Bộ định thời (scheduler) | Chọn công việc/tiến trình nào theo chính sách định thời. | W04 slide 12, 16 |
| Bộ điều phối (dispatcher) | Trao quyền CPU cho tiến trình đã được short-term scheduler chọn: đổi ngữ cảnh, chuyển về user mode, tiếp tục đúng vị trí chương trình. | W04 slide 18; W05 slide 15 và đối chiếu bổ sung bên dưới |
| Chuyển ngữ cảnh (context switch) | Lưu ngữ cảnh cũ, khôi phục ngữ cảnh mới. | W03 slide 27; W04 slide 18 |
| Độ trễ điều phối (dispatch latency) | Thời gian cần để dừng một tiến trình và khởi động tiến trình khác chạy. | W04 slide 18 |
| Ngắt đồng hồ (clock interrupt) | Một sự kiện có thể khiến bộ định thời ngắn được gọi. | W04 slide 17 |
| Ngắt I/O (I/O interrupt) | Ngắt từ I/O, cũng là một dịp có thể xét lại định thời. | W04 slide 17 |

W04 slide 18 dùng tên “bộ định thời” cho cả chuỗi chuyển quyền CPU. Để phân biệt thuật ngữ: **scheduler chọn, dispatcher trao CPU**. Tên dispatcher còn xuất hiện trong W05 slide 15. Đối chiếu ngoài chỉ để làm rõ hai vai trò: [Operating System Concepts Essentials — Ch5, trang PDF 7–8](https://www.os-book.com/OS8/os8e/slide-dir/PDF-dir/ch5.pdf#page=7).

## Dễ nhầm

- “Chấp nhận công việc vào hệ thống” → **long-term**. “Swap” → **medium-term**. “Chọn trong ready queue” → **short-term**.
- **Dispatcher** không phải một loại giải thuật như FCFS/SJF; nó thực hiện việc chuyển quyền sau khi đã chọn.
- **Dispatch latency** là phí thời gian chuyển quyền, không phải thời gian đợi của một tiến trình trong ready queue.
