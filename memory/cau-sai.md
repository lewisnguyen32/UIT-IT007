# Chỉ mục câu từng sai

Chi tiết câu sai:

- [Chương 1](cau-sai/chuong-1.md)
- [Chương 2](cau-sai/chuong-2.md)

## File theo chương

Khi chương có câu sai đầu tiên, tạo `memory/cau-sai/chuong-N.md` và thêm một liên kết tại đây. Chỉ mục chỉ có một dòng mỗi chương, không liệt kê từng câu hoặc lưu bộ đếm phải đồng bộ. Không tạo file theo câu hoặc theo phiên.

## Khuôn trong file chi tiết

Mỗi câu có một tiêu đề để tìm nhanh:

```text
## CS-C02-001 | 2.2 | cần ôn | YYYY-MM-DD
- Nguồn: liên kết file bài học + mã nguồn/trang/slide đã đối chiếu.
- Câu hỏi: nguyên văn.
- Trả lời sai đầu tiên (ngày): nguyên văn.
- Đáp án: đáp án đã đối chiếu.
- Lỗi: mô tả ngắn.

CS-C02-001 | YYYY-MM-DD | trả lời khi kiểm tra lại: nguyên văn | đúng/sai; lỗi mới nếu có.
```

Đây là khuôn minh họa, chưa phải câu đã giao/chấm. ID cấp tăng dần trong chương, không đổi hoặc dùng lại. Trạng thái là `cần ôn` hoặc `đã đúng lại`; ngày ở tiêu đề là ngày trả lời gần nhất. Cập nhật tiêu đề và thêm một dòng khi kiểm tra lại, giữ nguyên lịch sử. `Đã đúng lại` không đồng nghĩa thành thạo. Câu chưa trả lời lưu ở câu chờ, không tính là sai.

Năm trường ngay sau tiêu đề, mỗi trường đúng một dòng vật lý; mỗi lần kiểm tra lại cũng chỉ một dòng. Nội dung có xuống dòng được lưu bằng chuỗi JSON có dấu ngoặc kép và ký tự escape để giữ nguyên nội dung mà không làm lệch lệnh đọc năm dòng dưới đây.

## Đọc chọn lọc

1. Chỉ tra chương đang ôn trong chỉ mục này. Dùng `rg -n '^## CS-'` trên file chương để tìm theo mục/trạng thái; nếu nhiều kết quả, lọc và giới hạn số dòng trước khi đưa vào context.
2. Chọn 1–3 câu phù hợp, ưu tiên câu `cần ôn`; đôi lúc có thể hỏi lại câu `đã đúng lại`. Chỉ đọc tiêu đề và năm dòng nội dung cố định của ID đã chọn, không nạp cả file chương.
3. Nếu cần xem kết quả gần đây, lọc dòng bắt đầu bằng ID đó và chỉ lấy hai dòng cuối. Chỉ đọc lịch sử cũ hơn khi có lý do cụ thể.

Ví dụ thao tác khi file/ID tương ứng đã tồn tại:

```powershell
rg -n '^## CS-' memory/cau-sai/chuong-2.md | Select-String -SimpleMatch '| 2.2 | cần ôn |' | Select-Object -First 3
rg -n -A 5 '^## CS-C02-001 \|' memory/cau-sai/chuong-2.md
rg '^CS-C02-001 \|' memory/cau-sai/chuong-2.md | Select-Object -Last 2
```

`memory.md` và ghi chú chương chỉ dẫn tới đây hoặc tới ID liên quan; không chép lại câu/đáp án/lịch sử.
