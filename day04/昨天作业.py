# # 打印出所有三位中的水仙花数
# a = 100
# while a <= 999:
#     b = a // 100
#     s = a % 100 // 10
#     g = a % 10
#     if a == (b ** 3 + s ** 3 + g ** 3 ):
#         print(a)
#     a += 1
#
# # 五位数中的有多少个回文数
# a = 10000
# i = 0
# while a <= 99999:
#     if (a//10000 == a % 10)and (a//1000 == a % 1000 // 10):
#         print(a)
#         i += 1
#     a += 1
# print(i)
#
# # 从控制台输入一个数判断是否是质数
# a = int(input('输入一个数'))
# if a == 1:
#     print('不是质数，质数从2开始')
# else:
#     flag = 0
#     i = 1
#     while i < a:
#         j = i
#         while j < a:
#             if a == i * j:
#                 flag = 1
#             j += 1
#         i += 1
#     if flag == 0:
#         print('是质数')
#     else:
#         print('不是质数')
# '''
#
# '''
#
#
# # 从控制台输入一个数，分解质因数
# a = int(input('请输入一个数'))
# i = 2
# while i <= a:
#     if a % i == 0:
#         flag = 0
#         k = 2
#         while k <= i:
#             n = k
#             while n <= i:
#                 if i == k * n:
#                     flag = 1
#                 n += 1
#             k += 1
#         if flag == 0:
#              print(i)
#     i += 1
#
# 输入一个字符串，返回这个字符串中有多少个单词
a = input()
ga = a.lstrip().rstrip()
print(ga)
b = ga.count(' ') + 1
print(b)
#
# # 输入字符串，返回字符串中所有数字的和
# a = input()
# b = 0
# sum1 = 0
# while b < len(a):
#     if (a[b] >= '0') and (a[b] <= '9'):
#         sum1 += int(a[b])
#     b += 1
# print(sum1)
# # 求质因数
# num = 2*3*5*7*11
# i = 2
# while num != 1:
#     if num % i == 0:
#         print(i)
#         num //= i
#     else:
#         i += 1
