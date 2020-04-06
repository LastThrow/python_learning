**选择属性** : @
**获取a标签下的文本** ：a/text()
**获取a标签下的所有文本** ： a//text()
**根据节点关系选择内容** ： /html/head/meta/@content
**//p** : 获取整个html中的p标签内容
**//ul[@id="detail-list"]/li**  : 选中id为detail-list的ul标签下的li
**//ul[@id="detail-list"]/li//h1/p** : 选取指定li下的所有h1标签中的p 

#### 豆瓣案例
**获取所有图片的地址**：//div[@class="indent"]//table//a[@class="nbg"]//img/@src
**获取所有评价人数**：//div[@class="indent"]//table//span[@class="pl"]/text()

#### 百度案例
**获取所有下一页的地址**：//article[@id="bds-pages"]//a/@href
**根据文本进行定位** ： //a[text()="下一页>"]
**仅仅获取a标签下的文本(a标签内部的<em>标签下的文本获取不到)**：//div[@id="7"]/h3/a/text()
**获取a标签下的所有文本，内部节点的文本也可获取** ： div[@id="7"]/h3/a//text()
**获取第3个a标签** ： //div[@id="page"]//a[3]
**获取倒数第3个a标签** ： //div[@id="page"]//a[last()-2]
**获取前3个a标签** ： //div[@id="page"]//a[position()<4]
**获取a标签下子节点的文本大于4的标签**  ： //div[@id="page"]//a[span/text()>4]
**获取a标签下子节点大于4的标签(应该是默认取text())**  ： //div[@id="page"]//a[span>4]
**| 或的用法** : //div[@id="page"]//a[span=3]|//div[@id="page"]//a[last()-1]
**包含** : //div[contains(@class, 'i')]

使用XPath helper或者chrome中的copy xpath都是从element中提取的数据
但是爬虫获取的是url的响应，往往和element不同

lxml使用注意点
lxml可能会将html修改错误，使用etree.tostring()方法观察修改后的代码再使用
lxml可接受bytes和str类型的数据

提取页面数据的分组
1、先分组，取到一个包含分组标签的列表
2、遍历，取其中每一组进行数据提取，不会造成数据的对应错乱

### 爬虫的套路：

1、准备url

- 准备start_url
  - url规律不明显，总数不确定
  - 通过XPath提取下一页的url
  - js生成，需要寻找
- 准备url_list
  - 页码总数明确
  - url地址规律明显

2、发送请求，提取响应

- 添加随机的User-Agent，进行反 反爬虫
- 添加随机的代理ip，进行反发 发爬虫
- 在对方判断出爬虫访问后，应该添加更多的headers字段，包括cookie，可使用session解决
- 准备cookie池：将前几次的cookie保存在自己的cookie池，后期取出来用。
  - 不登录时，将res中cookie转换为dict保存：requests.utils.dict_from_cookiejar(res.cookies)
  - 登录时，准备多个账号，只用程序获取每个账号的cookie。之后随机选择cookie请求登录后才能访问的网站

3、获取数据

- 确定数据的位置
  - 若数据在当前的url地址中
    - 提取的是列表页中的数据：直接请求列表页的url地址
    - 提取的是详情页中的数据：确定url、发送请求、提取数据、返回
  - 若数据不在当前的url地址中
    - 可能在其他响应数据包中
      - 1、从network中寻找，或者使用过滤工具(不勾选js、css)
      - 2、使用search(不准确)，可以搜索数字和英文

- 提取数据
  - xpath：从html代码中提取整块数据，先分组，再挨个提取
  - json：loads()、dumps()
  - re：

4、保存

- 保存在本地，txt、csv、json
- 保存在数据库，mongodb，mysql


爬取的时候尽量爬取手机版或极速版，手机版可能返回json数据
伪装：动态User-Agent，代理ip，适当使用cookie
所线程爬取