"""
当调用Thread的时候，只是创建对象，不会创建线程
当调用Thread创建的实例对象的start方法时才会创建线程和执行线程
"""
import threading
import time


class MyThread(threading.Thread):
    # 类继承threading.Thread类，并实现run方法
    def run(self):
        for i in range(5):
            time.sleep(1)
            msg = "I'm " + self.name + "@" + str(i)  # name封装的是当前线程的名字
            print(msg)


def main():
    t = MyThread()
    t.start()


if __name__ == "__main__":
    main()
