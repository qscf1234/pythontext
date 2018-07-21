listNum = [86, 51, 63, 12, 5]
# num =0
# while num < 10:
#     val = int(input())
#     listNum.append(val)
#     num += 1
print(listNum)
# 升序排序法
listNum1 = listNum.copy()
listNum1.sort()
print(listNum1[len(listNum1)-2])
# 删除最大后再求最大
listNum2 = listNum.copy()
listNum2.sort()
listNum2.pop()
print(listNum2[len(listNum2)-1])


