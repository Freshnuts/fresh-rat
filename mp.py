import multiprocessing
import os
import time
import sys

# Need to implement when to end process and continue to in parent process.
# Time() is ineffective for scaling.

pool = multiprocessing.Pool()
q = multiprocessing.Queue()
l1 = multiprocessing.Lock()

def main():
    global cmd
    while 1:
        time.sleep(1)
        print "\nStart Process: ", os.getpid()
        print "======================"
        print "Menu:\n1. Send to all Procs.\n2. 1st Process Shell\n3. Quit"
        print "======================"
        option = raw_input("option #:> ")
        print ""
        if option == "1":
            print "Sending data to all clients."
            client01()
            q.put("id")
            term1()
            time.sleep(1)
            client02()
            q.put("id")
            term2()
        elif option == "2":
            client01shell()
            while True:
                cmd = raw_input("fresh#> ")
                q.put(cmd)
        elif option == "3":
            print "Quitting"
            exit()
        else:
            print "Error"


# Send Data to all Clients
def client01():
    global term1
    p  = multiprocessing.Pool(1, all_cmd,(q, )) # Function called, q as arg.
    def term1():
        p.terminate()
# Create Process for Interactive Shell With client #2.
def client02():
    global term2
    p = multiprocessing.Pool(1, all_cmd,(q, ))
    def term2():
        p.terminate()

def client01shell():
    global term1shell
    p = multiprocessing.Pool(1, shells)
    def term1shell():
        p.terminate()

def shells():
    print "Client Shell PID: %s" % os.getpid()
    item = q.get(True)
    os.system(cmd)

# Send command to all
def all_cmd(q):
    print "Client PID: %s" % os.getpid()
    item  = q.get(True)
    os.system(item)


main()
