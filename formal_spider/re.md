```python
匹配单个字符
. # 匹配任意单个字符(除了\n)，范围最广，re.findall(re.DOTALL)也可匹配\n
[] # 匹配[]中列举的字符
\d # 匹配数字，即0-9
\D # 匹配非数字
\s # 匹配空白，即空格，tab键
\S # 匹配非空白
\w # 匹配单词字符，即a-z，A-Z，0-9，_，Unicode码
\W # 匹配非单词字符

匹配多个字符
*	# 匹配前一个字符出现0次或者无限次，即可有可无
+	# 匹配前一个字符出现1次或者无限次，即至少有1次
?	# 匹配前一个字符出现1次或者0次，即要么有1次，要么没有，匹配到一次就返回结果
{m}	# 匹配前一个字符出现m次
{m,}	# 匹配前一个字符至少出现m次
{m,n}	# 匹配前一个字符出现从m到n次

关系操作符
^  # 表示开头
$  # 表示结尾
|  # 表示或
()  # 用于分组，可用group(1,2...)将()的内容取出

```

re.findall()  : 找所有，返回list

![image-20200213213353507](C:\Users\26952\AppData\Roaming\Typora\typora-user-images\image-20200213213353507.png)

从头开始匹配 : re.match()

随机找一个 : re.search()

替换：re.sub()

![image-20200213213849494](C:\Users\26952\AppData\Roaming\Typora\typora-user-images\image-20200213213849494.png)

编译：re.compile()， 提前编译，可节省时间

![image-20200213214637391](C:\Users\26952\AppData\Roaming\Typora\typora-user-images\image-20200213214637391.png)

关于re.S的编译

![image-20200213214857231](C:\Users\26952\AppData\Roaming\Typora\typora-user-images\image-20200213214857231.png)

关于原始字符串(在正则表达式中，r使得字符串表示其本身的含义)

![image-20200213215801968](C:\Users\26952\AppData\Roaming\Typora\typora-user-images\image-20200213215801968.png)

![image-20200213220147921](C:\Users\26952\AppData\Roaming\Typora\typora-user-images\image-20200213220147921.png)

