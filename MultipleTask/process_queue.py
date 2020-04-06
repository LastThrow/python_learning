"""
q = multiprocessing.Queue()
q.put()  # 放入数据，获取队列满时阻塞
q.put_nowait()  # 放入数据，获取队列满时异常
q.get()  # 获取数据，获取队列空时堵塞
q.get_nowait()  # 获取数据，获取队列空时异常
q.full()
q.empty()
"""
import multiprocessing
import time


def put_data(queue):
    # print("---in get_data--id(queue) = ", id(queue))
    data = [11, 22, 33, 44]
    for temp in data:
        queue.put(temp)
    print("----存放数据到队列完成----")


def get_data(queue):
    # print("---in get_data--id(queue) = ", id(queue))
    data_list = list()
    while True:
        data = queue.get()
        data_list.append(data)
        if queue.empty():
            break
    print("---从队列获取数据完成---")
    print(data_list)


def main():
    # 创建一个Queue
    q = multiprocessing.Queue()
    # print("---in main--id(q) = ", id(q))
    # 创建多个进程，将Queue的引用当作实参传递到进程里
    p1 = multiprocessing.Process(target=put_data, args=(q,))
    p2 = multiprocessing.Process(target=get_data, args=(q,))
    p1.start()
    time.sleep(1)
    p2.start()


if __name__ == '__main__':
    main()
