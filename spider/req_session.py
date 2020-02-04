import requests


def main():
    login_url = 'https://qzone.qq.com/'
    data = {
        "u": '269524963',
        "p": 'aptx4869....slj'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    }
    session = requests.Session()
    session.post(url=login_url, data=data, headers=headers)
    # 在同一次会话中共享cookie，后面直接打开就行
    profile_url = 'https://user.qzone.qq.com/269524963'
    res = session.get(url=profile_url)
    with open('profile.html', 'w', encoding='utf-8') as f:
        f.write(res.content.decode('utf-8'))


if __name__ == '__main__':
    main()
