import multiprocessing
import os
import Queue
import signal
import socket
import sys
from multiprocessing import Manager
import time

# Process 1
print "Start PID: ", os.getpid()


host = ''
port = 443
i = 0

def connect_s():
    global s
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
        print msg
        exit()


def bind_s():
    try:
        s.bind((host, port))
    except socket.error, msg:
        print msg
        exit()


def listen_s():
    try:
        s.listen(3)
    except socket.error, msg:
        print msg
        exit()

def client_p(conn):
    print "PID: ", os.getpid()
    print "Connected to %s on port %s." % (addr[0], addr[1])
    while True:
        data = conn.recv(1024)
        if data:
            print data
        else:
            print "client_p() Error"
            print "Removing Client: %s %s" % (addr[0], addr[1])
            # pop() removes final last element in list.
            # Works correct except for debugging on 127.0.0.1,
            # if 3x localhost connects, server will delete the
            # first 127.0.0.1 found on list, regardless on client #3.
            l.remove(str(addr[0]))
            l.remove(str(addr[1]))
            print l
            break

# Accept
def asc(l):
    global i
    global conn
    global addr
    while True:
        try:       
            conn, addr = s.accept()
            time.sleep(1)
            p = multiprocessing.Process(target=client_p, args=(conn, )) #P3
            p.start()
            conn.send("1")
            l.append(str(addr[0]))
            l.append(str(addr[1]))
            i += 1
            print "\nTotal Connection Made: %d" % i
        except socket.error:
            print "Cannot accept Target."
        time.sleep(1)




# Process 1   - Main menu loop
# Process 2   - asc(l) (Accept Clients Function)
# Process 3   - client_p (Client Intro)
# Process 4-9 - New Client/Server connections

connect_s()
bind_s()
listen_s()
l = Manager().list()
wp = multiprocessing.Process(target=asc, args=(l, )) # Process 2
wp.start()
while True:
    print "\nMenu\n====\n1. Show Targets\n2. Choose Single Target\n3. Quit"
    read = raw_input("\n:> ")
    if read == "1":
        print "Client Target List\n=================="
        try:
            l[0]
            l[1]
            print "IP: %s\tPort: %s" % (l[0], l[1])
        except:
            continue 
        try:
            l[2]
            l[3]
            print "IP: %s\tPORT: %s" % (l[2], l[3])
        except:
            continue
        try:
            l[4]
            l[5]
            print "IP: %s\tPORT: %s" % (l[4], l[5])
        except:
            continue
        raw_input("Press Enter")
        os.system("clear")
    elif read == "2":
        print "Select a Target:"
        c = 1
        n = 0
        while n < 6:
            try:
                l[n]
            except:
                continue
            print "%d. IP: %s\tPORT: %s" % (c, l[n], l[n+1])
            try:
                l[n+2]
            except:
                break
            c += 1
            n += 2

        opt2read = raw_input("Choose a Target: > ")
        if opt2read == "1":
            try:
                l[0]
                l[1]
                print "\nIP: %s Port: %s" % (l[0], l[1])
            except: 
                print "Error: User Input"
        elif opt2read == "2":
            try:
                l[2]
                l[3]
                print "\nIP: %s PORT: %s" % (l[2], l[3])
            except:
                print "Error: User Input"
        elif opt2read == "3":
            try:
                l[4]
                l[5]
                print "\nIP: %s PORT: %s" % (l[4], l[5])
            except:
                print "Error User Input"
        raw_input("Press Enter")
        os.system("clear")
    elif read == "3":
        print "Exit."
        break
    time.sleep(1)
    os.system("clear")

sys.exit()
