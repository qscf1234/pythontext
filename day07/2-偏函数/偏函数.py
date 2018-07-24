import functools
#
print(int('123', base=10))
print(int('1010', base=10))
print(int('1010', base=2))

# 偏函数
def int2(str, base =2):
    return int(str, base)
print(int2('1010'))

# 固定住原函数的部分参数，从而在调用时更简单。
int3 = functools.partial(int, base =2)
print(int3('111'))
