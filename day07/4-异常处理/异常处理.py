'''
Python有两种错误很容易辨认：语法错误和异常。

语法错误:
Python 的语法错误或者称之为解析错

异常:
即便Python程序的语法是正确的，在运行它的时候，也有可能发生错误。运行期检测到的错误被称为异常。

'''

# print(3/0)
# 需求：当程序遇到问题时

'''
try...except...else
格式:
try:
    语句t
except 错误码 as e：
    语句1
except 错误码 as e：
    语句2
...
else:
    语句n+1
注意：else可有可无
作用：用来检测try语句中的错误，从而让except语句捕获错误信息并处理
逻辑：当程序执行到try-except-else语句时
1、如果当try‘语句t’执行出现错误，会匹配执行第一个错误码，如果匹配上就执行对应‘语句’
2、如果当try‘语句t’执行出现错误，没有匹配的异常，错误将会被提交到上一层的try语句，
   或者到程序最上层
3、如果当try‘语句t’执行没有出现错误，执行下else下的语句
'''
try:
    print(3 / 1)
    # print(num)
except ZeroDivisionError as e:
    print('除数为0了')
except NameError as e:
    print('没有该变量')
else:
    print('***********')
print('&&&&&&&&&&&&&&')

# 使用except而不使用任何的错误类型
try:
    print(4/0)
except:
    print('程序出现异常')

# 使用except带着多种异常
try:
    print(5 / 0)
except (ZeroDivisionError, NameError):
    print('出现了ZeroDivisionError或NameError')

# 特殊
# 1、错误其实是class（类），所有的错误都继承自BaseException，所以在捕获的时候，它捕获了该类型的
#    错误，还把自类一网打尽
try:
    print(5 / 0)
except BaseException as e:
    print('异常1')
except ZeroDivisionError as e:
    print('异常2')

# 2、跨越多层调用，main调用了func2，func2调用了func1，func1出现了错误，
# 这是只要main捕获到了错误就可以处理
def func1(num):
    print(1 / num)
def func2(num):
    func1(num)
def main():
    func2(0)

try:
    main()
except ZeroDivisionError as e:
    print('*******')

'''
try...except...else
格式:
try:
    语句t
except 错误码 as e：
    语句1
except 错误码 as e：
    语句2
...
finally:
    语句n+1
作用，无论是否有错误都执行最后的语句
'''
try:
    print(3 / 0)
except ZeroDivisionError as e:
    print('除数为0了')
finally:
    print('***********')
print('&&&&&&&&&&&&&&')









# https://blog.csdn.net/lina_acm/article/details/54808910 参考文献