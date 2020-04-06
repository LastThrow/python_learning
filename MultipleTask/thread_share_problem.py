import threading
import time

num = 0


def test1(times):
    global num
    for i in range(times):
        num += 1


def test2(times):
    global num
    for i in range(times):
        num += 1


def main():
    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))
    t1.start()
    t2.start()
    time.sleep(10)
    print("-----in main----num:%s" % num)


if __name__ == '__main__':
    main()

"""
原子性：
1、获取num的值
2、将获取的值+1
3、把计算后的值存储起来，并让num指向改存储空间
"""
