"""
xx : 共有变量
_xx : 单前置下划线，私有化属性或方法，from module import * 禁止导入，类对象和子类可以访问，只在本模块中使用，别的模块无法访问
__xx : 双前置下划线，私有的，避免与子类中的属性命名冲突，无法在外部直接访问(名字重整所以访问不到)
__xx__ : 双前后下划线，用户名字空间的魔法对象或属性，不要自己定义这样的名字
xx_ : 单后置下划线，用于避免与python关键词冲突

import导入方法：
import xxx as XXX  # 起别名，防止导入的module与变量重名
from xxx import new_name  # 只是在本地定义了一个同名局部变量，指向与xxx模块中变量指向的同一地址
import xxx


有aa.py main.py
import aa.py
aa.test()  # 输出
此时另一个进程修改了aa.py里的test函数后，再去执行aa.test()输出依然不变
from imp import reload
reload(aa)  # 重新加载aa模块
aa.test()  # 此时输出改变
"""
