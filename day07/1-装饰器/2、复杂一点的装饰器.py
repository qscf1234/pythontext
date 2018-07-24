
def outer(func):
    def inner(age):
        if age < 0:
            age = 0
        func(age)
    return inner
# 使用@符号将装饰器应用到函数
# python2.4支持使用@符号
@outer  #相当于say = outer（say）
def say(age):
    print('sunck is %d years old'% (age))
# say = outer(say)
say(-10)
