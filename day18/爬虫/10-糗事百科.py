import urllib.request
import ssl
import os
import re
import time

def jokeCrawler(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36"}
    req = urllib.request.Request(url, headers=headers)

    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)

    HTML = response.read().decode('utf-8')
    pat = r'<div class="author clearfix">(.*?)<div class="stats">'
    re_joke = re.compile(pat, re.S)
    divList = re_joke.findall(HTML)
    dic = {}

    for div in divList:
        re_u = re.compile(r"<h2>(.*?)</h2>", re.S)
        username = re_u.findall(div)
        username = username[0]
        # print(username.strip('\n'))
        re_d = re.compile(r'<span>(.*?)</span>', re.S)
        duanzi = re_d.findall(div)
        duanzi = duanzi[0]
        # print(duanzi.strip('\n'))
        dic[username.strip('\n')] = duanzi.strip('\n')
    return dic
'''
url = 'https://www.qiushibaike.com/text/page/1'
jokeCrawler(url)
'''
path = os.path.join(os.getcwd(), 'test.txt')
for i in range(1, 11):
    url = 'https://www.qiushibaike.com/text/page/' + str(i)
    info = jokeCrawler(url)
    for k, v in info.items():
        str1 = k + "说：\n" + v + '\n'
        print(str1, end=' ')
        with open(path, 'a+', encoding='utf-8') as f:
            f.write(str1)
    # time.sleep(0.00001)
