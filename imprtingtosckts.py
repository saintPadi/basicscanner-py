import sys
import socket
from datetime import datetime

if  len(sys.argv) == 1 or sys.argv[1] == "--help" :
    
    print ("Invalid syntax !!")#Control Statement for if syntax error is committed.
    print ("Syntax :python3 scanner.py <ip>")#Correct Syntax

else:
    target = socket.gethostbyname(sys.argv[1]) #Translate the hostname to IPV4 addr
    port = sys.argv[2]
#Printing a pretty Banner.
    print("-"*50)
    print("Scanning target :"+target )
    print("Time Started: "+str(datetime.now()))
    print("-"*50)

    try :   
        for port in range(50,85):
            s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            result = s.connect_ex((target,port))
            if result == 0:
                print("Port {port}is open")
                s.close()
    except KeyboardInterrupt:
        print("\nExiting Program!!")    
        sys.exit()

    except socket.gaierror :
        print("Hostname did not resolve!!") 
        sys.exit()

    except socket.error :
        print("Could not connect to Server!!!")    
        sys.exit()

