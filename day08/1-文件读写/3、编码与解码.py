# 编码
path = r'D:\pythontext\day08\1-文件读写\file4.txt'
with open(path, 'w', encoding='utf-8') as f1:
    str1 = 'sunck is a good man 凯'
    f1.write(str1)
with open(path, 'rb') as f2:
    data = f2.read()
    print(data)
    print(type(data))
    newdata = data.decode('utf-8')
    print(newdata)
    print(type(newdata))
