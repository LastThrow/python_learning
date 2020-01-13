"""
实参：可变位置参数 和 可变关键字参数 ， 注意带等号的往后靠
形参：可变位置参数 :*args(尽可能多地收集所有的位置参数) , 可变关键字参数 : **kwargs , **kwargs 在 *args 后
def fun(*args , x):  # x只能用keyword传参
    pass
缺省参数是给不允许为空的参数的，*args和**kwargs可以为空，不允许给缺省参数
当函数返回多个返回值的时候，返回值的类型是 tuple
"""


def my_sum1(iteration):
    result = 0
    for x in iteration:
        result += x
    return result


def my_sum2(*iteration):  # 可变位置参数 ，将多个参数封装到一个名为iteration的tuple
    print(type(iteration), iteration)  # type为tuple，不可变
    result = 0
    for x in iteration:
        result += x
    return result


def showconfig(**kwargs):  # 可变关键字参数 ，将键值对封装到一个名字为kwargs的dict
    print(type(kwargs), kwargs)


def show1(username, password, *args, **kwargs):  # 注意，跟位置参数相关的往前写，跟关键字相关的参数往后写
    pass


def fun(x, y, *, z, **kwargs):  # z只能是keyword-only
    pass


def add(x, y):
    print(x + y)
    return x + y


def main():
    print(my_sum1({100: 1, 200: 2}))  # 此处用key进行迭代
    print(my_sum2(1, 2, 3, 4, 5))
    print(my_sum2(*range(10)))
    showconfig(a=1, b=2)
    # 参数解构， 必须在传实参的时候使用
    add(*[4, 5])
    add(*(4, 5))
    add(*{4, 5})
    add(*range(4, 6))
    t = [4, 5]
    add(*t)
    add(*{'a': 1, 'b': 2})  # 'ab'
    add(**{'x': 1, 'y': 2})  # 3 , 等价于add(x=1, y=2), 双星号解构必须是用于dict
    add(*{'a': 1, 'b': 2}.values())  # 3
    # {'a': 1, 'b': 2}.items()返回[('a',1),('b',2)] ,解构后变成('a',1),('b',2)两个参数，相加后变成('a',1,'b',2)
    add(*{'a': 1, 'b': 2}.items())


if __name__ == '__main__':
    main()
