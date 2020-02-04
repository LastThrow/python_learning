from collections import Iterable
"""
生成器是一种特殊的迭代器
"""


def create_num(all):
    a, b = 0, 1
    cur = 0
    while cur < all:
        yield a  # 执行到这堵塞，将a返回到调用处，再次for循环时从此处开始执行
        a, b = b, a+b
        cur += 1
    return 'OK......'


def main():
    nums = create_num(10)  # 创建一个生成器对象
    while True:
        try:
            res = next(nums)
            print(res, end=' ')
        except StopIteration as ex:
            print()
            print(ex.value)  # 得到生成器的return值
            break


if __name__ == '__main__':
    main()
