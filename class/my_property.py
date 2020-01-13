class Goods:
    @property  # 加语法糖
    def size(self):  # 定义成函数
        return 100

    def price(self):
        return 1000


def main():
    res1 = Goods().price()  # 调用实例方法
    res2 = Goods().size  # 调用property属性,而不用去调方法，这是封装的体现，不需要考虑传参的问题
    print(res1, res2)


if __name__ == '__main__':
    main()
