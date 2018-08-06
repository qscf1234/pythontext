import time, random
def product(c):
    c.send(None)
    print("消费者消费了数据%s" % r)
    while True:
        i = random.randint(0, 1000)
        print("生产者产生数据%d" % i)
        r = c.send(str(i))
        print("消费者消费了数据%s" % r)
        time.sleep(0.01)
    c.close()

def customer():
    data = ""
    while True:
        n = yield data
        if not n:
            return
        print("消费者消费了%s" % n)
        data = n

c = customer()
product(c)


