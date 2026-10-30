# Chương 4 — Định thời CPU

Nguồn: **W04** (`#Week04-Chapter4-1 2024.pptx`, 74 slide) và **W05** (`#Week05-Chapter4-2 2024.pptx`, 59 slide) trong `Lý thuyết/`. Đã soạn terms và lý thuyết ngắn theo kiểu Ch1–2 trong phạm vi cơ sở. Các “Phần” theo ảnh LMS không trùng ranh giới tệp Week04/Week05.

Mỗi bài có nghĩa tiếng Việt kèm tên tiếng Anh, dấu hiệu nhận diện, cặp dễ nhầm và nguồn slide tính từ 1. Giữ tên chuẩn nhiều từ/viết tắt, không tự rút thành một từ. Đây là bản ôn, chưa phải bộ bài tính hay đáp án chính thức. Soạn xong không đồng nghĩa đã giảng/tự kiểm/thành thạo.

## Phần 1

| Chủ đề theo ảnh | Nguồn |
|---|---|
| [Các khái niệm cơ bản về định thời](phan-1-khai-niem-co-ban.md) | W04 slide 5–8 |
| [Các loại định thời](phan-1-cac-loai-dinh-thoi.md) | W04 slide 10–18 |
| [Các tiêu chuẩn định thời CPU](phan-1-tieu-chuan-dinh-thoi.md) | W04 slide 20–22 |
| [Khung giải thuật/chế độ quyết định — trong bài khái niệm](phan-1-khai-niem-co-ban.md) | W04 slide 24–27, bổ trợ từ slide |
| [First-Come, First-Served (FCFS)](phan-1-fcfs.md) | W04 slide 29–33 |
| [Shortest-Job-First (SJF)](phan-1-sjf.md) | W04 slide 35–39; liên hệ nhận xét 44–47 |
| [Shortest-Remaining-Time-First (SRTF)](phan-1-srtf.md) | W04 slide 40–47, cùng phần SJF trưng dụng/ước lượng |
| [Priority Scheduling](phan-1-priority.md) | W04 slide 49–52 |

## Phần 2

| Chủ đề theo ảnh | Nguồn |
|---|---|
| [Round Robin (RR)](phan-2-round-robin.md) | W04 slide 54–63 |
| [Highest Response Ratio Next (HRRN)](phan-2-hrrn.md) | W05 slide 4 |
| [Multilevel Queue](phan-2-multilevel-queue.md) | W05 slide 6–9 |
| [Multilevel Feedback Queue](phan-2-multilevel-feedback-queue.md) | W05 slide 11–13 |
| [So sánh giải thuật — trong bài MLFQ](phan-2-multilevel-feedback-queue.md) | W05 slide 15, bổ trợ từ slide |

## Phần 3

| Chủ đề theo ảnh | Nguồn | Phạm vi tạm |
|---|---|---|
| [Định thời tiểu trình](phan-3-dinh-thoi-tieu-trinh.md) | W05 slide 17 | Đã soạn |
| [Định thời đa bộ xử lý, cân bằng tải, processor affinity](phan-3-dinh-thoi-da-bo-xu-ly.md) | W05 slide 19–28 | Đã soạn, hết slide 28 |
| Định thời theo thời gian thực | W05 slide 29–37 | Đọc thêm, chưa đưa vào lộ trình cơ sở |
| Định thời trên một số hệ điều hành | W05 slide 38–56 | Để tra, chưa đưa vào lộ trình cơ sở |

Slide 29 có ghi “ĐỌC THÊM”. Người dùng nói “hình như” thi đến slide 28 nên giới hạn này vẫn tạm, không coi đã xác nhận chính thức. Mục lục giữ đầy đủ ảnh nhưng không tự thêm phần ngoài giới hạn vào giảng/tự kiểm/%.

Đã kiểm ảnh công thức W04 slide 21/46, HRRN W05 slide 4 và hình affinity W05 slide 28. Chỗ điều kiện công thức waiting time hoặc tên scheduler/dispatcher chưa rõ trong nguồn đã được ghi ngay tại bài; đối chiếu ngoài cho dispatcher được ghi riêng.

Che phần tiếng Anh để nhớ từ rồi đảo chiều, nói chức năng bằng tiếng Việt. Tổng kết/câu ôn W04 slide 64–73; W05 slide 57–58 phải lọc đúng phần được giữ nếu dùng sau này. Bản terms này không tự giao/chữa các bài tính trong slide.
