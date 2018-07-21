'''
字典
使用键-值（key-value）存储，具有极快的查找速度
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，
整个字典包括在花括号({})中 ,格式如下所示：
d = {key1 : value1, key2 : value2 }
注意：字典是无序的
key 的特性：
1、字典中的key必须唯一
2、key必须是不可变对象
3、字符串、整数等都是不可变的，可以作为key
4、list是可变的不能作为key
'''

dict1 = {'tom': 60, 'lilei': 70}
# 元素访问
# 获取：字典名[key]
print(dict1['lilei'])

# 添加
# 一个key对应一个值，多次对一个key的value赋值，其实就是修改值
dict1['hanmeimei'] = 99
dict1['lilei'] = 80
print(dict1)

# 删除
dict1.pop('tom')
print(dict1)
# 遍历
for key in dict1:
    print(key, dict1[key])
for value in dict1.values():
    print(value)
for k, v in dict1.items():
    print(k, v)
print(dict1.items())
for i, v2 in enumerate(dict1):
    print(i, v2)

# list比较
# dict
# 1、查找和插入的速度极快，不会随着key-value的增加而变慢
# 2、需要占用大量的内存，浪费内存少

# list
# 1、查找和插入的速度随着数据量的增多而减慢
# 2、占用空间少，浪费内存是少



