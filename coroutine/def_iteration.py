from collections import Iterable
"""
迭代器存放的是生成数据的方式，而不是存放直接生成的数据
节省存放数据的空间
"""

class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """实现__iter__()方法后，此类的实例对象就是可迭代对象"""
        return ClassIterator(self)


class ClassIterator(object):
    """若一个类实现了__iter__()和__next__()，此类的实例对象就是一个迭代器"""

    def __init__(self, classmate):
        self.classmate = classmate
        self.cur = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.cur < len(self.classmate.names):
            name = self.classmate.names[self.cur]
            self.cur += 1
            return name
        else:
            raise StopIteration  # 当迭代器取完时，产生异常到f调用处进行处理，自动停止


def main():
    mates = Classmate()
    mates.add("shen")
    mates.add("huang")
    mates.add("zhang")
    # for循环执行时，首先判断mates是否实现了__iter__()，是一个可迭代对象
    # 然后调用mates的__iter__()得到一个迭代器对象的引用
    # for循环在取值时，实际上取的是上述迭代器对象__next__()的返回值，mate接收此返回值
    for mate in mates:
        print(mate)


if __name__ == '__main__':
    main()
