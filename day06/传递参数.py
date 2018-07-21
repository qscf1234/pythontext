'''
值传递：传递不可变类型
string、tuple、number是不可变的
'''

def func1(num):
    num = 10

temp = 20
func1(temp)
print(temp)

'''
引用传递：传递可变类型
list、dict、set是可变的
'''
def func2(lis):
    lis[0] = 100

li = [1, 2, 3, 4]
func2(li)
print(li)
