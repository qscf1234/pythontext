
'''
排序：冒泡，选择        快速排序，插入，计数器
'''

# 普通排序
list1 = [4, 7, 2, 6, 3]
list2 = sorted(list1)
print(list2)


# 按绝对值大小排序, key接受函数来实现自定义排序规则
list3 = [4, -7, 2, 6, -3]
list4 = sorted(list3, key=abs)
print(list4)

# 降序
list5 = [4, 7, 2, 6, 3]
list6 = sorted(list5, reverse=True)
print(list6)

# 函数可以自己写
def myLen(str):
    return len(str)
list7 = ['b333', 'a1111111', 'c22', 'd5554']
list8 = sorted(list7, key=myLen) # 默认升序排序
print(list8)



