"""
from importee import lst as li
from importee import show

print("importer------",show())
li.append(100)  # 新名字和旧名字指向同一地址空间
print("importer------",show())
li = [1,1,1,1,1,1,1]  # 改变该地址空间数据
print("importer------",show())
"""
import importee
print("importer------",importee.show())  
importee.lst.append(10000)  # 通过指明模块并修改数据
print("importer------",importee.show())
print(importee.T().__module__)