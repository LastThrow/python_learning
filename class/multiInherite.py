"""
grandson的__init__开始被调用
son1的__init__开始被调用
parent的__init__开始被调用
parent的__init__结束调用
son1的__init__结束调用
son2的__init__开始被调用
parent的__init__开始被调用
parent的__init__结束调用
son2的__init__结束调用
grandson的__init__结束调用
"""


class Parent(object):
    def __init__(self, name):
        print("parent的__init__开始被调用")
        self.name = name
        print("parent的__init__结束调用")


class Son1(Parent):
    def __init__(self, name, age):
        print("son1的__init__开始被调用")
        self.age = age
        Parent.__init__(self, name)
        print("son1的__init__结束调用")


class Son2(Parent):
    def __init__(self, name, gender):
        print("son2的__init__开始被调用")
        self.gender = gender
        Parent.__init__(self, name)
        print("son2的__init__结束调用")


class GrandSon(Son1, Son2):
    def __init__(self, name, age, gender):
        print("grandson的__init__开始被调用")
        Son1.__init__(self, name, age)
        Son2.__init__(self, name, gender)
        print("grandson的__init__结束调用")


def main():
    grandson = GrandSon('zhang', 30, 'woman')


if __name__ == '__main__':
    main()
