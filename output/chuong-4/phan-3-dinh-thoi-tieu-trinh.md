# Phần 3 — Định thời tiểu trình

Nguồn chính: **W05 slide 17**, liên hệ **W03 slide 53–59** và **W04 slide 16**. Học đủ tên phạm vi, đặc biệt từ **contention**.

## Các từ cần nhớ

| Khái niệm (English) | Định nghĩa/dấu hiệu | Nguồn |
|---|---|---|
| Định thời tiểu trình (thread scheduling) | Lựa chọn tiểu trình được thực thi; cần phân biệt mức thư viện và mức nhân. | W05 slide 17 |
| Tiểu trình người dùng (user thread) | Được thư viện quản lý; việc định thời ở mức thư viện xét các tiểu trình trong phạm vi tiến trình. | W05 slide 17; W03 slide 53 |
| Phạm vi tranh chấp trong tiến trình (process-contention scope / PCS) | Các tiểu trình tranh chấp tài nguyên thực thi trong phạm vi cùng một tiến trình, do thư viện luồng định thời theo mô hình nguồn. | W05 slide 17 |
| Tiểu trình hạt nhân (kernel thread) | Đối tượng nhân có thể chọn để chạy trên CPU. | W05 slide 17; W04 slide 16 |
| Phạm vi tranh chấp toàn hệ thống (system-contention scope / SCS) | Các kernel thread được xét trên phạm vi toàn hệ thống để chạy trên các CPU khả dụng. | W05 slide 17 |

## Dễ nhầm

- **PCS:** trong một process. **SCS:** toàn system. Từ chuẩn là **contention**, không phải `content` hay `context`.
- **User thread/kernel thread** nói mức hỗ trợ/quản lý, không có nghĩa một thread chỉ thực thi được trong đúng một chế độ CPU.
- Không phải mọi API tạo user thread đều bắt buộc cung cấp PCS như một chế độ chọn được; còn phụ thuộc mô hình ánh xạ và hệ điều hành. Bài này học phân biệt khái niệm phạm vi trong nguồn.
- PCS/SCS là **phạm vi định thời**, khác với ba mô hình ánh xạ Many-to-One, One-to-One, Many-to-Many ở [Ch3 mục 3.7](../chuong-3/3.7-tieu-trinh.md).
