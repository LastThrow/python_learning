from lxml import etree


def main():
    text = """
    <nav id="nav" class="clearfix">
        <div class="clearfix">
        <div class="nav_com">
            <ul>
                <li class="active"><a>推荐</a></li>                                                               
                <li class=""><a href="/nav/watchers">动态</a></li>        
                <li class=""><a href="/nav/career">程序人生</a></li>               
                <li class=""><a href="/nav/python">Python</a></li>                
                <li class=""><a href="/nav/java">Java</a></li>
            </ul>
        </div>
        </div>
    </nav>
"""
    # 此方法可以自动修正html代码，补全标签等
    html = etree.HTML(text)
    # print(etree.tostring(html, encoding="utf-8").decode("utf-8"))
    # 获取所有的href
    href_res = html.xpath("//ul//li//a/@href")
    # 获取所有的文本
    text_res = html.xpath("//ul//li//a/text()")
    # 把href和文本组成字典
    # for i in range(len(href_res)):
    #     dic = {}
    #     dic["title"] = text_res[i]
    #     dic["href"] = href_res[i]
    #     print(dic)
    # 当某个a标签下没有href时，上述方法会对应错误
    res = html.xpath("//ul//li")
    for i in res:
        dic = {
            "title": i.xpath("./a/text()")[0] if len(i.xpath("./a/text()")) > 0 else None,
            "href": i.xpath("./a/@href")[0] if len(i.xpath("./a/@href")) > 0 else None
        }
        print(dic)


if __name__ == '__main__':
    main()
