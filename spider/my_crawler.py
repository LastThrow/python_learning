from urllib import request
from urllib import parse


def main():
    res = request.urlopen('http://www.baidu.com')
    # print(res)  # 返回类文件对象http.client.HTTPResponse
    # print(res.read().decode('utf-8'))
    # print(res.readline())  # 返回bytes
    # print(res.readlines())  # 返回list
    # print(res.getcode())  # 返回int状态码
    # print(res.geturl())
    # res.close()

    """urlretrieve"""
    # request.urlretrieve('http://www.baidu.com', r'C:\baidu.html')  # 爬取源码并保存
    # request.urlretrieve('https://images.unsplash.com/photo-1579102298128-754755f6087b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=600&q=60','1.jpg')  # 爬取图片并保存

    """parse.urlencode()"""
    # params = {'name':'刘德华', 'age':18, 'greet':'hello'}
    # result = parse.urlencode(params)
    # print("编码结果：\n",result)

    # url = 'https://www.baidu.com/s?wd=刘德华'  # 报错，请求时无法ASCII码对中文编码
    # url = 'https://www.baidu.com/s?wd=%E5%88%98%E5%BE%B7%E5%8D%8E'
    # print('解码结果：', parse.unquote(url))

    # params = {'wd':'刘德华'}
    # qs = parse.urlencode(params)
    # url = 'https://www.baidu.com/s'
    # url = url + '?' + qs
    # res = request.urlopen(url)
    # print(res.getcode())

    """parse_qs"""
    # params = {'name':'刘德华', 'age':18, 'greet':'hello'}
    # qs = parse.urlencode(params)
    # print("将字典转换为请求参数格式：\n", qs)
    # res = parse.parse_qs(qs)
    # print("将请求参数转换成字典格式：\n", res)

    """urlparse  urlsplit"""
    # url = 'https://www.baidu.com/s;hello?wd=python&username=shen#1'
    # res1 = parse.urlparse(url)  # 多一个params属性，一般用的比较少
    # res2 = parse.urlsplit(url)
    # print(res1)  # urllib.parse.ParseResult
    # print(res2)


    url = 'https://www.lagou.com/message/newMessageList.json'
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'Referer': 'https://www.lagou.com/zhaopin/Python/?labelWords=label'
    }
    data = {
        'first': 'true',
        'pn': 1,
        'kd': 'Python'
    }
    req = request.Request(url, headers=headers, data=parse.urlencode(data).encode('utf-8'), method='POST')
    res = request.urlopen(req)
    content = res.read()
    with open('1.html', 'wb') as f:
        f.write(content)


if __name__ == '__main__':
    main()
