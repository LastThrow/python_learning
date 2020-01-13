'''
my_dict = {'John':15091524337 , 'Bob' : 13019718340 , 'Mike' : 15907623941}#键唯一，值不唯一
print(my_dict)

my_dict['Tom'] = 13391847632#增加新的键值对
len(my_dict)#返回键值对的数量
my_dict.items()#返回所有的键值对，返回list
my_dict.keys()#返回所有的键，返回list
my_dict.values()#返回所有的值，返回list 
my_dict.clear()#清空字典,返回字典

'Tom' in my_dict #判断键是否在字典中
for element in my_dict:
    print(element)#打印的是键
'''

string = 'fhaudsighuhasfuasfghjsadk'
my_dict = {}
for c in string :#统计每个字母出现的个数
    if c in my_dict:
        my_dict[c] += 1
    else:
        my_dict[c] = 1

print(my_dict)

my_dict1 = {'John':15091524337 , 'Bob' : 13019718340 , 'Mike' : 15907623941}#键唯一，值不唯一
print(my_dict1)