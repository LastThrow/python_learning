str = "12345"
print(str[:-1])  # 加上数字表示前闭后开
print(str[:])  # 不加数字表示至开头和至结尾
str1, str2 = "123", "124"
a, b = 3, 2  # 真是开了眼界
print(str1, str2, a, b)
for i in range(1,10,2):
    print(i)
list = ['python','java','c/c++']
for i in list:  # java中的for each
    print(i)

while a > 0:
    a -= 1
    print(a)
print(str, end="\n")  # 在最后输出换行
