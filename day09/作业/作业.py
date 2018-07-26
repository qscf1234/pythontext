linedict = {}
path = r'D:\pythontext\day09\作业\kaifang.txt'
f = open(path, 'r', encoding='utf-8')
# ysline = f.readline().rstrip('\n')      读取并去掉最后的换行符
# yslinelist = ysline.split(',', 1)       以第一个逗号为界切割成两个元素
# ysdict[yslinelist[0]] = yslinelist[1]   生成字典
while True:
    line = f.readline().rstrip('\n')
    # 判断是否是该文件最后一行
    if not line:
        break
    linelist = line.split(',', 1)
    linedict[linelist[0]] = linelist[1]
name = input('查询名字')
print(linedict[name])
f.close()
