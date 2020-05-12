from multiprocessing import Process
import socket
import os
import signal

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpSocket.bind(("0.0.0.0", 8000))
tcpSocket.listen(2)

def conn_handler(client, ip, Child_id):
	print("[C%d]Received connection from : %r" % (Child_id, ip))
	print("[C%d]Starting echo output... " % Child_id)
	data = 'dummy'
	while len(data):
		data = client.recv(2048)
		if len(data)==0:
			print("[C%d]Closing connection with %r" % (Child_id, ip))
			client.close()
			print("[C%d]Connection closed with %r" % (Child_id, ip))
			os.kill(os.getpid(), signal.SIGTERM)
		print("[C%d]Client sent: %s" % (Child_id, data))
		client.send(data)

def main():
	Child_id = 0
	while 1:
		Child_id = Child_id + 1
		print("Waiting for Client  ...\n")
		(client, (ip, sock)) = tcpSocket.accept()

		try:
			Process(target=conn_handler, args=(client, ip, Child_id)).start()
		except:
			print("Error: Uable to start Child Process.!![C%d]" % Child_id)
	
	tcpSocket.close()


if __name__ == "__main__":
	main()
