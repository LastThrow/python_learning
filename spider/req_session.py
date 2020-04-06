import requests
"""
使用requests请求登录后网页的思路：
实例化session
先使用session发送请求，登录网站，把cookie保存在session中
再使用session请求登录后的网站，session能够自动携带登录成功时保存在其中的cookie进行请求
"""


def str_to_dict(cookies_str):
    cookies_dist = {i.split("=")[0]: i.split("=")[1] for i in cookies_str.split("; ")}
    return cookies_dist


def main():
    session = requests.Session()
    login_url = 'http://www.renren.com/PLogin.do'
    data = {
        "email": '269524963@qq.com',
        "password": 'aptx4869..slj'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36',
    }

    # cookie: 'anonymid=k67hxshe-1vtmfm; _r01_=1; taihe_bi_sdk_uid=b9aa06bdb29d4e402a8209714fddbd5d; depovince=ZGQT; JSESSIONID=abcX7vNjbqDJ2azTEj0ax; taihe_bi_sdk_session=511521bb980dcaa60043c170a7574553; ick_login=69707d7d-c636-40ed-ae71-046562d5ce52; id=973614509; ver=7.0; loginfrom=null; wp_fold=0; ick=f3ada514-d0de-4116-8ef8-e2670631bb99; t=42f97870e5d5a5a25df456e4dc544a2f9; societyguester=42f97870e5d5a5a25df456e4dc544a2f9; xnsid=cbd32a1b; jebecookies=a3680de3-1307-4c64-add7-aac74d259129|||||'
    # cookie = str_to_dict(cookie)
    # res = session.get(url=profile_url, headers=headers, cookies=cookies)

    # 使用session发送请求，将cookie保存在其中
    session.post(url=login_url, data=data, headers=headers)
    # 在同一次会话中共享cookie，后面直接打开个人主页
    profile_url = 'http://www.renren.com/973614509/newsfeed/photo'
    res = session.get(url=profile_url, headers=headers)
    with open('profile.html', 'w', encoding='utf-8') as f:
        f.write(res.content.decode('utf-8'))


if __name__ == '__main__':
    main()
