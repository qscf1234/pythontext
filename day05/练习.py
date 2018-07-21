# 通过一段话做字典
str1 = 'sunck is a good man! sunck is a nice man! sunck is a hands man! ' \
       'sunck is a good man! sunck is a nice man! sunck is a great man! ' \
       'sunck is a noble man! sunck is a good man! sunck is a cool man! '
d={} # word:次数
l = str1.split(' ')
print(l)
for v in l:
    c = d.get(v)
    if c == None:
        d[v] = 1
    else:
        d[v] += 1
print(d)
print(d.values())
print(d.keys())

'''
思路：
1、以空格切割字符串
2、循环处理列表中的每个元素
3、以元素当作一个key去一个字典中提取数据
4、如果没有提取到，就以该元素作为key，1作为value存进字典
5、如果提取到，将对应的value修改，值+1
6、根据输入的字符串当作key再去字典取值
'''
