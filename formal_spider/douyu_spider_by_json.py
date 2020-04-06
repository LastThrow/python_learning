import requests
import json

class DouyuSpider_json():
    def __init__(self):
        self.temp_url = "https://www.douyu.com/gapi/rkc/directory/0_0/{}"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
        }
        self.part_url = "https://www.douyu.com"

    def get_json_str(self, next_url):
        print("正在请求：%s" % next_url)
        res = requests.get(next_url, headers=self.headers)
        return res.content.decode()

    def get_content_list(self, json_str):
        json_dict = json.loads(json_str)
        temp_json_list = json_dict["data"]["rl"]
        content_list = []
        for temp_json in temp_json_list:
            item = {}
            item["title"] = temp_json["rn"]
            item["category"] = temp_json["c2name"]
            item["author"] = temp_json["nn"]
            item["img"] = temp_json["rs1"]
            item["vedio_url"] = self.part_url + temp_json["url"]
            content_list.append(item)
            print(item)
        return content_list

    def save_content_list(self, content_list):
        print(content_list)
        with open("douyu_json_data.txt", "a") as fp:
            for content in content_list:
                fp.write(json.dumps(content, ensure_ascii=False))
                fp.write("\n")
        print("一页数据保存成功")

    def run(self):
        for i in range(1, 260):
            next_url = self.temp_url.format(i)
            json_str = self.get_json_str(next_url)
            content_list = self.get_content_list(json_str)
            self.save_content_list(content_list)


def main():
    spider = DouyuSpider_json()
    spider.run()


if __name__ == '__main__':
    main()
