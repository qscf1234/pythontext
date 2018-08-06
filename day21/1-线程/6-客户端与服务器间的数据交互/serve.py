import socket
import threading


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定IP端口
server.bind(('192.168.1.103', 8080))
# 监听 代表可建立socket连接的最大个数
server.listen(5)
print("服务器启动成功……")


'''
while True:
    #等待客户端链接
    clientSocket, clientAddress = server.accept()
    #启动一个线程，将当前链接的clientSocket交给线程
'''

def recover(clientSocket):
    while True:
        try:
            data = clientSocket.recv(1024)
            print("客户端说：" + data.decode("utf-8"))
            sendData = str(clientSocket)
            print(sendData)
            clientSocket.send(sendData.encode("utf-8"))
        except ConnectionAbortedError as e:
            break


while True:
    # 等待链接
    clientSocket, clientAddress = server.accept()
    print("%s --  %s 链接成功" % (str(clientSocket), clientAddress))
    p = threading.Thread(target=recover, args=(clientSocket,))
    p.start()
