import socket

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpSocket.bind(("0.0.0.0", 8000))
tcpSocket.listen(2)


while 1:
 print("Waiting for a Client ... ")
 (client, (ip, sock)) = tcpSocket.accept()

 print("Received connection from : ", ip)
 client.send("Press Return or Ctrl+C to close..\n")
 print("Starting ECHO output ... ")

 data = 'dummy'

 while len(data):
  data = client.recv(2048)
  if len(data)==1:
   print("Closing connection with ", ip)
   client.close()
   print("Connection closed successfully.!!")
   print("---------------------------------")
   break
  if len(data)==0:
   print("Some Error in connection with ", ip)
   print("Connection closed with ", ip)
   print("---------------------------------")
   break
  print("Client sent:", data)
  client.send(data)

tcpSocket.close()
