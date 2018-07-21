'''
概念：不使用def这样的语句定于函数，使用lambda来创建匿名函数
特点：
1、lambda 只是一个表达式，函数体比 def 简单很多。
2、lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
3、lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
4、虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函
   数时不占用栈内存从而增加运行效率。

语法：
lambda [arg1 [,arg2,.....argn]]:expression
'''

sun = lambda num1, num2: num1 + num2
print(sun(1, 2))

