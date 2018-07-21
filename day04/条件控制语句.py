# -*-coding: utf-8 -*-
'''
if 语句

if-else语句

if-elif-else语句
格式：
if 表达式1：
   语句1
elif 表达式2：
    语句2
elif 表达式3：
    语句3
。。。。。。。。。。。
else:
     语句.......

'''

age = int(input())
if  age < 0:
    print('娘胎里')
elif age < 3 and age >= 0:
    print('婴儿')
elif age < 6 and age >= 3:
    print('童年')
elif age < 18 and age >= 6:
    print('少年')
else:
    print('中年')
















