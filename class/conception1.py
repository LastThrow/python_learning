"""
类的特殊属性：
__name__：对象名，返回 str
__class__：类名，等价于 type(Person)
__dict__:对象的属性的字典(至关重要)，
__qualname__:类的限定名

实例的特殊属性：
__class__:返回实例的类名，也可用type(instance)取类型
__dict__:返回关于实例的 KV 对，包含实例属性以及相应的值(只是__init__(self)内部的)，不包含类属性
"""


class MyClass:
    """a doc annotation"""
    x = 'abc'

    def foo(self):  # self表示成员方法，指未来实例本身
        print("foo method")


class Person:
    """在python中不需要声明属性"""
    def __init__(self, name, age):  # __init__(self)函数至少有一参数self，用于对生成的属性进行属性配置，此方法不允许有返回值
        self.name = name  # 赋值即定义
        self.age = age

    def show_age(self):
        print(self.name, self.age)


class Person1:
    age = 100  # 类属性，也即java中的静态属性

    def __init__(self, name):
        self.name = name


def main():
    print(MyClass.__doc__)  # 返回文档注释，"__doc__"是类的特殊属性
    print(MyClass.__name__)  # 返回类名，标识符都是str
    print(type(MyClass))  # 返回 <class 'type'>，表示自定义类是type的实例
    ins1 = MyClass()  # 实例化对象
    ins2 = MyClass()  # ins1 和 ins2 是两个完全不同的对象
    """
    实例化：等号右边先执行，构造一个全新的实例
    初始化：将当前实例交给__init__()做出厂配置，将当前实例赋给self，实参再赋给相应形参
            执行__init__()中相应语句，最后将此实例对象交给标识符tom
    """
    tom = Person('tom', 20)
    print(Person)  # 调用__init__()
    print(Person('tim', 10))  # 调用__init__()
    tom.show_age  # 将当前实例与函数的第一参数self绑定
    tom.show_age()
    # "ABC".lower()等价于str.lower("ABC")
    Person.show_age(tom)  # 等价于上面的写法
    print(Person.show_age)  # 返回<function Person.show_age at 0x000001FFEB056488>
    lisa = Person1('lisa')
    print(lisa.name, lisa.age, Person1.age)  # 类属性可以通过实例访问，也可以通过类名访问


if __name__ == '__main__':
    main()
