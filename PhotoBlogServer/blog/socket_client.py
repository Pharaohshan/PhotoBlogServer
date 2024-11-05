import socket

def send_file():
    print("Client starting...")  # 启动提示
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 8080))  # 连接到服务器地址和端口

    print("Connecting to server at 127.0.0.1:8080")
    
    # 打开并发送文件
    with open('send_file.txt', 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            client_socket.sendall(data)
            print("Sending data...")  # 发送数据提示

    print("File sent. Sync complete.")  # 同步完成提示
    client_socket.close()

# 启动客户端并发送文件
if __name__ == "__main__":
    send_file()
