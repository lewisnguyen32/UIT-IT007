# Chương 4 — Kết quả và điểm cần ôn

- BT-C04-002, mở rộng tự áp dụng HRRN theo yêu cầu (01/11/2026), không phải ý có sẵn trong ảnh đề: đã giải mẫu theo chế độ không trưng dụng, ratio=(waiting+burst)/burst (W05 slide 4). Gantt P3 0–10 → P2 10–14 → P1 14–19 → P4 19–31 → P5 31–42; trung bình waiting=response=9,2, turnaround=17,6. Đã kiểm bằng mô phỏng, chưa có câu trả lời tự giải; không ghi nhận thành thạo.

- 01/11/2026: người dùng tự tổng kết đúng tiêu chí chọn của SJF, RR, HRRN, FCFS; đã bổ sung điều kiện đã đến/sẵn sàng và phân biệt SJF với SRTF. Quy ước số priority cần ôn: [CS-C04-003](cau-sai/chuong-4.md). Chưa kết luận thành thạo.

- BT-C04-002 (01/11/2026), ảnh Câu 2 (2.5đ) người dùng gửi; dữ kiện (arrival, burst): P1 (8,5), P2 (3,4), P3 (0,10), P4 (6,12), P5 (11,11). Đã giải mẫu SRTF và RR q=7, chưa có câu trả lời tự giải. SRTF: P3 0–3 → P2 3–7 → P3 7–8 → P1 8–13 → P3 13–19 → P5 19–30 → P4 30–42; trung bình waiting 8,2, response 6,4, turnaround 16,6. RR: P3 0–7 → P2 7–11 → P4 11–18 → P3 18–21 → P1 21–26 → P5 26–33 → P4 33–38 → P5 38–42; trung bình waiting 13,6, response 7,4, turnaround 22. Đã kiểm bằng mô phỏng; dùng turnaround = kết thúc − đến theo W04 slide 20–21; nguyên tắc SRTF W04 slide 40, RR W04 slide 54. Chưa kết luận thành thạo.

Mốc hiện tại ở [memory.md](../memory.md); bài soạn ở [mục lục Ch4](../output/chuong-4/README.md). Chưa theo dõi %.

- SRTF: người dùng yêu cầu phương pháp trình bày bài từ ảnh; đã hướng dẫn mẫu bằng giản đồ Gantt và bảng tính thời gian, chưa ghi nhận người dùng tự giải. Dữ kiện (arrival, burst): P1 (3,4), P2 (12,6), P3 (9,3), P4 (0,11), P5 (5,6). Đối chiếu kết quả: Gantt P4 0–3 → P1 3–7 → P5 7–9 → P3 9–12 → P5 12–16 → P2 16–22 → P4 22–30; trung bình waiting 5,6, response 1,2, turnaround 11,6. Nguồn bài: ảnh người dùng gửi; nguồn lý thuyết: W04 slide 20–21, 40. Mã bài: BT-C04-001.

## C04-TS-001

10 câu tự soạn Ch4 phần 1–2 theo yêu cầu người dùng, trừ phần 3. Giao, được trả lời và chữa ngày 31/10/2026. Trả lời mỗi câu bằng một từ tiếng Anh (chấp nhận viết tắt chuẩn của tên giải thuật) hoặc một số. Đã rà độc lập phạm vi, nguồn và độ rõ của câu hỏi.

1. Bộ phận nào trao quyền CPU cho tiến trình đã được bộ định thời ngắn chọn? (W04 slide 18; W05 slide 15.)
2. Tiêu chuẩn nào đo số tiến trình hoàn tất trong một đơn vị thời gian? (W04 slide 22.)
3. Tiến trình P đến lúc 2 ms, chạy lần đầu lúc 5 ms và kết thúc lúc 12 ms. Thời gian đáp ứng của P là bao nhiêu ms? (W04 slide 20–21.)
4. Giải thuật nào phục vụ tiến trình theo thứ tự vào ready queue, đến trước được phục vụ trước? (W04 slide 29.)
5. Khi CPU rảnh, giải thuật nào chọn tiến trình sẵn sàng có CPU burst kế tiếp ngắn nhất và không cho tiến trình mới đến đoạt CPU? (W04 slide 35–36.)
6. Giải thuật nào chọn tiến trình có thời gian CPU còn lại ngắn nhất trong các tiến trình đã đến và còn chạy được, kể cả tiến trình đang chạy; có thể lấy lại CPU khi tiến trình mới đến có burst ngắn hơn phần còn lại của tiến trình hiện tại? (W04 slide 40.)
7. Cơ chế tăng dần độ ưu tiên cho tiến trình chờ lâu để tránh bị trì hoãn vô hạn gọi là gì? (W04 slide 51.)
8. Giải thuật nào cấp CPU luân phiên tối đa một quantum mỗi lượt; hết quantum mà vẫn còn cần CPU thì tiến trình được đưa về cuối ready queue? (W04 slide 54.)
9. Theo HRRN, một tiến trình đã chờ 6 ms và có thời gian phục vụ dự kiến 3 ms. Tỉ số đáp ứng của tiến trình là bao nhiêu? (W05 slide 4.)
10. Giải thuật nhiều hàng đợi nào cho phép tiến trình chuyển hàng dựa trên hành vi thực thi hoặc thời gian chờ? (W05 slide 9, 11–13.)

Nguồn tự soạn: các bài tương ứng trong [Ch4](../output/chuong-4/README.md). Các mã slide ở từng câu tính từ 1. Không phải câu lấy nguyên văn từ đề thi hoặc câu ôn trong slide.

Kết quả ngày 31/10/2026: 8/10 câu đúng hoàn toàn; câu 4 đúng giải thuật nhưng cần sửa tên chuẩn, câu 10 trả lời chưa biết. Không suy ra thành thạo hoặc hoàn tất mục.
- Các câu đúng, giữ nguyên câu trả lời: 1. `dispatcher`; 2. `throughput`; 3. `3`; 5. `SJF`; 6. `SRTF`; 7. `aging`; 8. `RR`; 9. `3`. Đã chữa câu 3 bằng 5 − 2 = 3 ms; câu 9 bằng (6 + 3)/3 = 3.
- Câu 4: [CS-C04-001](cau-sai/chuong-4.md#cs-c04-001--phần-1--cần-ôn--2026-10-31).
- Câu 10: [CS-C04-002](cau-sai/chuong-4.md#cs-c04-002--phần-2--cần-ôn--2026-10-31).

- MLQ/MLFQ (31/10/2026): đã giảng cách chọn giữa các hàng và trong mỗi hàng, gán hàng cố định của MLQ, chuyển hàng theo phản hồi/aging của MLFQ; minh họa một tiến trình CPU burst 30 ms qua Q0 RR 8 ms, Q1 RR 16 ms, Q2 FCFS với quy tắc xuống hàng khi dùng hết quantum. Nguồn: W05 slide 6–9, 11–13; quy tắc cụ thể của ví dụ được nêu rõ khi giảng. Chưa có câu trả lời tự kiểm sau bài này; CS-C04-002 giữ trạng thái cần ôn.
