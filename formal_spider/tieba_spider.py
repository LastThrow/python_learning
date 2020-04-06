import requests
from lxml import etree
import json


class TiebaSpider:
    def __init__(self, tieba_name):
        self.session = requests.session()
        self.tieba_name = tieba_name
        self.start_url = "https://tieba.baidu.com/f?kw="+tieba_name+"&fr=ala0&tpl=5"
        self.headers = {
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        }
        self.part_url = "https://tieba.baidu.com/"

    def get_html(self, url):
        print("**********正在请求:", url)
        res = self.session.get(url, headers=self.headers)
        return res.content

    def get_content_list(self, html_str):
        html_element = etree.HTML(html_str)
        # 获取到包含每一个帖子所有内容的div，因为爬取的内容带有注释，难以爬取
        div_list = html_element.xpath("//li[contains(@class, 'j_thread_list')]")
        print("-"*20,div_list)
        content_list = []
        # 从所有内容中获取想要的内容
        for div in div_list:
            item = {}
            item["title"] = div.xpath(".//a[@class='j_th_tit']/@title")[0] if len(div.xpath(".//a[@class='j_th_tit']/@title"))>0 else None
            item["text"] = div.xpath(".//a[@class='j_th_tit']/text()")[0] if len(div.xpath(".//a[@class='j_th_tit']/text()"))>0 else None
            item["href"] = self.part_url + div.xpath(".//a[@class='j_th_tit']/@href")[0] if len(div.xpath(".//a[@class='j_th_tit']/@href"))>0 else None
            item["img_list"] = self.get_post_imgs(item["href"], [])
            item["img_list"] = [ requests.utils.unquote(i).split("src=")[-1] for i in item["img_list"]]
            content_list.append(item)
        next_url = html_element.xpath("//a[text()='下一页>']")[0] if len(html_element.xpath("//a[text()='下一页>']"))>0 else None
        print("-----in get_content_list --------- next_url : ", next_url)
        return content_list, next_url

    def get_post_imgs(self, post_url, total_imgs):
        post_html_str = self.get_html(post_url)
        # 修正获取到的html字符串，并转为element对象
        post_html_element = etree.HTML(post_html_str)
        img_list = post_html_element.xpath("//img[@class=\"BDE_Image\"]/@src")
        total_imgs.extend(img_list)
        post_next_url = post_html_element.xpath("//a[text()='下一页']/@href")
        if len(post_next_url) > 0:
            post_next_url = post_next_url[0]
            print("-----in get_post_imgs----post_next_url--- : ", post_next_url)
            return self.get_post_imgs(post_next_url, total_imgs)
        return total_imgs

    def save_content_list(self, content_list):
        file_path = self.tieba_name + ".txt"
        with open(file_path, "a") as fp:  # encoding="utf-8"
            for content in content_list:
                fp.write(json.dumps(content, ensure_ascii=False, indent=2))
                fp.write("\n")
        print("保存成功")

    def run(self):
        next_url = self.start_url
        while next_url is not None:
            html_str = self.get_html(next_url)
            content_list, next_url = self.get_content_list(html_str)
            self.save_content_list(content_list)


def main():
    spider = TiebaSpider("李毅")
    spider.run()


if __name__ == '__main__':
    main()
