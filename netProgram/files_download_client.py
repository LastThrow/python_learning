import socket


def main():
    # 1.创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.获取服务器的ip和port
    dest_ip = "192.168.0.104"
    dest_port = 7788
    # 3.连接服务器
    tcp_socket.connect((dest_ip, dest_port))
    while True:
        # 4.获取下载的文件名字
        download_filename = input("输入下载文件名：")
        if download_filename == "exit":
            tcp_socket.send(download_filename.encode("utf-8"))
            break
        # 5.将文件名字发送到服务器
        tcp_socket.send(download_filename.encode("utf-8"))
        # 6.接收文件中的数据
        recv_data = tcp_socket.recv(1024*1024)  # 单位字节 B
        if recv_data.decode("utf-8")[0] != '没':
            # 7.保存数据到文件中
            with open("new_" + download_filename, "wb") as f:
                f.write(recv_data)
            print("文件%s下载完成!" % download_filename)
        else:
            print(recv_data.decode("utf-8"))
    # 8.关闭套接字
    tcp_socket.close()

if __name__ == "__main__":
    main()
