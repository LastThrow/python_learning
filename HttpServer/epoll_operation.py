import socket
import time
import re
import select

"""
单进程，单线程，epoll，事件通知最快
利用epoll将前面程序遍历list改为OS进行事件通知，提高效率 
"""


def service_client(new_socket, request):
    """为客户端返回数据"""
    if request == "":
        new_socket.close()
        return
    print(request)
    request_lines = request.splitlines()
    print(request_lines)
    # GET /index.html HTTP/1.1
    file_name = ""
    res = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    if res:
        file_name = res.group(1)
        print("文件名:", file_name)
        if file_name == "/":
            file_name = "/index.html"
    try:
        f = open("./html" + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        body = "------file not found------"
        response += "Content-Length:%d\r\n" % len(body)
        response += "\r\n" + body
        new_socket.send(response.encode("utf-8"))  # 前端中charset=utf-8表示设置浏览器解析数据的编码格式
    else:
        body = f.read()
        f.close()
        response = "HTTP/1.1 200 OK\r\n"  # 换行
        response += "Content-Length:%d\r\n" % len(body.decode("utf-8"))
        response += "\r\n" + body.decode("utf-8")
        new_socket.send(response.encode("utf-8"))  # 前端中charset=utf-8表示设置浏览器解析数据的编码格式
        new_socket.send(body)


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 设定套接字选项
    tcp_server_socket.bind(("", 8888))  # 绑定
    tcp_server_socket.listen(128)  # 监听
    tcp_server_socket.setblocking(False)  # 设置为非堵塞
    # 创建一个epoll对象
    epl = select.epoll()  # http服务器和内核直接共用的空间

    fd_event_dict = dict()
    # 将监听套接字对应的文件描述符fd
    epl.register(tcp_server_socket.fileno(), select.EPOLLIN)  # 套接字有输入就通知此监听套接字
    fd_event_dict[tcp_server_socket.fileno()] = tcp_server_socket
    while True:
        time.sleep(1)
        # 默认堵塞，直到OS通过事件通知告诉程序，才会解堵塞
        # 返回有消息的事件列表[(fd, event), (套接字对应的文件描述符，文件描述符代表的事件)]
        fd_event_list = epl.poll()
        for fd, event in fd_event_list:
            # 对于监听套接字，等待新的客户端到来
            if fd == tcp_server_socket.fileno():
                new_socket, client_addr = tcp_server_socket.accept()
                epl.register(new_socket.fileno(), select.EPOLLIN)
                fd_event_dict[new_socket.fileno()] = new_socket
            # 对于通信的套接字，处理客户端发送的请求
            elif event == select.EPOLLIN:
                # 判断已经连接的客户端是否有数据发送过来
                recv_msg = fd_event_dict[fd].recv(1024).decode("utf-8")  # 没有信息则异常
                if recv_msg:  # 客户端发送过来信息
                    service_client(fd_event_dict[fd], recv_msg)
                else:  # 客户端调用close，导致recv_msg为b''
                    print("-----一个客户端退出----")
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
