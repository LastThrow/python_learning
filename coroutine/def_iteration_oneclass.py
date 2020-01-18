from collections import Iterable


class Classmate(object):
    def __init__(self):
        self.names = list()
        self.cur = 0

    def add(self, name):
        self.names.append(name)

    # 实现__iter__()方法后，此类的实例对象就是可迭代对象
    def __iter__(self):
        return self

    def __next__(self):
        if self.cur < len(self.names):
            name = self.names[self.cur]
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
