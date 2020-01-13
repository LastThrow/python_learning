def ins_sort(lst):
    # 从下标为1的元素开始向前插入
    for i in range(1, len(lst)):
        # 从第i个元素开始，若小于前一个元素，则交换位置
        # j一直指向待处理的元素(同一元素)
        for j in range(i, 0, -1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
    return lst


def main():
    lst = [4, 1, 2354, 51, 5, 45, 1, 51, 5, 25]
    lst = ins_sort(lst)
    print(lst)


if __name__ == '__main__':
    main()
