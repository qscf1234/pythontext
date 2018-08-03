import urllib.request
import ssl
import re
import os.path
from collections import deque

def writeFileBytes(htmlBytes, toPath):
    with open(toPath, 'wb') as f:
        f.write(htmlBytes)
def writeFileStr(htmlBytes, toPath):
    with open(toPath, 'w', encoding='utf-8') as f:
        f.write(htmlBytes.decode('utf-8'))
def getHtmlBytes(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)
    return response.read()
def QQSpider(url, toPath):
    htmlBytes = getHtmlBytes(url)
    # writeFileBytes(htmlBytes, os.path.join(os.getcwd(), 'File1.html'))
    # writeFileStr(htmlBytes, os.path.join(os.getcwd(), 'File2.html'))
    htmlStr = htmlBytes.decode('utf-8')

    # 查找QQ
    pat = r'[1-9]\d{5,13}'
    re_qq = re.compile(pat)
    qqList = re_qq.findall(htmlStr)
    # 去重
    qqList = list(set(qqList))
    for qqStr in qqList:
        f = open(os.path.join(os.getcwd(), 'qqFile.txt'), "a", encoding='utf-8')
        for qqStr in qqList:
            f.write(qqStr + "\n")
        f.close()

    # 查找网页
    pat = r'(((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?)'
    re_url = re.compile(pat)
    urlList = re_url.findall(htmlStr)
    # 去重
    urlList1 = []
    for url1 in urlList:
        urlList1.append(url1[0])
    urlList1 = list(set(urlList1))
    return urlList1

def center(url, toPath):
    queue = deque()
    queue.append(url)
    while len(queue) != 0:
        targetUrl = queue.popleft()
        urlList = QQSpider(targetUrl, toPath)
        for tempUrl in urlList:
            queue.append(tempUrl)

url = 'https://www.douban.com/group/topic/20285003/'
# toPath = os.path.join(os.getcwd(), 'qqFile.txt')
center(url, os.getcwd())
