"""
q = multiprocessing.Queue()
q.put()
q.put_nowait()
q.get()
q.get_nowait()
q.full()
q.empty()
"""
import multiprocessing
import time


def download_from_web(queue):
    print("---in download--id(queue) = ", id(queue))
    data = [11, 22, 33, 44]
    for temp in data:
        queue.put(temp)
    print("----完成存放数据到队列----")


def analysis_data(queue):
    print("---in analysis--id(queue) = ", id(queue))
    get_data = list()
    while not queue.empty():
        data = queue.get()
        get_data.append(data)
    print("---数据下载完成---")
    print(get_data)


def main():
    # 创建一个Queue
    q = multiprocessing.Queue()  # 默认最大
    print("---in main--id(q) = ", id(q))
    # 创建多个进程，将Queue的引用当作实参传递到进程里
    p1 = multiprocessing.Process(target=download_from_web, args=(q,))
    time.sleep(2)
    print(q.empty())  # True
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
