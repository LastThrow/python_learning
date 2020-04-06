import requests


def main():
    proxies = {
        "http": "117.131.119.116:80",
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36"
    }
    url = "http://www.taobao.com"
    res = requests.get(url, proxies=proxies, headers=headers)
    print(res.content.decode("utf-8"))


if __name__ == '__main__':
    main()
