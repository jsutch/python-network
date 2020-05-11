# banner.py

import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP

t_host = str(input("Enter the host name: "))
t_port = int(input("Enter Port: "))

message='GET HTTP/1.1 \r\n'
sock.connect((t_host,t_port))
sock.send(message.encode())

ret = sock.recv(1024)
print('[+]' + str(ret))
