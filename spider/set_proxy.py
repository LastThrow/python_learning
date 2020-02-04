from urllib import request
import ssl


def main():
    # 不使用代理
    # 返回访问的ip
    url = 'http://httpbin.org/ip'
    res = request.urlopen(url)
    print("不使用代理返回ip：\n", res.read().decode('utf-8'))

    # 使用代理
    # 1.使用ProxyHandler传入代理，构建一个handler
    handler = request.ProxyHandler({'http': "111.72.25.191:9999"})
    # 2.使用handler构建一个opener
    opener = request.build_opener(handler)
    # 3.使用open()发送请求
    res = opener.open(url)
    print("使用代理返回ip：\n",res.read().decode('utf-8'))


if __name__ == '__main__':
    main()
