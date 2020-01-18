from collections import Iterable

"""
此类中没有list用于存储数据，只是在调用时直接生成，不会占用大量内存空间存储数据
__iter__(可迭代对象)
__next__(迭代器)
"""
class Fibonacci(object):
    def __init__(self, num):
        self.num = num
        self.cur = 0
        self.a = 0
        self.b = 1

    # 实现__iter__()方法后，此类的实例对象就是可迭代对象
    def __iter__(self):
        return self

    def __next__(self):
        if self.cur < self.num:
            res = self.a
            self.a, self.b = self.b, self.a+self.b
            self.cur += 1
            return res
        else:
            self.__init__(self.num)  # 一次调用完成后，重新恢复对象
            raise StopIteration  # 当迭代器取完时，产生异常到调用处进行处理，自动停止


def main():
    fibos = Fibonacci(10)  # 只是定义了一个可迭代对象，存储的是生成数据的方式，只占用少量空间
    for fibo in fibos:  # 真正调用时再将需要的数据一个一个返回
        print(fibo, end=" ")
    print()
    print(list(fibos))
    print(tuple(fibos))


if __name__ == '__main__':
    main()
