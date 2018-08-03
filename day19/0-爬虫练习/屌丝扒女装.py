import urllib.request
import os
import ssl
import re
import time

def imageSpider(url, toPath):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36"}
    req = urllib.request.Request(url, headers=headers)

    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)

    HTMLStr = response.read()
    with open(os.path.join(toPath, 'file1.html'), 'wb') as f:
        f.write(HTMLStr)
    # <img src="//img14.360buyimg.com/n7/s230x322_jfs/t18349/300/1767127918/124538/fdc80b03/5ad8645cNaf289cc3.jpg!cc_230x322.jpg"/>
    # //img20.360buyimg.com/n7/s230x322_jfs/t20440/151/2422179907/253174/5ffa16d3/5b553602N7a2657c8.jpg!cc_230x322.jpg
    pat = r'<img src="([0-9a-zA-Z_/ .?=:.!]*?)"/>'
    re_image = re.compile(pat, re.S)
    imageList = re_image.findall(HTMLStr.decode('utf-8'))
    print(type(imageList[0]))
    num = 1
    for imageUrl in imageList:
        path = os.path.join(toPath, str(num) + '.jpg')
        num += 1
        # 把图片下载下来
        print(imageUrl)
        imageUrl1 = 'http:' + imageUrl
        print(imageUrl1)
        urllib.request.urlretrieve(imageUrl1, filename=path)


toPath = os.path.join(os.getcwd(), 'image')
print(toPath)
url = 'https://search.yhd.com/c9719-0-0'
imageSpider(url, toPath)
