'''
datetime比time高级，可以理解为datetime基于time进行了封装，提供了各种使用的函数，datetime模块的
接口更直观，更容易调用

模块中的类：
datetime    同时有时间和日期
timedelta   主要用于计算时间的跨度
tzinfo      时区相关
time        只关注时间
date        只关注日期
'''
import datetime
# 获取当前时间
d1 = datetime.datetime.now()
print(d1)
# 获取指定时间
d2 = datetime.datetime(1999, 10, 1, 10, 28, 25, 123456)
print(d2)
# 将时间转为字符串
d3 = d1.strftime('%y-%m-%d  %X')
print(d3)
# 将格式化字符串转换为datetime对象
# 注意：转换的格式要与字符串一致
d4 = datetime.datetime.strptime(d3, '%y-%m-%d  %X')
print(d4)
print(type(d4))
# 间隔时间
d5 = datetime.datetime(1999, 10, 1, 10, 28, 25, 123456)
d6 =datetime.datetime.now()
d7 = d6 - d5
print(d7)
print(type(d7))
# 间隔的天数
print(d7.days)
# 间隔天数的秒数
print(d7.seconds)
