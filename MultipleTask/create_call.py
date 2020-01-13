"""
当调用Thread的时候，只是创建对象，不会创建线程
当调用Thread创建的实例对象的start方法时才会创建线程和执行线程
"""
import threading
import time


def test():
    for i in range(5):
        print("%d-------" % i)
        time.sleep(1)


def main():
    print(threading.enumerate())  # 只打印主线程
    t1 = threading.Thread(target=test)  # 创建普通对象
    print(threading.enumerate())  # 只打印主线程
    t1.start()  # 创建并执行线程
    print(threading.enumerate())  # 打印主线程和主线程


if __name__ == "__main__":
    main()
