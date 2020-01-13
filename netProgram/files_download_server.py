import socket

def send_file_to_client(client_socket, client_addr):
    while True:
        file_name = client_socket.recv(1024).decode("utf-8")
        if file_name == "exit":
            break
        print("客户端 %s 下载的文件是:%s" % (client_addr, file_name))
        file_content = None
        try:
            f = open(file_name, "rb")
            file_content = f.read()
            f.close()
        except Exception as ret:
            client_socket.send(str("没有"+file_name+"这一文件, 换一个下载").encode("utf-8") )
        if file_content:
            client_socket.send(file_content)


def main():
    # 1、买个手机(创建套接字 socket)
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2、插手机卡(绑定本地信息 bind)
    tcp_server_socket.bind(("", 7788))
    # 3、手机设置为响铃(将套接字由主动b变为被动 listen)
    tcp_server_socket.listen(128)  # 监听7788端口
    while True:
        client_socket, client_addr = tcp_server_socket.accept()  # 返回一个元组，产生用于给客户端服务的套接字
        send_file_to_client(client_socket, client_addr)
        client_socket.close()
        break  # 这里只能服务一次
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
