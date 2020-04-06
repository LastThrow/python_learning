import requests
import json


class BaiduTrans:
    def __init__(self, trans_str):
        self.trans_str = trans_str
        self.lang_detect_url = "https://fanyi.baidu.com/langdetect"
        self.headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36"}
        self.trans_url = "https://fanyi.baidu.com/basetrans"

    def parse_url(self, url, data):
        res = requests.post(url, data=data, headers=self.headers)
        return json.loads(res.content.decode())

    def get_res(self, dict_res):
        res = dict_res["trans"][0]["dst"]
        print("结果：", res)

    def run(self):
        lang_detect_data = {"query": self.trans_str}
        # 获取语言类型
        lang = self.parse_url(self.lang_detect_url, lang_detect_data)["lan"]
        # 准备post数据
        trans_data = {"query": self.trans_str, "from":"zh", "to":"en"} if lang=="zh" else {"query": self.trans_str, "from":"en", "to":"zh"}
        dict_res = self.parse_url(self.trans_url, trans_data)
        self.get_res(dict_res)


def main():
    my_str = input("输入：")
    bf = BaiduTrans(my_str)
    bf.run()


if __name__ == '__main__':
    main()
