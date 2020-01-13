import threading
import time

# 创建互斥锁
mutex = threading.Lock()
g_num = 0


def test1(time):
    global g_num
    for i in range(time):
        mutex.acquire()  # 上锁，若之前没有上锁，则此时上锁成功，否则阻塞直到锁被解开，才可再次使用mutex锁
        g_num += 1  # lst1指向的地址空间改变，需要加global
        mutex.release()
    print("-----in test1 g_num=", g_num)


def test2(time):
    global g_num
    for i in range(time):
        mutex.acquire()  # 上锁，若之前没有上锁，则此时上锁成功，否则阻塞直到锁被解开
        g_num += 1  # lst1指向的地址空间改变，需要加global
        mutex.release()
    print("-----in test2 g_num=", g_num)


def main():
    # target指定将来这个线程去按哪个函数执行代码
    # args指定将来调用函数时，传递哪个参数
    t1 = threading.Thread(target=test1, args=(100000,))
    t2 = threading.Thread(target=test2, args=(100000,))

    t1.start()
    t2.start()

    time.sleep(2)  # 等待两个子线程执行完
    print("-----in main num=", g_num)


if __name__ == "__main__":
    main()