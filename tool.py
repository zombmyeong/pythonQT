#_*_coding:utf-8_*_

import threading

#name, data info
#number 8000 ~
#connect 8000
#close 8001
#disconnection or somthing 8003
#recv disconnection 8004

#send start 8010
#recv success 8011

class clientManagement(threading.Thread) :

    def __init__(self, c, addr) :
        threading.Thread.__init__(self)
        self.c = c
        self.addr = addr
        self.input = ''

    def run(self) :
        self.c.send('8000\n')
        self.input = self.c.recv(1024)
        name, info = self.input.split(',')
        #sql

        self.c.send.('8010\n')
        while True :
            self.input = ''
            self.input = self.c.recv(1024)
            if self.input != '' and self.input is not None :
                if self.input == '8003' :
                    break
                elif self.input == '8004' :
                    self.c.send('8001\n')
                    break
                else :
                    self.c.send('8011\n') 


    def __del__(self) :
        print 'close : ', self.addr
        self.c.close()

