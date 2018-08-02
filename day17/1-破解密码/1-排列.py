import itertools
# 从n个不同元素中取出m（m≤n）个元素，按照一定的顺序排成一列，叫做从n个元素中取出m个元素的一个排列(Arrangement)。特别地，当m=n时，这个排列被称作全排列(Permutation)
'''
1 2 3 4
_ _ _
'''
mylist = list(itertools.permutations([1, 2, 3, 4], 3))
print(mylist)
print(len(mylist))

'''
排列的可能性次数：n! / (n-m)!
'''
