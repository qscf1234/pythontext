from multiprocessing import Process,Queue
import os
import time

def write(q):
    print('启动写子进程%s' % (os.getpid()))
    for chr in ["A", "B", "C", "D"]:
        q.put(chr)
        time.sleep(1)
    print("结束写子进程%s" % (os.getpid()))

def read(q):
    print("启动读子进程%s" % (os.getpid()))
    while True:
        value = q.get(True)
        print("value = " + value)
    print("结束读子进程%s" % (os.getpid()))

if __name__ == '__main__':
    # 父进程创建队列，并传递给子进程
    q = Queue()
    wp = Process(target=write, args=(q, ))
    rp = Process(target=read, args=(q, ))
    wp.start()
    rp.start()
    #
    wp.join()
    # rp进程里是个死循环，无法等待其结束，只能强行结束
    rp.terminate()

    print("父进程结束")
