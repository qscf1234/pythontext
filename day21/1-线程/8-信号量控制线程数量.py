import threading
import time

sem = threading.Semaphore(3)

def run():
    with sem:
        for i in range(10):
            print('%s---%d' % (threading.current_thread().name, i))

if __name__ == '__main__':
    for i in range(6):
        threading.Thread(target=run).start()
