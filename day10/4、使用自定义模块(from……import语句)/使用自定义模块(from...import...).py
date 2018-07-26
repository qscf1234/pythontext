'''
from ...import语句
作用：从模块中导入一个指定的部分到当前命名空间
格式：from module import name1[, name2][, name3].......
'''
from sunck import sayGood, sayNice
'''
程序内容的函数可以将模块中的同名函数覆盖
def sayGood():
    print("********")
'''
sayGood()
sayNice()
# sayHandsome # 没有引入sayHandsome

