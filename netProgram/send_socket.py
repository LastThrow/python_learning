"""
接收流程：
1、创建套接字
2、发送数据，以bytes的形式发送到指定 ip 和 port
3、关闭套接字
"""
import socket


def main():
    # 创建udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest_addr = ("127.0.0.1", 8080)  # 目的信息
    # 绑定本地信息
    local_addr = ("", 8888)  # 空字符串表示本地ip
    udp_socket.bind(local_addr)
    while True:
        send_data = input("输入发送的数据：")
        # 收发数据
        if send_data == "exit":
            udp_socket.sendto(send_data.encode("utf-8"), dest_addr)
            break
        udp_socket.sendto(send_data.encode("utf-8"), dest_addr)  # encode()返回bytes
    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()
