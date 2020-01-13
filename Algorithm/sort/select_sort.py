def sel_sort(lst):
    for i in range(len(lst)-1):
        min_index = i
        for j in range(i+1, len(lst)):  # 在下标为i+1到len(lst)-1之间的元素之间找到最小元素的下标
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]  # 最小元素与当前元素交换，然后当前元素后移


def main():
    lst = [4, 1, 2354, 51, 5, 45, 1, 51, 5, 25]
    sel_sort(lst)
    print(lst)


if __name__ == '__main__':
    main()
