from multiprocessing import Pool
import os, time, random


def worker(msg):
    t_start = time.time()
    print("%s 号进程开始执行，进程号为%d" % (msg, os.getpid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg, "号进程执行完毕，耗时%0.2f秒" % (t_stop-t_start))


def main():
    pool = Pool(3)  # 定义一个进程池，最大容量为3
    for i in range(10):
        # Pool().apply_async(要调用的目标，(传递给目标的参数))
        # 每次循环会用空闲的子进程调用目标
        pool.apply_async(worker, (i,))
    print("-----start----")
    pool.close()  # 关闭进程池后，pool不再接收新的请求
    # 等待pool中的所有子进程执行完，必须放在close后
    # 若是没有join，则主进程提前结束，所有子进程消亡
    pool.join()
    print("-----end-----")


if __name__ == '__main__':
    main()
