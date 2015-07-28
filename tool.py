#_*_coding:utf-8_*_
import socket
import threading
import time
import protocol
import MySQLdb.connector as mariadb

lock = threading.Lock()

class server () :
    def __init__(self, HOST, PORT, LISTEN) :
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((HOST, PORT))
        self.s.listen(LISTEN)
        self.s.settimeout(5)
        self.client = []
        self.status = True

class serverAccept(threading.Thread) :
    def __init__(self, server) :
        threading.Thread.__init__(self)
        self.server = server
        self.start()

    def run(self) :        
        while self.server.status : 
            c = None
            addr = None
            try:
                c, addr = self.server.s.accept()
                if c != None and addr != None :
                    t = clientManagement(c, addr)
                    with lock : self.server.client.append(t);
                    t.start()
            except Exception, e:
                time.sleep(0.5)

class serverRemove(threading.Thread) :
    def __init__(self, server) :
        threading.Thread.__init__(self)
        self.server = server
        self.start()

    def run(self) :
        while self.server.status :
            with lock :
                for c in self.server.client :
                    if not c.isAlive() :
                        del c
            time.sleep(5)

class clientManagement(threading.Thread) :

    def __init__(self, c, addr) :
        threading.Thread.__init__(self)
        self.c = c
        self.addr = addr

    def run(self) :
        self.c.send(protocol.CLIENT_CONNECT+'\n')
        self.input = self.c.recv(1024)
        name, pswd, info = self.input.split(',')

        #sql
        self.mariadb_connection = mariadb.connect(user = name, password = pswd, database='myapp')
        self.cursor = self.mariadb_connection.cursor()

        self.c.send(protocol.CLIENT_SEND_START+'\n')
        while True :
            self.input = ''
            self.input = self.c.recv(1024)
            if self.input != '' and self.input is not None :
                if self.input == protocol.CLIENT_RECV_DISCONNECT :
                    self.c.send(protocol.CLIENT_CLOSE+'\n')
                    break
                else :
                    cursor.excute("INSERT INTO xxxxx VALUES (%d, %d)",( xxxx ,self.input))
                    self.c.send(protocol.CLIENT_RECV_SUCCESS+'\n') 


    def __del__(self) :
        print 'close : ', self.addr
        self.c.close()
