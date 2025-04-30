# 🏘️ Crawler dữ liệu căn hộ chung cư Đà Nẵng từ Alonhadat

## 📌 Mô tả
Tool tự động thu thập thông tin các căn hộ chung cư đang rao bán tại Đà Nẵng từ website [alonhadat.com.vn](https://alonhadat.com.vn).

Thông tin được thu thập bao gồm:
- Tiêu đề
- Mô tả
- Diện tích
- Giá
- Địa chỉ

Kết quả được lưu vào file Excel theo ngày, ví dụ: `alonhadat_da_nang_20250429.xlsx`.

---

## 🚀 Cài đặt

### Bước 1: Clone project
```bash
git clone <link-project-cua-ban>
cd <ten-thu-muc>

    Bước 2: Cài đặt thư viện cần thiết
    pip install -r requirements.txt

    Bước 3: Chạy crawler thủ công
    - Sau khi cài thư viện, chạy file Python: python alonhadat.py
    - File kết quả sẽ được lưu tại thư mục hiện tại với tên dạng: alonhadat_da_nang_<ngày>.xlsx
    - Ví dụ: alonhadat_da_nang_20250429.xlsx

    📁 Cấu trúc thư mục
    ├── alonhadat.py              # File chính để crawl
    ├── requirements.txt          # Danh sách thư viện cần cài
    └── README.md                 # Hướng dẫn sử dụng

    📝 Ghi chú
    Cần cài sẵn Google Chrome.

    ChromeDriver phải tương thích với phiên bản Chrome bạn đang dùng.

    Khi website yêu cầu Captcha, bạn có thể xác thực tay trực tiếp trong trình duyệt, sau đó quay lại terminal nhấn ENTER (nếu có tạm dừng).


    
