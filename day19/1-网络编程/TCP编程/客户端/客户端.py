import socket
'''
客户端：创建TCP链接时，主动发起连接的叫做客户端
服务端：接收客户端的连接
'''
# 1、创建一个socket
# 参数1：指定协议  AF_INET  或 AF_INET6
# 参数2：SOCK_STREAM执行使用面向流的TCP协议
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2、建立连接
# 参数：是一个元组，第一个元素为要连接的服务器的IP地址，第二个参数为端口
sk.connect(('www.sina.com.cm', 80))

# 3、请求数据
sk.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 4、等待接受数据
data = []
while True:
    # 每次接受1K数据
    tempData = sk.recv(1024)
    if tempData:
        data.append(tempData)
    else:
        break

dataStr = (b''.join(data)).decode('utf-8')

# 断开链接
sk.close()
# print(dataStr)

headers, HTML = dataStr.split('\r\n\r\n', 1)
print(headers)
print(HTML)
