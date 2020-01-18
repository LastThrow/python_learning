import re
"""
要求：
匹配163邮箱地址，@符号前有4到20位字符，其中不包含空格换行
"""
"""
^  # 表示开头
$  # 表示结尾
|  # 表示或
()  # 用于分组，可用group(1,2...)将()的内容取出
"""


def main():
    mails = ["name1@gmail.com", "_n ame@163.com", "2_name@163..com", "__@163.com"]
    reg = r"^([a-zA-z0-9_]{4,20})@(163|126|qq|gmail)\.com$"  # "." 需要转义
    for mail in mails:
        res = re.match(reg, mail)  # ^表示开头，$表示结尾
        if res is None:
            print("变量名 %s 不符合要求" % mail)
        else:
            print("变量名 %s 符合要求" % mail)


if __name__ == '__main__':
    main()
