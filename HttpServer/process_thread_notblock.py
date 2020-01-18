import socket
"""
单进程，单线程实现并发操作
"""

def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 设定套接字选项
    tcp_server_socket.bind(("", 8888))  # 绑定
    tcp_server_socket.listen(128)  # 监听
    tcp_server_socket.setblocking(False)  # 设置为非堵塞
    client_socket_list = list()
    while True:
        try:
            new_socket, client_addr = tcp_server_socket.accept()  # 等待客户端
        except Exception as error:
            print("-------无新的客户端连接--------")
        else:
            print("新的客户端连接，无异常产生")
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)
        for client_socket in client_socket_list:
            try:
                # recv函数其实是去操作系统缓冲区取自己的数据
                # 如果在执行前面的代码的时候，客户端发来数据，会统一保存在缓冲区
                recv_msg = client_socket.recv(1024)  # 没有信息则异常
            except Exception as error:
                print("------此客户端没有发送数据------")
            else:  # 收到数据
                if recv_msg:  # 客户端发送过来信息
                    print("客户端发来的信息:", recv_msg.decode("utf-8"))
                else:  # 客户端调用close，导致recv_msg为b''
                    print("-----一个客户端退出----")
                    client_socket_list.remove(client_socket)
                    client_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
