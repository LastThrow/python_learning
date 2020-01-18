import socket
import re
import threading

"""
为什么是四次挥手不是三次挥手?
1.回复已经收到对方释放连接的消息，由于客户端等着确认，应该尽快进行第二次挥手
2.通知应用程序调用close，进行第三次挥手
  但是应用程序此时不一定就调用close，只能等到应用程序调用close的时候才进行第三次挥手
3.服务器调用close后，发送第三次挥手的包，客户端收到第三次挥手的包后，会发送第四次挥手的包
  然后接着等待一段时间，以免服务器没有收到第四次挥手的包，再重新发送第三次挥手的包
"""


def service_client(new_socket):
    """为客户端返回数据"""
    request = new_socket.recv(1024).decode("utf-8")   # 接收浏览器的请求
    if request == "":
        new_socket.close()
        print("**************空请求***************")
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
        header = "HTTP/1.1 404 NOT FOUND\r\n"
        body = "------file not found------"
        response = header + "\r\n" + body
        new_socket.send(response.encode("utf-8"))
    else:
        body = f.read()
        f.close()
        header = "HTTP/1.1 200 OK\r\n"  # 换行
        response = header + "\r\n"
        new_socket.send(response.encode("utf-8"))  # 前端中charset=utf-8表示设置浏览器解析数据的编码格式
        new_socket.send(body)
    new_socket.close()


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 设定套接字选项
    tcp_server_socket.bind(("", 8888))  # 绑定
    tcp_server_socket.listen(128)  # 监听
    while True:
        new_socket, client_addr = tcp_server_socket.accept()  # 等待客户端
        t = threading.Thread(target=service_client, args=(new_socket,))
        t.start()
        # 多进程启动时，子进程中会复制父进程里的资源，包括这个new_socket
        # 复制后父子进程中的new_socket都指向系统底层同一个资源
        # 此处关闭父进程中的new_socket，子进程执行完成后再关闭new_socket
        # 四次挥手才会开始，系统底层释放资源
        # 而多线程里则不复制资源，故主线程不能调用close
        # new_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
