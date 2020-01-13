# String Operation
"""
x+y     n*x     x in s
lower() upper()
split()

计算字串son在str中出现的次数
str.count(son)

替换字符串
str.replace(old,new)  # 返回新的字符串

宽度为width，将str居中，用fillChar填充
str.center(width[,fillChar])

将str头尾出现的char1,char2,...都删除
str.strip(char1,char2,...)

用尽可能多地空格切割字符串，并返回list
str.split()

将str插入到iter的每个元素之间
str.join(iter)

字符串的比较是对齐了一个一个比较ASCII码，'10' > '2' 返回 False
"""

a = "1234567890"
# 从0-9，步长为2
print(a[0:9:2], "\n")
# 负数表示从前往后取
# 缺省分别表示至开头和结尾
print(a[::-2])
b = "abc"
print(b+"6and9")  # 并不改变b
print(b, end='#')  # end改变print打印出的最后一个字符
# str() 和 eval()有相反的功能
print(ord('m'))  # 返回Unicode编码

print(chr(10004))  # 返回Unicode编码对应的字符
for i in range(12):
    print("星座表示符：{}".format(chr(9800 + i)))  # print自带换行
c = "YUUYUIyuiHK"
d = "abc"
print(" ".join(d))
#  槽
print("{1}{2}{0}".format("a","b","c"))
print("{0:=^20}".format("python"))
print("{0:=>20}".format("python"))
print("{0:=<20}".format("python"))

