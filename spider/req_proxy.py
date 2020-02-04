import requests


def main():
    proxy = {
        'http': '115.239.24.140:9999'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    }
    data = {
        'u': '269524963',
        'p': 'aptx4869....slj'
    }
    res = requests.get('https://unsplash.com/', headers=headers, data=data, proxies=proxy)
    # print(res.content.decode('utf-8'))
    content = res.content
    with open('unsplash.html', 'wb') as f:
        f.write(content)


if __name__ == '__main__':
    main()
