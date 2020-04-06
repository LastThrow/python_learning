import requests


class TiebaSpider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = "https://tieba.baidu.com/f?ie=utf-8&kw=" + tieba_name + "&pn={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36"
        }

    def get_url_list(self):
        url_list = []
        for i in range(5):
            url_list.append(self.url_temp.format(i * 50))
        return url_list

    def get_url_content(self, url):
        res = requests.get(url, headers=self.headers)
        # 将cookie转换为字典
        # requests.utils.dict_from_cookiejar(res.cookies)
        return res.content

    def save_html(self, html_bytes, page_num):
        file_path = "{}-第{}页.html".format(self.tieba_name, page_num)
        with open(file_path, "wb") as f:
            f.write(html_bytes)

    def run(self):
        url_list = self.get_url_list()
        for url in url_list:
            html_bytes = self.get_url_content(url)
            page_num = url_list.index(url) + 1
            print("正在爬取第%s页..." % page_num)
            self.save_html(html_bytes, page_num)


def main():
    spider = TiebaSpider("李毅")
    spider.run()


if __name__ == '__main__':
    main()
