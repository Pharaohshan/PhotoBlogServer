import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8080))  # 监听所有地址的 8080 端口
    server_socket.listen(1)
    print("Socket server listening on port 8080...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connected by {addr}")
        
        # 接收客户端发送的数据并保存到文件
        with open('received_file.txt', 'wb') as f:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    print("No more data received. Closing file.")
                    break
                f.write(data)
                print(f"Received data chunk of size {len(data)}")  # 输出每次接收的数据大小
        
        print("File received.")
        client_socket.close()

# 运行服务器
if __name__ == "__main__":
    start_server()
