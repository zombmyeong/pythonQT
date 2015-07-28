#_*_coding:utf-8_*_

import sys
import socket
import tool

HOST = ''
PORT = 57000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(10)
s.settimeout(1)
client = []

def main() :
    try:
        while True :
            c = None
            addr = None

            c, addr = s.accept()
            if c != None and addr != None :
                t = tool.clientManagement(c, addr)
                client.append(t);
                t.start()
                print 'connected : ', addr

            for c in client :
                if not c.isAlive() :
                    del c
    finally:
        s.shutdown(SHUT_RDWR)
        s.close()

if __name__ == '__main__' :
    main()
