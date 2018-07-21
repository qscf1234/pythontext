# list --> set
l1 = [1, 2, 3, 4]
s1 = set(l1)

# tuple --> set
t2 = (1, 2, 3, 4)
s2 = set(t2)

# set --> list                          list()
# set --> tuple                         tuple()

# 关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符，实例如下：

a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b
