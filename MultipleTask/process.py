"""
进程和线程区别：
进程先有才有的线程，进程是资源分配的基本单位，执行的工作由线程完成
进程是多个资源的总称，包括代码、内存、显示器、网络等，比如一台PC打开多个QQ
线程比较轻量级，是操作系统调度的单位，比如QQ可以同时聊天、逛空间、播放在线音乐等

多进程完成多任务：
不同资源中，多个箭头同时执行，进程之间互相独立
多线程完成多任务：
同一资源中，有多个箭头同时执行

一个进程可理解为工厂的一条流水线，包括加工物品、加工工具等资源，进程之间不共享资源
一个线程可理解为一条流水线上的一个工人，线程之间共享资源(全局变量)
"""
import multiprocessing
import time

g_num = [1]

def test1(num):
    global g_num
    for i in range(num):
        g_num.append(2)
    print("-----in test1---g_num=", g_num)
    print("-----in test1---id(g_num) =", id(g_num))


def test2(num):
    global g_num
    for i in range(num):
        g_num.append(3)
    print("-----in test2---g_num=", g_num)
    print("-----in test2---id(g_num) =", id(g_num))


def main():
    # 进程实现多任务，耗费资源非常大
    p1 = multiprocessing.Process(target=test1, args=(1,))
    p2 = multiprocessing.Process(target=test2, args=(1,))
    # 主进程创建子进程，子进程复制一份资源
    # 但是代码不复制，共享同一份代码，从指定函数开始执行
    p1.start()
    p2.start()  # 主进程创建子进程

    time.sleep(2)
    print("-----in main---g_num=", g_num)
    print("-----in main---id(g_num) =", id(g_num))


if __name__ == "__main__":
    # 通过打印id我们可以发现，所有子进程和父进程使用的g_num地址都不一样
    # 再一次说明了，其实创建子进程后，子进程将父进程的资源复制一份，再去执行相关代码
    # 进程间资源不共享
    print("--------id(g_num) =", id(g_num))
    main()
