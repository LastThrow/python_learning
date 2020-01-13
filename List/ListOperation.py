"""
list just like the string,it has operations:
索引：[]
切片：[:]
拼接：+ , *
成员：in
长度：len()
循环：for

they also have some different operations:
list使用[]生成，元素之间用','分隔
list可以包含多种类型的对象
内容是可变的，String内容不可变
list的底层是一个数组

常用方法：
lst[0]
lst[0:3]
lst.append('hello')  # 在末尾增加元素,返回为NoneType,O(1)
lst.extend(['hello','world'])  # 在末尾增加新的列表,没有返回值，直接加在lst后面
lst.insert(3,'hello')  # 在指定位置插入元素
lst.pop(1)  # 索引一步找到，并移动元素
lst.pop()  # 移除最后一个元素
lst.count('a')  # O(n)
lst.index('a')  # 返回自第一次出现'a'的索引,无'a'时报错 , O(n)
lst.find('a')  # 返回自第一次出现'a'的索引,无'a'时返回-1
lst.remove('a')  # 从左到右查找第一个'a',并从lst中移除 , 需要遍历且移动元素,效率较低, O(n)
lst.sort()  # 按照字典序排序
lst.sort(key=len)  # len是一个内建函数，按照元素长度排序，并且改变对象本身
lst.sort(key=len,reverse=True)  # len是一个内建函数，按照元素长度逆序排序
sorted(lst,key=len)  # 按照元素长度排序，并且不改变对象本身
lst.reverse()  # 逆序，效率不高
lst.index('hello')  # 返回元素第一次在列表中出现的位置，不在则抛出异常
len(lst)  # O(1)
列表解析生成列表
lst = [i**2 for i in range(1,10)]
lst = [1,2,3,4,5]  # 列表元素在内存中连续分配内存

lst1 = lst.copy()  # lst1 和 lst 引用的不同地址空间
lst.clear()
 # 表示lst内元素在内存中的引用计数减 1，当然元素的值也可以在内存中被其他变量引用，
# 将len标记为0即可，而不是真的把元素清除回收（由gc完成）
"""


def getScore(student):
    return student[1]


# 列表解析生成列表
students = [['zhang', 99], ['wang', 90], ['li', 95]]
ave = sum(s[1] for s in students) / len(students)
# students.sort( key=getScore , reverse=True )#降序

students.sort(key=lambda s: s[1], reverse=False)  # 升序
print(students)

lst = [i for i in range(1, 9) if i % 2 == 0]
print(lst)
