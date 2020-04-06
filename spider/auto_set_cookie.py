from urllib import request
from urllib import parse
from http.cookiejar import CookieJar


def get_opener():
    # 创建一个cookiejar对象，可保存服务器发送的cookie，下次自动登录
    cookiejar = CookieJar()
    # 使用cookiejar创建一个HTTPCookieProcessor对象
    handler = request.HTTPCookieProcessor(cookiejar)
    # 使用handler创建一个opener
    opener = request.build_opener(handler)
    return opener


def login(opener, login_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/79.0.3945.130 Safari/537.36',
    }
    data = {
        'u': '269524963',
        'p': 'aptx4869....slj'
    }

    req = request.Request(login_url, data=parse.urlencode(data).encode('utf-8'), headers=headers)
    opener.open(req)
    res = opener.open(req)


def visit_profile(opener, profile_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/79.0.3945.130 Safari/537.36',
    }
    req = request.Request(profile_url, headers=headers)
    res = opener.open(req)
    content = res.read()
    with open('profile.html', 'wb') as f:
        f.write(content)


def main():
    opener = get_opener()
    login_url = 'https://qzone.qq.com/'
    login(opener, login_url)
    profile_url = 'https://user.qzone.qq.com/269524963'
    visit_profile(opener, profile_url)


if __name__ == '__main__':
    main()
