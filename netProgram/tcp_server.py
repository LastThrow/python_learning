import socket


def main():
    # 1、买个手机(创建套接字 socket)
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2、插手机卡(绑定本地信息 bind)
    tcp_server_socket.bind(("", 7788))
    # 3、手机设置为响铃(将套接字由主动b变为被动 listen)
    tcp_server_socket.listen(128)  # 监听7788端口
    while True:
        # 4、等待别人打电话(等待客户端连接 accept)
        print("--------等待新的客户连接---------")
        client_socket, client_addr = tcp_server_socket.accept()  # 返回一个元组，产生用于给客户端服务端额套接字
        print("--------一个客户已经连接---------")
        print("客户端地址:", client_addr)
        while True:  # 循环为一个客户端服务
            recv_msg = client_socket.recv(1024)  # 这里若客户端调用close()，则返回b''，长度为0
            if recv_msg and recv_msg.decode("utf-8") != "exit":
                print("客户端发来信息：%s" % recv_msg.decode("utf-8"))
                reply_msg = input("输入回复客户端的信息：")
                client_socket.send(reply_msg.encode("utf-8"))  # 以utf-8编码为bytes类型发送
            else:
                break
        print("一个客户端服务完毕")
        client_socket.close()
    # 此套接字若是关闭，则新的客户端无法连接，原有的客户端服务不受影响
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
