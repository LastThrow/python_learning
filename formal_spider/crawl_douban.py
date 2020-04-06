import json
import requests
from pprint import pprint


def main():
    proxies = {
        "http": "113.194.28.88:9999",
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36",
        "Referer": "https://m.douban.com/movie/",
        "Accept": "*/*",
    }
    session = requests.Session()
    session.get(url="https://movie.douban.com/", headers=headers)
    cookie = session.cookies
    url = "https://m.douban.com/rexxar/api/v2/movie/modules?need_manual_chart_card=1&for_mobile=1"
    res = requests.get(url=url, proxies=proxies, cookies=cookie, headers=headers)
    data_str = res.content.decode("unicode_escape")
    data_dict = json.loads(data_str)  # loads：json字符串------>python数据类型
    print(data_dict)
    print(type(data_dict))
    print("*" * 100)
    with open("douban2.json", "w", encoding="utf-8") as f:  # encoding表示打开文件方式
        # ensure_ascii=False表示让中文显示，indent表示缩进
        # json.dumps()  python数据类型------>json字符串
        f.write(json.dumps(data_dict, ensure_ascii=False, indent=4))

    with open("douban2.json", "r", encoding="utf-8") as f:
        ret1 = f.read()
        ret2 = json.loads(ret1, encoding='utf-8')
        # json字符串 json.loads() ------> python数据类型
        pprint(ret2)
        pprint(type(ret2))


if __name__ == '__main__':
    main()
