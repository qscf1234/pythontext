'''
filter()
原型：filter(fn, lsd)
参数1是函数
参数2是序列

功能：用于过滤序列

'''

def func1(num):
    if num % 2 == 0:
        return True
    return False

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

l = filter(func1, list1)
print(list(l))
print(type(l))

data= [["姓名", "年龄", "爱好"], ["tom", 25, "无"], ["hanmeimei", 26, "金钱"]]
def func2(v):
    v = str(v)
    if v == "无":
        return False
    return True
for line in data:
    l2 = filter(func2, line)
    print(list(l2))
