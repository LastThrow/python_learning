# 函数内部用global表示告诉当前函数，此变量是全局变量，即不在任何函数内部的变量
# 若报错，立即停止程序的执行


def outer():
    c = 1
    x = 1  # 当outer()执行完毕后，x就被销毁
    lst = [0]

    # 闭包 ：内嵌函数使用外部函数定义的局部变量，内层函数不消亡，使用到的外部函数定义的局部变量也不消亡

    def inner():  # 开一个房间，里面放着函数定义，门牌号为inner，inner的引用计数加1
        print(x)  # 可以就这样使用外层函数的本地变量，但不能修改或赋值（赋值即定义）
        nonlocal c  # nonlocal告诉当前函数，c1不是当前函数的本地变量，可以是外面某一层函数的本地变量，绝对不是global
        c = 1
        lst[0] += 1  # 不是赋值即定义，是对list内元素修改
        print(c)
        return c

    return inner  # 返回函数调用，inner的引用计数减1


def main():
    m = outer()  # 执行后，可理解为将inner的门牌号换成m
    print(m())  # 因为有闭包，执行时 c 这个列表并没有被销毁，而outer的引用计数减 1


if __name__ == '__main__':
    main()
