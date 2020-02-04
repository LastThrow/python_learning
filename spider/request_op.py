import requests


def main():
    res = requests.get('http://www.baidu.com')
    # print(res.text)  # reuqest会根据自己猜测的解码方式进行解码，所以大部分时候我们看到的是乱码
    # print(res.content.decode('utf-8'))  # content是直接从网上抓取的数据，没有任何的解码，是byte类型，
    # 查看访问的完整url
    print(res.url)
    # 查看响应头部的编码
    print(res.encoding)
    print(res.status_code)
    # params = {
    #     'wd': '中国'
    # }
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    # }
    # res = requests.get('http://www.baidu.com/s', params=params)
    with open('china.html', 'w', encoding='utf-8') as f:
        f.write(res.content.decode('utf-8'))
    print(res.url)  # 底层自动拼接url

    # 下面使用代理


if __name__ == '__main__':
    main()
