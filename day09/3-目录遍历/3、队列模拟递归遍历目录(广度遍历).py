import os
import collections

def getAllDirQU(path):
    queue = collections.deque()
    # 进队
    queue.append(path)
    while len(queue) != 0:
        # 出队数据
        dirPath = queue.popleft()
        # 找出所有目录
        fileList = os.listdir(dirPath)
        for fileName in fileList:
            # 绝对路径
            fileAbsPath = os.path.join(dirPath, fileName)
            if os.path.isdir(fileAbsPath):
                print('目录' + fileName)
                queue.append(fileAbsPath)
            else:
                print('普通文件' + fileName)

getAllDirQU(r'D:\pythontext')
