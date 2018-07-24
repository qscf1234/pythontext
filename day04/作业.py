'''
打印九九乘法表
输入两个数，求这两个数的最大公约数
输入一个字符串，将字符串中的大写字母转小写字母，小写字母转大写
随机生成一个6位数的验证码（数字，大小写字母）
'''
'''
## 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('%d * %d = %d' % (j, i, i*j))
'''
'''
# 输入两个数，求这两个数的最大公约数
a = int(input())
b = int(input())
c = min(a, b)
d = max(a, b)
e = min(a, b)
while c:
    if d % c == 0:
        if e % c == 0:
            break
    c = c - 1
print(c)
'''
'''
# 输入一个字符串，将字符串中的大写字母转小写字母，小写字母转大写
# a = input()
# b = []
# for i, j in enumerate(a):
#     if (j >= 'a') and (j <= 'z'):
#         b.append(chr(ord(j) - 32))
#     if (j >= 'A') and (j <= 'Z'):
#         b.append(chr(ord(j) + 32))
# c = ''.join(b)
# print(c)


# a = list(input())
# for i, j in enumerate(a):
#     if (j >= 'a') and (j <= 'z'):
#         a[i] = chr(ord(j) - 32)
#     if (j >= 'A') and (j <= 'Z'):
#         a[i] = chr(ord(j) + 32)
# a = ''.join(a)
# print(a)
'''

# 随机生成一个6位数的验证码（数字，大小写字母）
import random
a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
     'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'A', 'S',
     'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'Z', 'X',
     'C', 'V', 'B', 'N', 'M']
b = random.sample(a, 5)
print(b)
