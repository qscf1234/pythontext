import urllib.request
import os.path

# 向指定的url地址发起请求，并返回服务器相应的数据(文件的对象)
response = urllib.request.urlopen('http://www.baidu.com')

# 读取文件的全部内容，会把读取到的数据赋值给一个字符串变量
# date = response.read()
# print(date)

# 读取一行
# date = response.readline()
# print(date)

# 读取文件的全部内容，会把读取到的数据赋值给一个列表变量
date = response.readlines()
'''
print(date)
print(len(date))
print(type(date[100]))
print(type(date[100].decode('utf-8')))
'''

# 将爬取到的网页写入文件
# path = os.path.join(os.getcwd(),'file','file1.html')
# with open(path, 'wb') as f:
#     f.write(date)

# response属性
# 返回当前环境的有关信息
print(response.info())
# 返回状态码
print(response.getcode())
# if response.getcode() == 200 or response.getcode() == 304:
#     处理网页信息
#     pass

# 返回当前正在爬取的URL地址
print(response.geturl())
'''

url = 'https://www.baidu.com/s?wd=%E5%87%AF%E5%93%A5%E5%AD%A6%E5%A0%82&rsv_spt=1&rsv_iqid=0xa1de459600008990&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=21&rsv_sug1=12&rsv_sug7=100&rsv_sug2=0&inputT=8405&rsv_sug4=11235'
# 解码
newUrl = urllib.request.unquote(url)
print(newUrl)
# 编码
newUrl2 = urllib.request.quote(newUrl)
print(newUrl2)
'''
