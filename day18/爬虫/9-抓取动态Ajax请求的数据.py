import urllib.request
import ssl
import json

def ajaxCrawler(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36"}
    req = urllib.request.Request(url, headers=headers)

    # 使用ssl创建未验证的上下文
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)

    jsonStr = response.read().decode("utf-8")
    jsonData = json.loads(jsonStr)

    return jsonData

'''
url1 = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=1'
info = ajaxCrawler(url1)
print(info)
'''
for i in range(1, 11):
    url2 = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=' + str(i * 20) + '&limit=1'
    info = ajaxCrawler(url2)
    print(info)
