import requests
from lxml import etree
import threading
from queue import Queue
import json


class QiubaiSpider:
    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        }
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_queue = Queue()

    def get_url_list(self):
        # return [self.url_temp.format(i) for i in range(1, 14)]
        for i in range(1, 14):
            # 将所有的url放入线程队列
            self.url_queue.put(self.url_temp.format(i))

    def parse_url(self):
        while True:
            url = self.url_queue.get()  # 使得url线程队列计数加1
            res = requests.get(url, headers=self.headers)
            # return res.content.decode()
            self.html_queue.put(res.content.decode())
            self.url_queue.task_done()  # 使得url线程队列计数减1

    def get_content_list(self):
        while True:
            html_str = self.html_queue.get()
            html = etree.HTML(html_str)
            div_list = html.xpath("//div[@id='content-left']/div")
            content_list = []
            for div in div_list:
                item = {}
                item["content"] = div.xpath(".//[@class='content']/span/text()")
                item["content"] = [i.replace("\n", "") for i in item["content"]]
                content_list.append(item)
            self.content_queue.put(content_list)
            self.html_queue.task_done()

    def save_content_list(self, content_list):
        while True:
            content_list = self.content_queue.get()
            with open("qiubai.txt", "a") as fp:
                for content in content_list:
                    fp.write(json.dumps(content, ensure_ascii=False))
                    fp.write("\n")
            print("save successfully!")
            self.content_queue.task_done()

    def run(self):
        thread_list = []
        t_url = threading.Thread(target=self.get_url_list)
        thread_list.append(t_url)
        t_parse = threading.Thread(target=self.parse_url)
        thread_list.append(t_parse)
        t_html = threading.Thread(target=self.get_content_list)
        thread_list.append(t_html)
        t_save = threading.Thread(target=self.save_content_list)
        thread_list.append(t_save)
        for t in thread_list:
            # 把子线程设置为守护线程，该线程不重要，主线程结束，子线程结束
            t.setDaemon(True)
            t.start()
        for q in [self.url_queue, self.html_queue, self.content_queue]:
            q.join()  #  让主线程阻塞，等待队列任务完成，再结束


def main():
    spider = QiubaiSpider()
    spider.run()


if __name__ == '__main__':
    main()
