import socket
import time
import re
"""
单进程，单线程实现并发操作
将短连接改为长连接
短连接: 浏览器请求一次数据便进行一次连接
长连接: 浏览器一次性将所有的数据获取，并主动断开连接
"""


def service_client(new_socket, request):
    """为客户端返回数据"""
    # request = new_socket.recv(1024).decode("utf-8")   # 接收浏览器的请求
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

    client_socket_list = list()
    while True:
        time.sleep(1)
        try:
            new_socket, client_addr = tcp_server_socket.accept()  # 等待客户端
        except Exception as error:
            pass
        else:
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)
        # 论询效率低，应该为事件通知(epoll)
        for client_socket in client_socket_list:
            try:
                # recv函数其实是去操作系统缓冲区取自己的数据
                # 如果在执行前面的代码的时候，客户端发来数据，会统一保存在缓冲区
                recv_msg = client_socket.recv(1024).decode("utf-8")  # 没有信息则异常
            except Exception as error:
                pass
            else:  # 收到数据
                if recv_msg:  # 客户端发送过来信息
                    service_client(client_socket, recv_msg)
                else:  # 客户端调用close，导致recv_msg为b''
                    print("-----一个客户端退出----")
                    client_socket.close()
                    client_socket_list.remove(client_socket)
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
