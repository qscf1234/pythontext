'''
for 语句：
格式：
for 变量名 in 集合:
    语句
逻辑：按顺序取‘集合’中的每个元素赋值给‘变量’，再去执行语句，如此循环往复，
      直到取完‘集合’中的元素截至
'''
for i in [1, 2, 3, 4, 5]:
    print(i)
'''
range([start], end, [step])函数  列表生成器
功能：生成数列
'''
a = range(10)
print(a)
for x in range(10):
    print(x, )
for y in range(2, 20, 2):
    print(y)
# enumerate()同时遍历下标和元素
for index, m in enumerate([1, 2, 3, 4, 5]):
    print(index, m)
sum1 = 0
for n in range(1, 101, 1):
    sum1 += n
print(sum1)
