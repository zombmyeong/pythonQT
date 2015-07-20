#_*_coding:utf-8_*_

import threading

class clientManagement(threading.Thread) :

    def __init__(self, c, addr) :
        threading.Thread.__init__(self)
        self.c = c
        self.addr = addr
        self.c.send('thanx for connecting')

    def run(self) :
        pass

    def __del__(self) :
        c.send('good bye')
        c.close()

