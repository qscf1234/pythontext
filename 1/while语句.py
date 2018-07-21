'''
while 语句：
格式
while 表达式:
      语句
逻辑： 当程序执行到while语句时会先计算表达式的值，
      表达式为假不执行，为真执行
'''
i = 1
while i <= 10:
    print(i)
    i = i+1
# 计算1+2+.....+100
sum1 = 0
num1 = 1
while num1 <= 100:
    sum1 += num1
    num1 += 1
    print(sum1, num1)

str1 = 'sunck is a handsome man'
index = 0
while index < len(str1):
    print('str[%d] = %s'%(index, str1[index]))
    index += 1
