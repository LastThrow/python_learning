from collections import Iterable
"""
生成器是一种特殊的迭代器
有使得函数暂停执行并返回值的功能
"""
def create_num(all):
    a, b = 0, 1
    cur = 0
    while cur < all:
        res = yield a  # 执行到这堵塞，将a返回到调用处，再次for循环时从此处开始执行
        print('send传入的参数为', res)  # 打印send传入的参数
        a, b = b, a+b
        cur += 1
    return 'OK......'


def main():
    nums = create_num(10)  # 创建一个生成器对象
    while True:
        try:
            # send也是取一个值，可以给生成器传参
            # 但是第一次启动生成器用next()，第一次send()传入的参数没有变量接收
            res = nums.send(None)
            print(res, end=' ')
        except StopIteration as ex:
            print(ex.value)  # 得到生成器的return值
            break


if __name__ == '__main__':
    main()
