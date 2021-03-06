from multiprocessing import Process
from time import sleep

num = 100

def run():
    print('父进程开始')
    global num
    num += 1
    print(num)
    print('子进程结束')


if __name__ == '__main__':
    print('父进程开始')

    p = Process(target=run, )
    p.start()
    p.join()

    # 在子进程中欧修改全局变量对父进程中的全局变量没有影响
    # 在创建子进程时对全局变量做了一个备份，父进程中的与子进程中的num是完全不同的两个变量
    print(num)
    print('父进程结束')
