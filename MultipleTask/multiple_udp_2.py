import socket
import threading


def recv_msg(udp_socket):
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print("收到数据"+recv_data[0].decode("utf-8"))


def send_msg(udp_socket, dest_ip, dest_port):
    while True:
        send_msg = input("输入发送的数据：")
        udp_socket.sendto(send_msg.encode("utf-8"), (dest_ip, dest_port))


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 7777))

    dest_ip = "127.0.0.1"
    dest_port = 8888

    # 创建2个对象
    t_recv = threading.Thread(target=recv_msg, args=(udp_socket,))
    t_send = threading.Thread(target=send_msg, args=(udp_socket, dest_ip, dest_port))

    # 启动2个线程
    t_recv.start()
    t_send.start()


if __name__ == '__main__':
    main()