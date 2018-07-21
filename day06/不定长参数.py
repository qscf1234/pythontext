'''
概念：能处理比定义时更多的参数
'''
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数,如果函数调用时没有指定参数就是
# 空元组

def func(name, *args):
    print(name)
    for x in args:
        print(x,end=',')
    print('\n')

func('sunck', 'good', 'nice', 'handsom')

# 加了两个星号 ** 的参数会以字典的形式导入。
def func2(**kwargs):
    print(kwargs)
    print(type(kwargs))
func2(x = 1, y = 2, z = 3)


