import threading
import time

def func():
    # 事件对象
    event = threading.Event()
    def run():
        for i in range(5):
            # 阻塞，等待事件触发
            event.wait()
            event.clear()
            print('sunck is a good man')
    t = threading.Thread(target=run).start()
    return event

e = func()

for i in range(5):
    time.sleep(1)
    e.set()
