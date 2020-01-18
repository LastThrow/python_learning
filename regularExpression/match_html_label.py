import re

"""
|  # 表示或，匹配左右任意一个表达式
()  # 括号中字符作为分组，可用group(1,2...)将()的内容取出
\num  # 引用分组num匹配到的字符串
(?P<name>)  # 给分组起别名
(?P=name)  # 引用别名为name分组匹配的字符串 
"""


def main():
    labels = ["<html><body>哈哈哈哈</body></html>"]
    reg = r"^<(?P<p1>\w*)><(?P<p2>\w*)>\w*</(?P=p2)></(?P=p1)>$"
    for label in labels:
        res = re.match(reg, label)  # ^表示开头，$表示结尾
        if res is None:
            print(" %s 不符合要求" % label)
        else:
            print(" %s 符合要求" % label)


if __name__ == '__main__':
    main()
