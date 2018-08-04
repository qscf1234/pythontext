import os
import time
from multiprocessing import Pool, Process

def copyFile(rPath, wPath):
    with open(rPath, 'rb') as f1:
        Data = f1.read()
        with open(wPath, 'wb') as f2:
            f2.write(Data)

if __name__ == '__main__':
    print('父进程启动')
    star = time.time()

    rPath = os.path.join(os.getcwd(), 'file')
    wPath = os.path.join(os.getcwd(), 'tofile')

    filesList = os.listdir(rPath)

    # 创建多个进程
    # 进程池
    # 表示可以同时执行的进程数量
    # Pool默认大小是CPU核心数
    pp = Pool()
    for fileName in filesList:
        pp.apply_async(copyFile, args=(os.path.join(rPath, fileName), os.path.join(wPath, fileName)))
    pp.close()
    pp.join()
    end = time.time()
    print('总耗时：%0.5f' % (end - star))
    print('父进程结束')
