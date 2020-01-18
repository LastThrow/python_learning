"""
此代码还是单线程，只是当某个任务浪费时间时，去做了别的任务
协程依赖线程，线程依赖进程
协程切换，就像是调用一个函数，耗费资源少，效率高
"""
import time
import gevent
from gevent import monkey


monkey.patch_all()  # 打补丁，检查所有耗时的代码，自动换成gevent


def fun(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # gevent.sleep(1)  # time.sleep(1)不行
        time.sleep(0.5)


def main():
    # 真正是这样用的
    gevent.joinall([
        gevent.spawn(fun, 5),  # 创建Greenlet对象，但是没有执行fun函数
        gevent.spawn(fun, 4),
        gevent.spawn(fun, 3)
    ])
    """
    g1 = gevent.spawn(fun, 5)  # 创建Greenlet对象，但是没有执行fun函数
    g2 = gevent.spawn(fun, 4)
    g3 = gevent.spawn(fun, 3)
    g1.join()
    g2.join()
    g3.join()
    """


if __name__ == '__main__':
    main()
