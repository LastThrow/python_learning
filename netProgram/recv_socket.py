"""
接收流程：
1、创建套接字
2、绑定本地的ip和port
3、接收数据
4、关闭套接字
"""

import socket


def main():
    # 创建udp套接字，即可收也可发
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本地信息
    local_addr = ("", 8080)  # 只能绑定自己的ip，空字符串表示本地ip
    udp_socket.bind(local_addr)  # 监听本地主机的8080端口
    # 接收数据

    while True:
        recv_data = udp_socket.recvfrom(1024)
        recv_msg = recv_data[0]  # 信息
        recv_from = recv_data[1]  # (源ip，源端口)
        # 打印接收到的数据
        if recv_msg.decode("utf-8") == "exit":
            break
        print("接收到信息：%s，来自于：%s" % (recv_msg.decode("utf-8"), str(recv_from)))
        # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()
