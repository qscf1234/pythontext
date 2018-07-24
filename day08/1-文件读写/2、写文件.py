path = r'D:\pythontext\day08\1-文件读写\file2.txt'
f = open(path, 'w')

# 写文件
# 1、将信息写入缓冲区
f.write('sunck is a good man\n')

# 2、刷新缓冲区
# 刷新缓冲区的四种方法：flush()方法刷新，关闭文件时刷新，遇到\n刷新,换成区域写满时刷新
# 直接吧内部缓冲区的数据立刻写入文件，而不是被动 等待自动刷新写入换成区写入
# f.flush()
# import time
# while True:
#     f.write('sunck is a good man')
#     time.sleep(0.01)
#     pass

f.close()


with open(path, 'a') as f2:
    f2.write('good man')
