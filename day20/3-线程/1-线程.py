'''
在一个进程的内部，要同时干多件事，就需要同时运行多个“子任务”，我们把进程内的这些“子任务”叫做线程
线程通常叫做轻型的进程。线程是共享内存空间的并发执行的多任务，每一个线程都共享一个进程的资源
线程是最小的执行单元，而进程由至少一个线程组成。如何调度进程和线程，完全由操作系统决定，程序自己不能决定什么时候执行，执行多长时间
模块
1、_thread模块       低级模块
2、threading模块     高级模块，对_thread进行了封装
'''
