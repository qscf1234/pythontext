from functools import reduce

# python内置map()和reduce()函数

'''
map()
原型  map(fn, lsd)
参数1是函数
参数2是序列

功能：将传入的函数依次作用在序列中的每一个元素，并把结果作为新的Iterator放回
'''

# 将单个字符串转换成对应的字面量整数
def chr2int(chr):
    if ord(chr) <=57 and ord(chr)>=48:
        return ord(chr)-48

list1 = ['2', '1', '5', '6']
res = map(chr2int, list1)
print(res)
print(list(res))

# 将整数元素的序列转换成字符串型
l = map(str, [2, 1, 5, 6])
print(list(l))

'''
reduce(fn, lsd)
参数1为函数
参数2为列表
功能：一个函数作用在序列上，这个函数必须接受两个参数，reduce把结果继续和序列的下一个元素累计运算
reduce(f, [a, b, c, d])
f(f(f(a, b), c), d)
'''

# 求一个序列的和
list2 = [1, 2, 3, 4, 5]
def mysum(x, y):
    return x+y
r = reduce(mysum, list2)
print(r)

# 将字符串转换成对应字面量数字
def str2int(str):
    def fc(x,y):
        return x * 10 + y
    def chr2int(chr):
        if ord(chr) <= 57 and ord(chr) >= 48:
            return ord(chr) - 48
    return reduce(fc, map(chr2int, list(str)))
a = str2int('123456')
print(a)
print(type(a))

def myMap(func, li):
    reslist= []
    for parase in li:
        res = func(parase)
        reslist.append(res)
    return reslist
