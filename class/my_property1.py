# coding = UTF-8
class foo(object):
    price = 100

    def get_bar(self):
        print("getter...")
        return self.price

    def set_bar(self, value):
        self.price = value
        print("setter...set value ", value)

    def del_bar(self):
        print("deleter...")

    # property是一个类，有4个参数，property(fget=None, fset=None, fdel=None, doc=None)
    BAR = property(get_bar, set_bar, del_bar, "description...")


def main():
    obj = foo()
    print(obj.BAR)  # 首先在property()里面找第1个参数，调用get_bar方法
    obj.BAR = 200  # 首先在property()里面找第2个参数，调用set_bar方法
    desc = foo.BAR.__doc__  # 首先在property()里面找第4个参数，调用相应方法
    # p = obj.get_bar()  # 通过对象调用实例方法
    # print("price = ", p)
    print(desc)
    del obj.BAR  # 首先在property()里面找第3个参数，调用相应方法


if __name__ == '__main__':
    main()
