import threading
import time


lst = [11, 22]


def test1(temp):
    global lst
    temp += [33]  # lst1指向的地址空间改变，需要加global
    print("-----in test1 temp=", temp)


def test2(temp):
    print("-----in test2 temp=", temp)


def main():
    # target指定将来这个线程去按哪个函数执行代码
    # args指定将来调用函数时，传递哪个参数
    t1 = threading.Thread(target=test1, args=(lst, ))
    t2 = threading.Thread(target=test2, args=(lst, ))
    
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)
    
    print("-----in main lst=", lst)


if __name__ == "__main__":
    main()


