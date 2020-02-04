import requests


def main():
    url = 'https://www.lagou.com/jobs/companyAjax.json?needAddtionalResult=false'
    data = {
        'first': 'true',
        'pn': 1,
        'kd': 'Python'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'Referer': 'https://www.lagou.com/zhaopin/Python/?labelWords=label'
    }
    res = requests.post(url=url, data=data, headers=headers)
    print(res.json())  # 将返回的字符串转换成字典形式，返回dict
    print(res.text)


if __name__ == '__main__':
    main()
