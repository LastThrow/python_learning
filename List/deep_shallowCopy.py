import copy

# 注意在python中简单数据类型的常量只有一个地址

list0 = [1, [2, 3], 4, 'abc']  # 存的等价于 [1, 101房间号码, 4, 'abc']
list1 = list0.copy()  # 浅拷贝,只是做了第一层拷贝, l1 存的等价于 [1, 房间号码, 4, 'abc']
# print(l0 == l1)  # == 仅仅比较内容是否相同，而不是引用是否相同

# 打印列表元素的地址
# print("列表list0元素的地址:", end=" ")
# for i in list0:
#     print(id(i), end=" ")
# print()
# print("列表list1元素的地址:", end=" ")
# for i in list1:
#     print(id(i), end=" ")
# print()
# # 打印列表的地址
# print("列表list0的地址:", id(list0))
# print("列表list1的地址:", id(list1))
# list0[0] = 100
# print("列表list0元素的地址:", end=" ")
# for i in list0:
#     print(id(i), end=" ")
# print()
# print("列表list1元素的地址:", end=" ")
# for i in list1:
#     print(id(i), end=" ")
# print()
# l2 = copy.deepcopy(l0)  # 深拷贝 存的等价于 [1, 500房间号码, 4, 'abc']
# # print(id(l2[1]))
# l3 = l0  # 相当于 l0 和 l3 引用同一地址

l4 = [[1, 2, 3]] * 3  # 浅拷贝l4 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]] l4内部相当于存这3个相同的门牌号码 都访问同一个房间
for i in l4[0]:
    print(i, end=" ")
l4[0][1] = 100
for i in l4[0]:
    print(i, end=" ")
