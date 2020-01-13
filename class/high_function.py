class Person:
    pass


# 高阶函数，动态增加属性
def add_name(name: str, cls):
    cls.NAME = name


def main():
    print(1, Person.__dict__)
    add_name('tom', Person)
    Person.age = 20
    print(2, Person.__dict__)


if __name__ == '__main__':
    main()
