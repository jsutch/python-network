import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port on the server given by the caller
#server_address = (sys.argv[1], 10000)
server_address = (sys.argv[1], 8000)
print('connecting to %s port %s' % server_address, file=sys.stderr)
sock.connect(server_address)

try:
    
    message = b'message.'
    print('sending "%s"' % message, file=sys.stderr)
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received "%s"' % data, file=sys.stderr)

finally:
    sock.close()
