import os
import time

def copyFile(path):
    # 得到当前目录下所有文件
    rPath = os.path.join(path, 'file')
    filesList = os.listdir(rPath)
    print(len(filesList))
    for filesName in filesList:
        absPath = os.path.join(rPath, filesName)
        if os.path.isfile(absPath):
            with open(absPath, 'rb') as f1:
                Data = f1.read()
                copyPath = os.path.join(path, 'tofile', filesName)
                print(copyPath)
                with open(copyPath, 'wb') as f2:
                    f2.write(Data)

if __name__ == '__main__':
    star = time.time()
    path = os.getcwd()
    copyFile(path)
    end = time.time()
    print('总耗时：%0.5f' % (end-star))
