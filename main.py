#_*_coding:utf-8_*_

import sys
import time
import tool

server = tool.server('', 57000, 10)

acceptThread = tool.serverAccept(server)
removeThread = tool.serverRemove(server)

def main() :
    try:
        while True :
            instruction = raw_input('>>>')
            if instruction != '' and instruction != None :
                if instruction == 'quit' :
                    break
            time.sleep(1)

    finally:
        server.status = False
        acceptThread.join()
        removeThread.join()
        server.s.close()

if __name__ == '__main__' :
    main()
    print 'end'