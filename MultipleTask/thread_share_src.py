import threading
import time

num = 100


def test1():
    global num
    num += 1
    print("-----in test1----num:%s" % num)


def test2():
    print("-----in test2----num:%s" % num)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)
    print("-----in main----num:%s" % num)


if __name__ == '__main__':
    main()
