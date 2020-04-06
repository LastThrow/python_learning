json在数据交换中起到载体的作用，承载着传递的数据

json字符串---json.loads()--->python数据类型
python数据类型---json.dumps()--->json字符串
```python
data_str = res.content.decode("unicode_escape")
data_dict = json.loads(data_str)

with open("douban2.json", "w", encoding="utf-8") as f:  # encoding表示打开文件方式
    # ensure_ascii=False表示让中文显示，indent表示缩进
    # json.dumps()  python数据类型------>json字符串
    f.write(json.dumps(data_dict, ensure_ascii=False, indent=4))
```


包含json的类文件对象---json.load()--->python数据类型
python数据类型---json.dump()--->包含json的类文件对象

```python
with open("douban.json", "r", encoding="utf-8") as f:
    data_dict = json.load(f)

with open("douban.json", "w", encoding="utf-8") as f:
    json.dump(data_dict, f, ensure_ascii=False, indent=2)
    # 其中data_dict表示python数据类型，可以是dict  
```
如何获取json：json的url可以使用手机版页面获取

json中的字符串都是用双引号引起来的
    若不是双引号
    eval：可实现简单的字符串和python类型的转换
    replace：把单引号替换为双引号

往一个文件写入多个json串，不再是一个json串，不可直接读取
一行写一个json串，按照行读取，或者更改获取的数据区间


