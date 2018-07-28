
'''
人
类名：Person
属性：gun
行为：fire

枪
类名：Gun
属性：bulletBox
行为：shoot

弹夹
类名：BulletBox
属性：bulletcount
行为：
'''
class Person(object):
    def __init__(self, gun):
        self.gun = gun
    def fire(self):
        self.gun.shoot()
    def fillBullet(self, count):
        self.gun.bulletBox.count += count
        print('剩余子弹：%d发' % (self.gun.bulletBox.count))

class Gun(object):
    def __init__(self, bulletBox):
        self.bulletBox = bulletBox
    def shoot(self):
        if self.bulletBox.count == 0:
            print('没有子弹了')
        else:
            self.bulletBox.count -= 1
            print('剩余子弹：%d发' % (self.bulletBox.count))

class BulletBox(object):
    def __init__(self,count):
        self.count = count


# 弹夹
bulletBox = BulletBox(5)

# 枪
gun = Gun(bulletBox)

# 人
per = Person(gun)

per.fire()
per.fire()
per.fire()
per.fillBullet(2)
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()


