lst1 = [11, 22]
lst2 = [1, 2]
num = 100
# 如果需要修改全局变量的地址，则需要用global
# 如果不需要修改全局变量的地址，例如列表的append，则不需要用global


def main():
    global lst1
    lst1 += [33, 44]  # lst1指向的地址空间改变，需要加global
    lst2.append(3)  # lst2指向的地址空间不变，不需要global，当然加上也不会错
    print("lst1=", lst1)
    print("lst2=", lst2)
    global num
    num += 1  # 地址改变
    print(id(num), num)


if __name__ == "__main__":
    main()

