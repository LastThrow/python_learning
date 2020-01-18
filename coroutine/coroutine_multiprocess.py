import time

def test1():
    while True:
        print('-----test1-----')
        time.sleep(0.5)
        yield


def test2():
    while True:
        print('-----test2-----')
        time.sleep(0.5)
        yield


def main():
    t1 = test1()
    t2 = test2()
    while True:
        # next(t1)
        # next(t2)
        t1.send(None)  # 假并发
        t2.send(None)


if __name__ == '__main__':
    main()