import time
import threading


def sing():
    """唱歌5秒"""
    for i in range(5):
        print("----正在唱歌----%d" % i)
        time.sleep(1)


def dance():
    """跳舞3秒"""
    for i in range(3):
        print("----正在跳舞----%d" % i)
        time.sleep(1)


def main():
    # 若创建Thread时执行的函数运行结束，意味着这个子线程消亡
    # 若主线程提前消亡，则子线程也将消亡
    t1 = threading.Thread(target=sing)  # 此处主线程创建第一个子线程
    t2 = threading.Thread(target=dance)  # 此处主线程创建第二个子线程
    # 调用threading.Thread()仅仅只是创建一个普通的对象
    # 只有调用start后，线程队列中才会创建新的线程
    t1.start()  # 线程开始执行
    t2.start()
    while True:
        num = len(threading.enumerate())
        if num == 1:
            print("当前线程数：{}".format(num))  # 打印出创建的线程
            break
        print("当前线程数：{}".format(num))  # 打印出创建的线程
        time.sleep(1)


if __name__ == "__main__":
    main()
