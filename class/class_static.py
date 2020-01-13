"""
class Person:
    def normal_function():
        print('normal')


Person.normal_function()  # 可以调用
Person().normal_function  # 执行时将Person()创建的对象传入normal_function的第一形参，从而报错
"""

#  有一个类无法操作实例，成千上万个实例
#  类可以调用实例方法(手动传实例)，类方法，静态方法
#  实例可以调用 实例方法，类方法，静态方法


class Person:
    def __init__(self):
        self.name = 'tom'

    # 实例方法，带self的是给实例用的，Person.method(Person()) 可以调用，操作实例
    def method(self):
        print('method')

    # 类方法，"classmethod"是一个关键字，不管用类访问，还是实例访问，最后传给第一参数的都是类本身，类似于java中的静态方法
    @classmethod
    def clsmtd(cls):  # 类方法中，第一参数cls指的是类本身，类或实例调用时，都会把类传给第一参数
        print(cls)  # 给类，操作类

    # 静态方法，"staticmethod"是一个关键字，说明此方法只是由类管，无论用类或是实例访问，都不需要任何参数，也可以自己手动添加形参
    @staticmethod
    def stmtd():
        print('static')


def main():
    Person.method(Person())  # 类调用类方法，手动传入实例
    Person().method()  # 实例调用实例方法
    Person.clsmtd()  # 类调用，类型直接传给第一参数
    Person().clsmtd()  # 实例调用，将实例的类型抽取传给第一参数
    Person.stmtd()  # staticmethod不会注入任何实例或类型，只是归到该类，但不用该类任何资源，用的很少
    Person().stmtd()
    print(Person.__dict__)


if __name__ == '__main__':
    main()
