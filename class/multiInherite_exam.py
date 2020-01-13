class Parent(object):
    x = 1


class Child1(Parent):  # 继承不是复制
    pass


class Child2(Parent):
    pass


print(Parent.x, Child1.x, Child2.x)  # 1 1 1
# 以上打印时其实Child1和Child2中是没有x属性的，自己没有就到父类里面找，所以结果是1 1 1
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)  # 1 2 1
# 以上打印时Child2中是没有x属性的，自己没有就到父类里面找，而Child1自己有x属性，所以结果是1 2 1
Parent.x = 3
# 同样的，Child2中是没有x属性，到父类里面找，而Child1自己有x属性，所以结果为3 2 3
print(Parent.x, Child1.x, Child2.x)  # 3 2 3

