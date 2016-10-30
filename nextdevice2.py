import socket
import sys
import math
# Create a.txt TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('', 8891)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)

def dopow(num):
    print math.pow(num,2)


while True:
    # Wait for a.txt connection
    print >>sys.stderr, 'waiting for connection'
    connection, client_address = sock.accept()
    try:
        print >> sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)

            if data:
                #print >> sys.stderr, 'received "%s"' % data
                data=data.rstrip()
                print >> sys.stderr,int(data)/2.0
                #print >> sys.stderr, 'sending data back to the client'
                #connection.sendall(data)
            else:
                #print >> sys.stderr, 'no more data from', client_address

                connection.close()
                break

    finally:
        # Clean up the connection
        connection.close()
