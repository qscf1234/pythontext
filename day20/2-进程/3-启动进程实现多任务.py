from multiprocessing import Process

'''
multiprocessing 库
跨平台版本的多进程模块，提供了一个Process类来代表一个进程对象
'''

from time import sleep

def run():
    while True:
        print('sunck is a nice man')
        sleep(0.4)

if __name__ == '__main__':
    print('主(父)进程启动')
    # 创建子进程
    # target说明进程执行的任务
    p = Process(target=run)
    # 启动进程
    p.start()
    while True:
        print('sunck is a good man')
        sleep(1)
