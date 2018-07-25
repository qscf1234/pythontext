import os
def getAllDirRE(path, sp = ''):
    sp += '---'
    # 得到当前目录下所有文件
    filesList = os.listdir(path)
    # 处理每一个文件
    for fileName in filesList:
        # path\fileName  （用绝对路径）
        if os.path.isdir(os.path.join(path, fileName)):
            print(sp + '目录', fileName)
            getAllDirRE(os.path.join(path, fileName),sp)
        else:
            print(sp + '普通文件', fileName)

getAllDirRE(r'D:\pythontext')
