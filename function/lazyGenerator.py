def main():
    lazyGenerator = (x for x in range(10))  # 惰性生成器，只提供一次迭代，迭代完成则清空
    result = 0
    for x in lazyGenerator:  # 但是用for循环可以迭代多次
        result += x
    print(max(lazyGenerator))
    print(min(lazyGenerator))  # 错误，只能迭代一次


if __name__ == '__main__':
    main()
