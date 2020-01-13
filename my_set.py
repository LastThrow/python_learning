def main():
    s1 = set()  # 一步到位
    # 可索引，一定可遍历，set 允许遍历，不允许索引，只要是可遍历都是可迭代对象
    # 比较内容是否相等，而不是引用地址，b'123'表示bytes类型， None为NoneType
    # 元组中不可加入不可哈希类型，即可变类型(list, dict, set, bytearray)
    # immutable class :int, float, bool, str, tuple,range, frozenset, bytes,NoneType
    s1 = {1, 2, 5, 6, 'a', 'c', 3, 2, 1, 2, 1, (1, 2), (1, 2), b'123', None}
    s1.add('abc')  # 一次只能增加一个元素
    s1.update(range(10))  # 将是s1增加为s1和range(10)的并集
    s1.update((range(10),))  # 增加一个元组
    s1.discard(1)  # 删除元素， 若不存在也不报错
    s1.remove(1)  # 删除元素，若不存在则报错KeyError
    s1.pop()  # 随机弹出一个元素
    s1.clear()  # 标记一下，此集合引用这些元素了，相应对象引用次数减1
    len(s1)  # 增加，删除的过程中自行记录的，O(1)
    # 返回bool, 通过哈希函数比对 O(1)，若在list中这样用则是一个一个比对，O(n)
    # 在set中查找元素过程：先对要查找的值求哈希值(门牌号码)，直接到房间里查找，O(1)
    a = 'abc' in s1
    b = 'abc' not in s1
    s2 = {1, 2}
    s2.issubset(s1)  # 判断是否是子集
    print(s1 & s2)  # 求s1 和 s2的交集
    print(s1 | s2)  # 求s1 和 s2的并集
    print(s1 ^ s2)  # 求s1 和 s2的对称差集，即(s1-s2)|(s2-s1)
    s1.isdisjoint(s2)  # 判断s1、s2是否有交集


if __name__ == '__main__':
    main()
