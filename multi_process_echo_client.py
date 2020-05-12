import socket
import sys
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSocket.connect((sys.argv[1], int(sys.argv[2])))
print("Input some string : ['quit' to exit]")
data = "dummy"
while 1:
	data = input("|> ")
	if data=="quit":
		tcpSocket.close()
		break
	tcpSocket.sendall(data)
	result = tcpSocket.recv(2048)
	print(result)  
