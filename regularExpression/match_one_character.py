"""
. # 匹配任意单个字符(除了\n)，范围最广
[] # 匹配[]中列举的字符
\d # 匹配数字，即0-9
\D # 匹配非数字
\s # 匹配空白，即空格，tab键
\S # 匹配非空白
\w # 匹配单词字符，即a-z，A-Z，0-9，_，Unicode码
\W # 匹配非单词字符
"""
import re


def main():
    try:
        print(re.match(r"速度[1-26-8]", "速度1").group())
        print(re.match(r"速度\d", "速度1").group())
        print(re.match(r"速度[1-8a-dA-D]", "速度C").group())
        print(re.match(r"速度\w", "速度哈哈").group())  # \w包括变量命名规范的字符，Unicode码
        print(re.match(r"速度\s\d", "速度\t3").group())
        print(re.match(r"速度.", "速度213").group())
        print(re.match(r"速度[12678]", "速度3").group())  # 匹配不了，产生异常
    except Exception:
        pass


if __name__ == '__main__':
    main()
