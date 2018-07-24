def sum1(a,b):
    return a + b
# 函数名也相当于一种变量名
f = sum1
# 函数名加()才执行
print(sum1(1, 2))
print(f(1, 2))
