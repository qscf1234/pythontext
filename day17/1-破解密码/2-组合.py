import itertools
# 从m个不同的元素中，任取n（n≤m）个元素为一组，叫作从m个不同元素中取出n个元素的进行组合
'''
1 2 3 4
'''
mylist = list(itertools.combinations([1, 2, 3, 4, 5], 4))
print(mylist)
print(len(mylist))

'''
m   n
5 - 5   1
5 - 4   5
5 - 3   10
5 - 2   10

120/120(m-n)!
120/24(m-n)!
120/6(m-n)！
m!/(n!(m-n)!)

'''
