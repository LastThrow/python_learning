class Goods:
    p = 100

    @property  # 获取
    def price(self):
        print('@property')
        return self.p

    @price.setter  # 设置
    def price(self, value):
        self.p = value
        print('@price.setter')

    @price.deleter  # 删除
    def price(self):
        print('@price.deleter')


def main():
    obj = Goods()
    print(obj.price)  # 调用了@property修饰的方法
    obj.price = 123  # 调用了@price.setter修饰的方法，并将123传递给形参value
    print(obj.price)  # 调用了@property修饰的方法
    del obj.price  # 调用了@price.deleter修饰的方法


if __name__ == '__main__':
    main()
