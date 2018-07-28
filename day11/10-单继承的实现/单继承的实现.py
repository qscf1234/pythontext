from person import Person
from student import Student
from worker import Worker

per = Person("aa", 1, 2)

stu = Student("tom", 18, 12345, 110)
print(stu.name, stu.age)
stu.run()
print(stu.stuId)
# print(stu.__money)私有属性
print(stu.getMoney())  # 通过继承过来的共有方法访问私有属性
# stu.stuFunc()

wor = Worker("lilei", 20, 111)
print(wor.name, wor.age)
wor.eat("apple")

print(per.getMoney())
