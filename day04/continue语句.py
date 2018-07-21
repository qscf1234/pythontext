'''
continue语句
作用：跳过当前循环中的剩余语句，然后继续下一次循环
'''
for i in range(10):
    print(i)
    if i == 3:
        continue
    if i == 8:
        break
    print('*')
    print('&')

i = 0
while i < 10:
    print(i)
    if i == 3:
        i += 1
        continue
    if i == 8:
        break
    print('*')
    print('&')
    i += 1
