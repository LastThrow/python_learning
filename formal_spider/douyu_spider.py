import requests
from selenium import webdriver
import json


class DouyuSpider():
    def __init__(self):
        self.start_url = "https://www.douyu.com/directory/all"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
        }
        self.part_url = "https://www.douyu.com"
        self.driver = webdriver.Chrome()

    def get_html_str(self, next_url):
        res = requests.get(next_url, headers=self.headers)
        return res.content.decode()

    def get_content_list(self):
        li_list = self.driver.find_elements_by_xpath("//div[@class='layout-Module-container layout-Cover ListContent']/ul/li")
        content_list = []
        for li in li_list:
            item = {}
            item["title"] = li.find_element_by_xpath(".//h3").text
            item["category"] = li.find_element_by_xpath(".//span[@class='DyListCover-zone']").text
            item["author"] = li.find_element_by_xpath(".//h2").text
            item["audience"] = li.find_element_by_xpath(".//span[@class='DyListCover-hot is-template']").text
            item["img"] = li.find_element_by_xpath(".//img[@class='DyImg-content is-normal']").get_attribute("src")
            item["vedio_url"] = self.part_url + li.find_element_by_xpath(".//div/a").get_attribute("href")
            content_list.append(item)
            print(item)
        # 从上面那个url获取的html没有下一页的href，无奈，只能爬取json
        next_url = self.driver.find_elements_by_xpath("//li[@title='下一页']/span[@class='dy-Pagination-item-custom']")
        print("next_url:",next_url)
        next_url = next_url[0] if len(next_url)>0 else None
        return content_list, next_url

    def save_content_list(self, content_list):
        print(content_list)
        with open("douyu_data.txt", "a") as fp:
            for content in content_list:
                fp.write(json.dumps(content, ensure_ascii=False))
                fp.write("\n")
        print("一页数据保存成功")

    def run(self):
        self.driver.get(self.start_url)
        content_list, next_url = self.get_content_list()
        self.save_content_list(content_list)
        while next_url is not None:
            time.sleep(3)
            next_url.click()
            content_list, next_url = self.get_content_list()
            self.save_content_list(content_list)


def main():
    spider = DouyuSpider()
    spider.run()


if __name__ == '__main__':
    main()
