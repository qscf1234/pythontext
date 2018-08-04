from multiprocessing import Process
from time import sleep
import os

'''
multiprocessing 库
跨平台版本的多进程模块，提供了一个Process类来代表一个进程对象
'''

def run(str):
    while True:
        # os.getpid()获取当前进程id号
        print('sunck is a %s man--%s' % (str, os.getpid()))
        # os.getppid()获取当前进程的父进程id号
        print('父进程号%s' % (os.getppid()))
        sleep(1)

if __name__ == '__main__':
    print('主(父)进程启动')
    # 创建子进程
    # target说明进程执行的任务
    p = Process(target=run, args=('nice',))
    # 启动进程
    p.start()
    while True:
        print('sunck is a good man--%s' % (os.getpid(), ))
        sleep(1)
