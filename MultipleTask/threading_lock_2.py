import threading
import time

# 创建互斥锁
mutex = threading.Lock()
num = 0


def test1(times):
    global num
    for i in range(times):
        mutex.acquire()  # 上锁，若之前没有上锁，则此时上锁成功，否则阻塞直到锁被解开，才可再次使用mutex锁
        num += 1
        mutex.release()


def test2(times):
    global num
    for i in range(times):
        mutex.acquire()  # 上锁，若之前没有上锁，则此时上锁成功，否则阻塞直到锁被解开
        num += 1
        mutex.release()


def main():
    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))
    t1.start()
    t2.start()
    time.sleep(2)  # 等待两个子线程执行完
    print("-----in main num=", num)


if __name__ == "__main__":
    main()
