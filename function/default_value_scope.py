def fun1(x=1):  # 标识符fun1和内存中一个函数对象关联，此时fun1是一个全局变量
    x += 1
    print(x)


def fun2(y=[]):  # y每次引用相同的地址，因为fun2为全局变量，所以fun2执行结束后引用计数不会减1，y指向的内存空间不变
    y.append(1)
    print(id(y))


def fun3(a=1, b=2):  # 每次运行时所有缺省值的引用地址空间都不变
    print('id(a)=', id(a))
    print('id(b)=', id(b))


def fun4(xyz, m=123, n='abc'):
    print(fun4.__defaults__)  # (123, 'abc')
    print('id(m)=', id(m))  # id(m)= 1470090064
    m = 11111111  # 赋值即重新定义，m这个标识符指向的内存空间改变,不再指向缺省值的内存空间，缺省值的内存空间不变
    print('id(m)', id(m))  # id(m)=2784501932272
    print(fun4.__defaults__)  # (123, 'abc')


def fun5(xyz, m=123, *, n='abc', t=[1, 2]):
    m = 456  # 赋值即重新定义
    n = 'hello'
    t.append(10000)
    print(xyz, m, n, t)


def fun6(a=[]):
    """
    若是 a = 'hello'，字符串是不可变类型，那么a不能就地修改，a = a + 'world'等价于 a += 'world'，a指向新的内存地址
    """
    a += [5]  # 此种方法不会重新生成列表，并不等价于 a = a + [5]，表示就地修改，即a.extend([5])


def fun7(a=[]):
    a = a + [0]  # 此种方法重新生成列表，a指向此新列表，赋值即重新定义


def main():
    fun1()  # 1
    fun1()  # 1
    fun2()  # [1]
    fun2()  # [1, 1]
    fun2.__defaults__  # ([1, 1], )查看参数缺省值，返回包含所有缺省参数的元组
    fun3()
    fun3()
    fun4('xyz')
    print(fun5.__defaults__, fun5.__kwdefaults__)  # (123,) {'n': 'abc', 't': [1, 2]}
    fun5('world')  # world 456 hello [1, 2, 10000]
    print(fun5.__defaults__, fun5.__kwdefaults__)  # (123,) {'n': 'abc', 't': [1, 2, 10000]}


if __name__ == '__main__':
    main()
