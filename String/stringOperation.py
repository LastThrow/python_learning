def is_panlindrom(name):
    low = 0
    high = len(name) - 1
    while low < high:
        if name[low] != name[high]:
            return False
        low += 1
        high -= 1

    return True


def is_panlindrom_rec(name):
    if len(name) <= 1:
        return True
    else:
        if name[0] != name[-1]:
            return False
        else:
            return is_panlindrom_rec(name[1:-1])


def is_ascending(name):  # 判断字符串升序排列
    temp = name[0]

    for char in name:
        if temp > char:
            return False
        temp = char

    return True


def regularEx(name):
    import re  # the Regular Expression Module
    pattern = 'C.A'  # '.' 表示任意字符
    result = re.research(pattern, name)  # 库函数，判断name是否匹配pattern模式
    if result:
        print('Name is {}'.format(name))


def main():
    f = open('name.txt', 'r')
    for line in f:
        line = line.strip()  # 去掉开头结尾的回车空格
        if is_panlindrom_rec(line):
            print(line)
    f.close()


main()
