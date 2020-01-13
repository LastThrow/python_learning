class Money(object):
    def __init__(self):
        """
        __xxx为类私有属性，Money().__money获取不到
        python解释器将名字重整为 _Money__money，Money()._Money__money即可获取
        只有在类里写的，被python解释器重整名字后的才是私有的
        """
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:非整形变量")

    # 定义一个属性，当对这个money设置值时调用setMoney，当获取值时调用getMoney
    # property是一个类，有4个参数，property(fget=None, fset=None, fdel=None, doc=None)
    money = property(getMoney, setMoney)

    def __call__(self):  # 实现__call__方法，通过对象调用
        print('__call__')

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def __getslice__(self, i, j):
        pass

    def __setslice__(self, i, j, sequence):
        pass

    def __delslice__(self, i, j):
        pass


def main():
    a = Money()
    a.money = 100
    print(a.money)
    print(a.__class__)  # 查看当前对象是谁创建的
    print(a.__module__)  # 查看当前对象在哪个模块
    #  __new__用于创建对象，__init__用于初始化对象，共同完成构造对象
    #  __del__用于删除对象，由python解释器进行垃圾回收时自动执行
    # __call__
    a()  # 调用__call__方法，装饰器得用到
    #  __str__ 可用于得到对象的描述
    res = a['hello']  # 自动执行 __getitem__
    a['world'] = 'shen'  # 自动执行 __setitem__
    del a['hello']  # 自动执行 __del__

    a[-1:1:1]  # 自动执行 __getslice__
    a[0:2] = [11, 22, 33]  # 自动执行 __setslice__
    del a[0:2]  # 自动执行 __delslice__


if __name__ == '__main__':
    main()

