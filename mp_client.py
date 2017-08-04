import sys
import os
import socket
import subprocess

host = '127.0.0.1'
port = 443


# Create Socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print msg

# Connect to Server
try:
    s.connect((host, port))
except socket.error, msg:
    print msg

while 1:
    read = s.recv(1024)
    if read == "1":
        print "Recovered Number: ", read
        result = os.popen("uname -norm").read()
        s.send(result)
    elif read == "2":
        print "Option 2"
        s.close()
        exit()
    elif read == "3":
        s.close()
        print "Quit"
        exit()
    else:
        print "recv error"
        s.close()
        exit()
