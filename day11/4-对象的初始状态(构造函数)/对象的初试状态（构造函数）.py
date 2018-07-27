class Person(object):
    # name = ''
    # age = 0
    # height = 0
    # weight = 0
    def run(self):
        print('run')
    def eat(self, food):
        print('eat' + food)
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
'''
构造函数：__init__()  在使用类创造对象的时候自动调用
注意：如果不显示写出构造函数，默认会自动添加一个空的构造函数

'''
per = Person('hanmeimei', 20, 170, 55)
print(per.name, per.age, per.height, per.weight)
