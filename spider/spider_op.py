import requests


def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0Mobile / 15A5341fSafari / 604.1"
    }
    # params = {
    #     "wd": "python"
    # }
    # url_temp = "http://www.baidu.com/s?"
    # url = "http://www.baidu.com/s?wd={}".format("python")
    url = "http://www.baidu.com/"
    res = requests.get(url, headers=headers)
    print(res.content.decode("utf-8"))


if __name__ == '__main__':
    main()
