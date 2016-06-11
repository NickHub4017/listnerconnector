import socket
import sys
import time

import hashlib
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#
# class MyHandler(FileSystemEventHandler):
#     def on_modified(self, event):
#         print "Got it!"
#
# event_handler = MyHandler()
# observer = Observer()
# observer.schedule(event_handler, path='.', recursive=False)
# observer.start()

pipe_name = 'pipe_test'

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def makeconn(addr,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (addr, port)
    print >> sys.stderr, 'connecting to %s port %s' % server_address
    sock.connect(server_address)
    return sock;

prevmd5=0;

try:
    sock = makeconn('localhost', 8890)

    while (True):
        #data = sock.recv(16)
        #amount_received += len(data)
        #print >>sys.stderr, 'received "%s"' % data
        newmd5=md5("a.txt");

        if(prevmd5!=newmd5):
            prevmd5=newmd5;
            sock.close()

            f=open("a.txt")
            l=f.readline().split(",");
            p=l[0];
            q = int(l[1]);
            print p,q
            sock = makeconn(p,q)
        else:
            pipein = open(pipe_name, 'r')
            line = pipein.readline()[:-1]
            sock.sendall(line)




finally:
    print >>sys.stderr, 'closing socket'





