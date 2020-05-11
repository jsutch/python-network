import threading
import socket

"""
Updated to use Python3 and the threading module
"""

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpSocket.bind(("0.0.0.0", 8000))
tcpSocket.listen(2)

def conn_handler(client, ip, thread_id):
	print("[T%d]Received connection from : %r" % (thread_id, ip))
	client.send(b"Press Return or Ctrl+C to close..\n") # need bytes object
	print("[T%d]Starting echo output..." % thread_id)
	data = 'dummy'
	while len(data):
		data = client.recv(2048)
		if len(data)==1:
			print("[T%d]Closing connection with %r" % (thread_id, ip))
			client.close()
			print("[T%d]Connection closed successfully.!!" % thread_id)
			print("------------------------------------")
			break
		if len(data)==0:
			print("[T%d]Some Error in connection with %r" % (thread_id, ip))
			print("[T%d]Connection closed with %r" % (thread_id, ip))
			print("------------------------------------")
			break
		print("[T%d]Client sent: %s" % (thread_id, data))
		client.send(data)


thread_id = 0
while 1:
	thread_id = thread_id + 1
	print("Waiting for Client ...\n")
	(client, (ip, sock)) = tcpSocket.accept()

	try:
		#_thread.start_new_thread(conn_handler, (client, ip, thread_id, ))
                thread = threading.Thread(target=conn_handler(client, ip, thread_id,))
	except:
		print("Error: Unable to start thread [T%d]\n" % thread_id)

tcpSocket.close()
