# 引入模块
import sys
print(sys.argv)
# 获取命令行参数的列表
for i in sys.argv:
    print(i)
name = sys.argv[1]
age = sys.argv[2]
hoby = sys.argv[3]
print(name, age, hoby)
# 自动查找所需模块的路径的列表
print(sys.path)
