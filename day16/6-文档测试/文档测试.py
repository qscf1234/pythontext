import doctest
# doctest模块可以提取注释中的代码进行执行
# doctest严格按照python交互模式的输入提取
def mySum(x, y):
    '''
    get the sum from x and y
    :param x: firstNum
    :param y: secondNum
    :return: sum
    注意有空格
    example:
    >>> print(mySum(1,2))
    3
    '''
    return x + y

# 进行文档测试
doctest.testmod()
