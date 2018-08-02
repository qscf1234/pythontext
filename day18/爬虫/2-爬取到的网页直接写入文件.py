import urllib.request
import os.path

urllib.request.urlretrieve('http://www.baidu.com', filename=os.path.join(os.getcwd(), 'file', 'file2.html'))

# urlretrieve在执行的过程当中，会产生一些缓存
# 清楚缓存
urllib.request.urlcleanup()
