"""
^  # 在[]外表示开头，在[]内表示取反
$  # 表示结尾
"""
import re


def main():
    names = ["name1", "_n ame", "2_name", "__name__"]
    for name in names:
        res = re.match(r"^[a-zA-z_][a-zA-z0-9_]*$",name)  # ^表示开头，$表示结尾
        if res is None:
            print("变量名 %s 不符合要求" % name)
        else:
            print("变量名 %s 符合要求" % name)


if __name__ == '__main__':
    main()
