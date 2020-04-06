import time
import threading


mutex_1 = threading.Lock()
mutex_2 = threading.Lock()


class MyThread1(threading.Thread):
    def run(self):
        mutex_1.acquire()
        print(self.name + "-------mutex_1被占-------")
        time.sleep(1)
        print(self.name + "-------等待mutex_2-------")
        mutex_2.acquire()  # 此时mutex_2已经被占用，阻塞直到mutex_2被释放

        mutex_1.release()
        mutex_2.release()


class MyThread2(threading.Thread):
    def run(self):
        mutex_2.acquire()
        print(self.name + "-------mutex_2被占-------")
        time.sleep(1)
        print(self.name + "-------等待mutex_1-------")
        mutex_1.acquire()  # 此时mutex_1已经被占用，阻塞直到mutex_1被释放

        mutex_1.release()
        mutex_2.release()


def main():
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
