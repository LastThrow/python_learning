import socket


def main():
    # 创建Tcp的套接字,socket.STREAM
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接服务器
    tcp_socket.connect(("127.0.0.1", 7788))  # 服务器的ip和port
    # 发送，接收数据
    while True:
        send_msg = input("输入发送的信息：")
        if send_msg == "exit":
            break
        tcp_socket.send(send_msg.encode("utf-8"))
        # 关闭套接字
        recv_data = tcp_socket.recv(1024).decode("utf-8")
        print("服务器发来信息：", recv_data)
    tcp_socket.close()


if __name__ == "__main__":
    main()
