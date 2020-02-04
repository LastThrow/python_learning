from urllib import request
from http.cookiejar import MozillaCookieJar


def main():
    # 创建一个cookiejar对象，可保存服务器发送的cookie，下次自动登录
    cookiejar = MozillaCookieJar('cookie.txt')
    # 从文件动态加载保存的cookies，ignore_discard=True表示同样加载过期的cookie
    cookiejar.load(ignore_discard=True)
    # 使用cookiejar创建一个HTTPCookieProcessor对象
    handler = request.HTTPCookieProcessor(cookiejar)
    # 使用handler创建一个opener
    opener = request.build_opener(handler)
    res = opener.open('http://httpbin.org/cookies')
    # ignore_discard = True表示同样加载过期的cookie
    # cookiejar.save(ignore_discard=True)
    for cookie in cookiejar:
        print(cookie)


if __name__ == '__main__':
    main()
