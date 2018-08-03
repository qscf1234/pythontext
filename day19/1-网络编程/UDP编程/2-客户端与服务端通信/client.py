import socket

udpClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = input('请输入数据：')
    udpClient.sendto(data.encode('utf-8', ), ('192.168.1.103', 8090))
    data, addr = udpClient.recvfrom(1024)
    print('服务端说：', data)
