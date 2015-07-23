#_*_coding:utf-8_*_

import threading

class clientManagement(threading.Thread) :

    def __init__(self, c, addr) :
        threading.Thread.__init__(self)
        self.c = c
        self.addr = addr
        self.input = ''

    def run(self) :
        self.c.send('thanx for connecting\n')
        while True :
            self.input = self.c.recv(1024)
            print self.input
            if float(self.input) > 300 :
                break
    
    def __del__(self) :
        print 'close : ', self.addr
        self.c.send('good bye\n')
        self.c.close()

