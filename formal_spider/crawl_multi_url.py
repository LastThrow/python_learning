import requests
import json


class DoubanSpider:
    def __init__(self):
        self.url_temp = "https://movie.douban.com/j/search_subjects?type=tv&tag=%E5%9B%BD%E4%BA%A7%E5%89%A7&sort=recommend&page_limit=20&page_start={}"
        self.headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36"}

    def get_json_str(self, url):
        res = requests.get(url, headers=self.headers)
        return res.content.decode()

    # 此函数将json字符串转换为python数据类型dict
    def get_content_list(self, json_str):
        dict_data = json.loads(json_str)  # 转换完成后，dict_data是字典
        print("type(dict_data):", type(dict_data))
        content_list = dict_data["subjects"]  # 还是字典
        return content_list  # 返回的是一个字典，键是0，1，2，，，，19

    def save_content_list(self, content_list):
        with open("douban.txt", "a", encoding="utf-8") as fp:
            for content in content_list:
                fp.write(json.dumps(content, ensure_ascii=False))
                fp.write("\n")
        print("保存成功")

    def run(self):
        num = 0
        while True:
            url = self.url_temp.format(num)
            json_str = self.get_json_str(url)
            content_list = self.get_content_list(json_str)
            self.save_content_list(content_list)
            if len(content_list) < 20:
                break
            num += 20


def main():
    spider = DoubanSpider()
    spider.run()


if __name__ == '__main__':
    main()
