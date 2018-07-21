'''
set:类似dict，是一组key的组合，不存储value

本质：无序和无重复元素的集合
'''
# 创建
# 创建set需要一个list或者tuple或者dict作为输入集合
# 重复元素在set中会自动被过滤
s1 = set([1, 2, 3, 4, 5, 4, 3])        # 列表
print(s1)
s2 = set((1, 2, 3, 4, 5, 4, 3))        # 元组
print(s2)
s3 = set({1: 'good', 2:'cool'})        # 字典
print(s3)
# 添加
s4 = set([1, 2, 3, 4, 5])
s4.add(6)
s4.add(3) # 可以添加重复的但是不会用效果
# s4.add([7, 8, 9]) # set的元素不能是列表，字典，因为他们可变
s4.add((7, 8, 9))
print(s4)

# 插入整个list、tuple、字符串，打碎插入
s5 = set([1, 2, 3, 4, 5])
s5.update([6, 7, 8])
s5.update('update')
s5.update({11: 'good', 12: 'cool'})
print(s5)

# 删除
s6 = set([1, 2, 3, 4, 5])
s6.remove(3)
print(s6)

# 遍历
s7 = set([1, 2, 3, 4, 5])
for i in s7:
    print(i)
# set没有索引
for index, date in enumerate(s7):
    print(index, date)
# index没有实际意义


s8 = set([1, 2, 3])
s9 = set([2, 3, 4])
# 交集
a1 = s8 & s9
print(a1)
print(type(a1))
# 并集
a2 = s8 | s9
print(a2)
print(type(a2))

