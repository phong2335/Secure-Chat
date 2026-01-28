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

## 🛠️ Công nghệ sử dụng

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

Bạn cần chạy các script sau để sinh ra khóa bí mật và database

```bash
# Sinh khóa mã hóa tin nhắn (secret.key)
python GenFernet.py

# Khởi tạo database người dùng (users.db)
python init_database.py
```

_Lưu ý: Bạn cần tự tạo chứng chỉ SSL (`server.crt` và `server.key`) bằng OpenSSL và đặt vào thư mục gốc._

- Lệnh tạo chứng chỉ bằng OpenSSL
  ```powershell
  openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.crt -days 365 -nodes
  ```

  - **`req`**: (Request) Lệnh yêu cầu quản lý chứng chỉ.
  - **`x509`**: Chỉ định xuất ra chứng chỉ tự ký (Self-signed) thay vì tạo một yêu cầu ký chứng chỉ (CSR) gửi lên các tổ chức CA (Certificate Authority). Phù hợp cho môi trường thử nghiệm/nội bộ.
  - **`newkey rsa:2048`**: Tạo một cặp khóa mới bằng thuật toán RSA với độ dài 2048 bit.
  - **`keyout server.key`**: Lưu cái **Chìa khóa bí mật** vào file tên là `server.key`.
  - **`out server.crt`**: Lưu cái **Chứng chỉ công khai** vào file tên là `server.crt`.
  - **`days 365`**: Chứng chỉ này có hạn sử dụng là 1 năm (365 ngày).
  - `nodes`: (No DES) Quan trọng. Tham số này yêu cầu OpenSSL **không mã hóa file Private Key**. Điều này cho phép Server khởi động tự động mà không cần quản trị viên nhập mật khẩu để mở khóa file key mỗi lần chạy.

### 3. Chạy Server

```bash
python server.py
```

### 4. Chạy Client

```bash
python client.py
```

## 📸 Demo

- Giao diện khi chạy server và lắng nghe các client kết nối đến
  ![image.png](images/image1.png)
  
- Giao diện menu lựa chọn từ client
  ![image.png](images/image2.png)
- Đăng ký thành công và gửi QR để thiết lập xác thực 2 lớp, dùng ứng dụng xác thực Authenticator
  ![image.png](images/image3.png)
- Giao diện đăng nhập thành công
  ![image.png](images/image4.png)
- Muốn gửi tin nhắn mã hóa thì gửi theo cú pháp
  ```powershell
  ENC: 'nội dung tin nhắn'
  ```
- Nếu không có ‘ENC:’ thì tin nhắn gửi đi sẽ không được mã hóa bằng Fernet mà chỉ có TLS.
