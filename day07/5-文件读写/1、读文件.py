'''

过程:
1、打开文件
2、读文件内容
3、关闭文件

'''

'''
1、打开文件
open(path，flag[, encoding][, errors])
path：要打开文件的路径
flag：打开方式
r       以只读的方式打开文件，文件的描述符放在开头
rb      以二进制格式打开一个文件用于只读，文件的描述符放在文件的开头
r+      打开一个文件用于读写，文件的描述符放在文件的开头
w       打开一个文件只用于写入，如果该文件已经存在会覆盖，如果不存在则创建新文件
wb      打开一个文件只用于写入二进制，如果该文件已经存在会覆盖，如果不存在则创建新文件
w+      打开一个文件用于读写如果该文件已经存在会覆盖，如果不存在则创建新文件
a       打开一个文件用于追加，如果文件存在，文件描述符将会放到文件末尾
a+      打开一个文件用于读写，如果文件存在，文件描述符将会放到文件末尾
encoding:编码方式
errors：错误处理

'''
path = r'D:\pythontext\day07\5-文件读写\file1.txt'
f = open(path, 'r', encoding='utf-8', errors='ignore')

'''
2、读文件内容
'''
# 1、读取文件全部内容
str1 = f.read()
print(str1)
# 2、读取指定字符数
# str2 = f.read(21)
# print('******'+str2+'******')
# str3 = f.read(21)
# print('******'+str3+'******')
# 3、读取整行
# str4 = f.readline()
# print(str4)
# str5 = f.readline()
# print(str5)
# 4、读取指定字符数
# str6 = f.readline(10)
# print(str6)
# 5、读取所有行并返回列表
# list7 = f.readlines()
# print(list7)
# 6、若给定的数字大于0，返回实际size字节的行数
# list8 = f.readlines(10)
# print(list8)
print('********************')
# 修改描述符的位置
f.seek(0)
str9 = f.read()
print(str9)

'''
3、关闭文件
'''
f.close()


# 一个完整的过程
try:
    f1 = open(path, 'r', encoding='utf-8')
    print(f1.read())
finally:
    if f1:
        f1.close()

# with 会自动关闭文件
with open(path, 'r', encoding='utf-8') as f2:
    print(f2.read())
