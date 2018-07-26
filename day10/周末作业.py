import os
import collections

def work(path):
    resPath = r"D:\pythontext\day10\res"
    if not os.path.exists(resPath):
        #不存在,创建
        os.mkdir(resPath)
    #打开文件
    with open(path, "r") as f:
        while True:
            #laphael1985@163.com----198587
            lineInfo = f.readline()
            if len(lineInfo) < 5:
                break
            #邮箱的字符串
            #laphael1985 @ 163.com
            mailStr = lineInfo.split("----")[0]
            #邮箱类型的目录
            #C:\Users\xlg\Desktop\Python-1704\day10\res\163
            #print(mailStr)
            fileType = mailStr.split("@")[1].split(".")[0]
            dirStr = os.path.join(resPath, fileType)
            if not os.path.exists(dirStr):
                #不存在,创建
                os.mkdir(dirStr)
            filePath = os.path.join(dirStr, fileType + ".txt")
            with open(filePath, "a") as fw:
                fw.write(mailStr+"\n")

def getAllDirQU(path):
    queue = collections.deque()
    queue.append(path)
    while len(queue) != 0:
        dirPath = queue.popleft()
        filesList = os.listdir(dirPath)
        for fileName in filesList:
            fileAbsPath = os.path.join(dirPath, fileName)
            if os.path.isdir(fileAbsPath):
                queue.append(fileAbsPath)
            else:
                #处理普通文件
                work(fileAbsPath)

getAllDirQU(r"D:\pythontext\day10\newdir")
