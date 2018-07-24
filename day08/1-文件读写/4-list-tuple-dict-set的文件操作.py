import pickle # 数据持久性模块
mylist = [1, 2, 3, 4, 5, 'sunck is a good man']
path = r'D:\pythontext\day08\1-文件读写\file5.txt'
f = open(path, 'wb')
pickle.dump(mylist, f)
f.close()

# 读取
f1 = open(path, 'rb')
templist = pickle.load(f1)
print(templist)
print(type(templist))
f1.close()

mydict = {'a': 1, 'b': 2}
path = r'D:\pythontext\day08\1-文件读写\file6.txt'
f = open(path, 'wb')
pickle.dump(mydict, f)
f.close()

# 读取
f1 = open(path, 'rb')
tempdict = pickle.load(f1)
print(tempdict)
print(type(tempdict))
f1.close()



