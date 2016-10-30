
import socket
import sys
import time

import hashlib

prevmd5=0;

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

while True:
    newmd5 = md5("a.txt");
    sock = makeconn('localhost', 8502)
    cmd=raw_input("Enter server,ipz :- ")
    sock.sendall(cmd)
    sock.close()
