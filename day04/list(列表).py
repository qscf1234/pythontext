# 存储5个人年龄求他们的平均年龄
# 列表本质是一种有序的集合

'''
创建列表
格式：列表名 = [列表选项1， 列表选项2， 列表选项3，。。。 ]
'''
age = [19, 18, 20, 21, 22]
print(sum(age) / 5)
# 创建一个空列表
list1 = []
print(list1)
# 创建带有元素的列表
list2 = [18, 19, 20, 21, 22]
print(list2)
# 注意列表中的元素数据可以是不同类型的
list3 = [1, 2, 'sunk', True]
print(list3)
# 列表元素的访问
# 注意不要越界
# 取值 格式： 列表名[下标]
list4 = [1, 2, 3, 4, 5]
print(list4[2])
# 替换
list4[4] = 300
print(list4)

# 列表操作
# 列表组合
list5 = [1, 2, 3]
list6 = [4, 5, 6]
list7 = list5 + list6
print(list7)
# 列表的重复 list * n
# 判断元素是否在列表中
list9 = [1, 2, 3, 4, 5, 6]
print(3 in list9)
print(9 in list9)
# 列表截取
list10 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list10[2:6])
print(list10[3:])
print(list10[:5])
print(list10[:len(list10)], len(list10))
# 二维列表 list = [[], [], [], [], .....]
list11 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list11[1][1])
# 列表方法
# append 在列表中的末尾添加新的元素
list12 = [0, 1, 2, 3, 4, 5]
list12.append([6, 7, 8])
print(list12)
# extend 在末尾中追加另一个列表中的多个值
list13 = [0, 1, 2, 3, 4, 5]
list13.extend([6, 7, 8])
print(list13)
# insert 在下标处添加一个元素，不覆盖原数据，原数据向后顺延
list14 = [0, 1, 2, 3, 4, 5]
list14.insert(1, 100)
print(list14)
# pop 移除指定下标处的元素,默认为-1(最后一个元素)
# 并返回删除的数据
list15 = [0, 1, 2, 3, 4, 5]
list15.pop()
print(list15)
# remove 移除列表中的某个元素第一个匹配的结果
list16 = [0, 1, 2, 3, 4, 5]
list16.remove(4)
print(list16)
# clear 清除列表中所有元素
list17 = [0, 1, 2, 3, 4, 5]
list17.clear()
print(list17)
# 从列表中找出某个值第一个匹配的索引值
list18 = [0, 1, 2, 3, 4, 5, 3, 4, 5]
index18 = list18.index(3)
index19 = list18.index(3, 6, 8)
print(index18, index19)
# 列表中的元素个数
list20 = [0, 1, 2, 3, 4, 5]
print(len(list20))
# 获取列表中的最大最小值
list21 = [0, 1, 2, 3, 4, 5]
print(max(list21))
print(min(list20))
# 查看元素在列表中出现的次数
list23 = [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]
print(list23.count(3))
num2 = 0
num1 = list23.count(3)
while num2 < num1:
    list23.remove(3)
    num2 += 1
print(list23)
# reverse 降序
list25 = [1, 2, 3, 4, 5]
list25.reverse()
print(list25)
# 升序
list25.sort()
print(list25)
# 拷贝
# 浅拷贝 引用拷贝
list27 = [1, 2, 3, 4, 5]
list28 = list27
list28[1] = 200
print(list28, list27)
# 深拷贝 内存拷贝
list29 = [1, 2, 3, 4, 5]
list30 = list29.copy()
list29[1] = 200
print(list29, list30)
# 将元组转成列表
list31 = list((1, 2, 3, 4))
print(list31)
