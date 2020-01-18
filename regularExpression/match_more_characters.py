"""
*	匹配前一个字符出现0次或者无限次，即可有可无
+	匹配前一个字符出现1次或者无限次，即至少有1次
?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
{m}	匹配前一个字符出现m次
{m,}	匹配前一个字符至少出现m次
{m,n}	匹配前一个字符出现从m到n次
"""
import re


def main():
    try:
        print(re.match(r"\d{1,3}", "133").group())  # {}可用来约束前面紧挨着的那个有多少位，即11个\d
        print(re.match(r"130-?\d{8}", "130-10101010").group())
        print(re.match(r"\d{3,4}-?\d{7,8}", "130-10101010").group())
        print(re.match(r"\d{3,4}-?\d{7,8}", "130-1010101").group())
        html_content = "312\n312\n4324125"
        print(re.match(r".*", html_content, re.S).group())  # 强行使得"."匹配上\n
        print(re.match(r".+","").group())  # 异常，+表示至少有一个字符
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()
