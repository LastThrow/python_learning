import socket


def send(udp_socket):
    dest_ip = "127.0.0.1"
    dest_port = 8080
    send_msg = input("输入要发送的信息：")
    udp_socket.sendto(send_msg.encode("utf-8"), (dest_ip, dest_port))


def recv(udp_socket):
    recv_data = udp_socket.recvfrom(1024)
    recv_msg = recv_data[0]
    recv_from = recv_data[1]
    print("%s:%s" % (str(recv_from), recv_msg.decode("utf-8")))


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定端口
    udp_socket.bind(("127.0.0.1", 8888))  # 此套接字监听8888端口 
    # 循环
    while True:
        print("-------聊天器------")
        print("1:发送信息")
        print("2:接收信息")
        print("0:退出系统")
        op = input("请输入功能：")
        if op == "1":
            # 发送
            send(udp_socket)
        elif op == "2":
            # 接收并显示
            recv(udp_socket)
        elif op == "0":
            break
        else:
            print("输入错误，请重新输入！")


if __name__ == "__main__":
    main()
