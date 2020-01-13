lst1 = [11, 22]
lst2 = [1 ,2]


def main():
    global lst1
    lst1 += [33, 44]  # lst1指向的地址空间改变，需要加global
    lst2.append(3)  # lst2指向的地址空间不变，不需要global，当然加上也不会错
    print("lst1=", lst1)
    print("lst2=", lst2)


if __name__ == "__main__":
    main()

