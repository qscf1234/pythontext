'''
概念：允许函数调用时参数的顺序与定义时不一定
'''

def myprint(str, age):
    print(str, age)
# 实参（实际参数）：调用函数是给函数传递的数据，本质是值
myprint( age = 18, str = 'sunck ')


