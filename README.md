# 🔒 Secure Chat System

Hệ thống chat an toàn được viết bằng **Python**, tích hợp các cơ chế bảo mật tiêu chuẩn để đảm bảo tính Bí mật (Confidentiality), Toàn vẹn (Integrity) và Xác thực (Authentication).

## 🚀 Tính năng nổi bật

Dự án tập trung giải quyết các vấn đề bảo mật mạng cơ bản:

- **Mã hóa đường truyền (Transport Security):** Sử dụng **SSL/TLS** (Self-signed certificate) để chống nghe lén (Man-in-the-Middle).
- **Mã hóa đầu cuối (End-to-End Encryption):** Tin nhắn được mã hóa bằng **Fernet (AES)**, Server chỉ đóng vai trò trung chuyển và không thể đọc nội dung tin nhắn.
- **Xác thực mạnh (Authentication):**
  - Password được băm (Hashing) bằng **SHA-256** kết hợp với **Salt** để chống tấn công Rainbow Table.
  - Tích hợp **2FA (Two-Factor Authentication)** sử dụng TOTP (Google Authenticator).
- **Cơ sở dữ liệu:** Sử dụng SQLite để quản lý người dùng.
- **Đa luồng (Multithreading):** Server có thể xử lý nhiều Client cùng lúc.

## 🛠️ Công nghệ sử dụng (Tech Stack)

- **Language:** Python 3
- **Network:** Python Socket (TCP/IP)
- **Security Libraries:**
  - `ssl`: Tạo kết nối an toàn TLS.
  - `cryptography`: Tạo khóa và mã hóa Fernet.
  - `hashlib`: Băm mật khẩu (SHA-256).
  - `pyotp`: Tạo mã OTP và QR Code.
  - `sqlite3`: Lưu trữ dữ liệu.

## ⚙️ Cài đặt & Chạy (Installation)

### 1. Cài đặt thư viện

```bash
pip install -r requirements.txt
```

### 2. Khởi tạo Khóa & Database

Bạn cần chạy các script sau để sinh ra khóa bí mật và database (vì chúng không được upload lên git để đảm bảo an toàn):

```bash
# Sinh khóa mã hóa tin nhắn (secret.key)
python GenFernet.py

# Khởi tạo database người dùng (users.db)
python init_database.py
```

_Lưu ý: Bạn cần tự tạo chứng chỉ SSL (`server.crt` và `server.key`) bằng OpenSSL và đặt vào thư mục gốc._

### 3. Chạy Server

```bash
python server.py
```

### 4. Chạy Client

```bash
python client.py
```

## 📸 Demo

(Chèn ảnh chụp màn hình lúc đăng nhập thành công và lúc chat mã hóa vào đây)
