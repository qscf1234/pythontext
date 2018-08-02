import urllib.request
import random

url = 'http://www.baidu.com'
'''
# 模拟请求头
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
# 设置一个请求体
req = urllib.request.Request(url, headers=headers)
# 发起请求
response = urllib.request.urlopen(req)
date = response.read()
print(date.decode('utf-8'))
'''

agentsList = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0"
]
agentStr = random.choice(agentsList)
req = urllib.request.Request(url)
# 向请求体里添加了User-Agent
req.add_header("User-Agent", agentStr)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
