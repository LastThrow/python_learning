"""
简单总结：
1.进程是资源分配的单位
2.线程是操作系统分配的单位
3.进程切换需要的资源大，效率低
4.线程切换需要的资源一般，效率一般(不考虑GIL的情况下)
5.协程切换任务需要资源少，效率高
6.多进程，多线程根据cpu核数不一样可能是并行的，但在协程是在一个线程中，所以是并发的
"""
import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()  # 用于将耗时函数替换成gevent内的函数


def download_pic(img_name, img_url):
    req = urllib.request.urlopen(img_url)
    img_content = req.read()
    with open(img_name , 'wb') as f:
        f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(download_pic, '1.jpg', "https://images.unsplash.com/photo-1579102298128-754755f6087b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=600&q=60"),
        gevent.spawn(download_pic, '2.jpg', "https://images.unsplash.com/photo-1579085354165-2363f36061ff?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=600&q=60"),
        gevent.spawn(download_pic, '3.jpg', "https://images.unsplash.com/photo-1579097273874-d7857a3996b0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=600&q=60")
    ])


if __name__ == '__main__':
    main()
