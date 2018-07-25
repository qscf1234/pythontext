import os

def getAlldirDE(path):
    stack = []
    stack.append(path)
    # 处理栈，当栈为空的时候结束循环
    while len(stack) != 0:
        # 从栈里去除数据
        dirPath = stack.pop()
        # 目录下所有文件
        fileList = os.listdir(dirPath)
        # 处理每个目录，如果是普通文件则打印出来，如果是目录就将该目录地址压栈
        for fileName in fileList:
            fileAbsPath = os.path.join(dirPath, fileName)
            if os.path.isdir(fileAbsPath):
                # 是目录就压栈
                stack.append(fileAbsPath)
                print('目录' + fileName)
            else:
                print('普通文件' + fileName)

getAlldirDE(r'D:\pythontext')
