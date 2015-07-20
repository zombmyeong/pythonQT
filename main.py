#_*_coding:utf-8_*_

import sys
import socket
import tool

s = socket.socket()
host = socket.gethostname()
port = 65888
s.bind((host,port))
s.liten(10)
client = []

def main() :
    while True :
        c, addr = s.accept()
        t = tool.clientMangement(c, addr)
        client.append(t);
        t.start()
        print 'connected', addr

    for c in client :
        del c

if __name__ == '__main__' :
    main()
