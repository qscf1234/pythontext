import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('192.168.1.103', 8080))

while True:
    date = input('请输入给服务器发送的数据')
    if date == '断开连接':
        client.close()
        break
    client.send(date.encode('utf-8'))
    info = client.recv(1024)
    print("服务器说：", info.decode("utf-8"))
