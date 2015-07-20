#_*_coding:utf-8_*_

import sys
import socket
import tool

HOST = ''
PORT = 57000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(10)
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
