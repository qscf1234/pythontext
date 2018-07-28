class Person(object):
    def __init__(self, count):
        self.count = count
    def fire(self):
        if self.count <= 0:
            print('没有子弹了')
            self.count = 0
        else:
            self.count -= 1
            print('剩余%d发子弹' % (self.count))
    def filebulle(self, count):
        self.count += count
        print('剩余%d发子弹' % (self.count))

per = Person(5)
per.fire()
per.fire()
per.fire()
per.filebulle(2)
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()