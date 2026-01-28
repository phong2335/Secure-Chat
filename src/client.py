import socket, ssl, threading
from cryptography.fernet import Fernet

host = '127.0.0.1'
post = 8080

try: 
    with open("secret.key", "rb") as f:
        cipher = Fernet(f.read())
except: 
    print("Thiếu file secret.key!")
    exit()

def receive(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data: break
            try: #nếu tin nhắn mã hóa E2EE
                print(f"\n[Room chat]: {cipher.decrypt(data).decode()}")
            except: #nếu tin nhắn không mã hóa
                print(data.decode(), end ="", flush=True) #flush để hiện hết dữ liệu ra màn hình, tránh bị giữ trong bộ đệm
        except: break

def start_client():
    #bỏ qua check chứng chỉ uy tín không
    context = ssl._create_unverified_context()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s = context.wrap_socket(s, server_hostname=host)

    try:
        s.connect((host, post))
    except:
        print("Không kết nối được với Server!")
        return

    threading.Thread(target=receive, args=(s,), daemon=True).start()

    while True:
        msg = input()
        if msg == 'exit': break

        #nếu gõ "ENC: nội dung" thì sẽ mã hóa
        if msg.startswith("ENC:"):
            real_msg = msg[4:]
            enc = cipher.encrypt(real_msg.encode())
            s.sendall(enc)
        else:
            s.sendall(msg.encode())
    s.close()

if __name__ == "__main__":
    start_client()