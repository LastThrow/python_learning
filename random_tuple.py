import random
from collections import namedtuple


random.randrange(1, 10)  # [1,10)
random.randint(1, 10)  # [1,10]
lst = list(range(1, 10))
for i in range(10):
    print(random.choice(lst))  # 从列表随机选择一个数字

random.shuffle(lst)  # 随机打乱lst

random.sample(lst, 5)  # 从样本空间取5个值，但不会把同一个值取两次 ， 返回类型为list

# 可理解为只读list
t6 = (1, [1, 2], '321', None)  # tuple为不可变对象，但是可以执行切片操作 ， 门牌号码不允许改变，但里面的list可以改变
t6[1][0] = 10  # 可以改变房间内部数据，房间引用的地址不变
t6.count([1, 2])  # 返回[1,2]出现的次数


Student = namedtuple('s', 'name, age')  # Student是标识符(程序员使用)，s是名字,Student是tuple的子类
student1 = Student('tom', 10)
student2 = Student('tim', 11)
