class Person:
    age = 3
    height = 170

    def __init__(self, name, age=18):
        self.name = name
        self.age = age


def main():
    Person.age = 30  # 将类属性age改为30
    tom = Person('tom')  # 此时tom的age取缺省值，自己没有的属性找类要age
    lisa = Person('lisa', 20)  # 此时lisa的age取实参20，自己有的属性用自己的，不找类要age
    print(1, Person.age, tom.age, lisa.age)  # 1 30 18 20
    print(2, Person.height, tom.height, lisa.height)  # 2 170 170 170
    print(10*'*', lisa.__dict__)  # 实例字典中没有height属性
    lisa.height = 175  # 为实例动态增加实例属性，在lisa字典中增加height属性，而此时tom的字典里没有height
    print(10*'*', lisa.__dict__)  # 实例字典中新增height属性
    print(3, Person.height, tom.height, lisa.height)  # 3 170 170 175
    tom.height += 10
    print(4, Person.height, tom.height, lisa.height)  # 4 170 180 175
    Person.height += 15
    print(5, Person.height, tom.height, lisa.height)  # 5 185 180 175
    print(Person.__dict__)  # 没有weight
    Person.weight = 70  # 动态为类增加一个类属性，类属性是所有实例共有的
    print(6, Person.weight, tom.weight, lisa.weight)  # 6 70 70 70
    print(Person.__dict__)  # 有weight
    print(7, tom.height, tom.__dict__['height'])  # 可以
    print(8, lisa.height, lisa.__class__.__dict__['height'], type(lisa).__dict__['height'])  # 访问路径不一样
    # lisa.__dict__['weight'] 不行，lisa的字典中没有weight


if __name__ == '__main__':
    main()
