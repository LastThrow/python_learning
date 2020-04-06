import requests
import json
import sys


def main():
    query_str = input("翻译：")
    # query_str = sys.argv[1]
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36"
    }
    data = {
        "from": "zh",
        "to": "en",
        'query': query_str,
    }
    post_url = "https://fanyi.baidu.com/v2transapi?from=zh&to=en"  # 请求网址找不到
    res = requests.post(post_url, data=data, headers=headers)
    print(res.content.decode("utf-8"))
    dict_ret = json.loads(res.content.decode())  # 加载json字符串，返回字典
    ret = dict_ret["trans"][0]["dst"]


if __name__ == '__main__':
    main()
