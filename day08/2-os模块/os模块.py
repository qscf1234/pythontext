import os
'''
os:包含了普遍的操作系统的功能
'''
# 获取操作类型  nt-->windows  posix-->Linux、Unix、Mac OS
print(os.name)
# 打印操作系统的详细信息  linux支持windows不支持
# print(os.uname())
# 获取操作系统的所有环境变量
print(os.environ)
# 获取操作系统的指定环境变量
print(os.environ.get('APPDATA'))

# 获取当前路径  ./a/
print(os.curdir)
# 获取当前工作目录，即当前python脚本所在的目录
print(os.getcwd())
# 以列表的形式返回指定目录下所有的文件
print(os.listdir(r'D:\pythontext\day08'))
# 在当前目录下创建新目录
# os.mkdir('sunck')
# 删除目录
# os.rmdir('sunck')
# 获取文件属性
#print(os.stat('sunck'))
# 重命名
#os.rename('sunck', 'kaige')
# 删除普通文件
# os.remove('file1.txt')
# 运行shell命令
# os.system('notepad')  # 打开记事本
# os.system('write')    # 打开写字板
# os.system('mspaint')  # 打开画图
# os.system('msconfig')   # 打开系统配置
# os.system('shutdown -s -t 500')  # 延时一段时间后关机
# os.system('shutdown -a')     # 取消关机
# os.system('taskkill /f /im notepad.exe')

# 有些方法存在os模块里，还有些存在于os.path
# 查看当前的绝对路径
print(os.path.abspath('./kaige'))
# 拼接路径
p1 = r'D:\pythontext\day08\2-os模块'
p2 = r'kaige'
# 注意：参数2里开始不要有斜杠
print(os.path.join(p1, p2))
# 拆分路径
path2 = r'D:\pythontext\day08\2-os模块\kaige'
print(os.path.split(path2))
# 获取后缀名（没有就是空）
print(os.path.splitext(path2))
# 判断是否是目录
print(os.path.isdir(path2))
# 判断文件是否存在
print(os.path.isfile(path2))
# 判断目录是否存在
print(os.path.exists(path2))
# 获得文件大小
path3 = r'D:\pythontext\day08\函数也是一种数据类型.py'
print(os.path.getsize(path3))
# 获得文件的目录
print(os.path.dirname(path3))
# 获得文件的名字
print(os.path.basename(path3))

