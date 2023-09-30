import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format ("PoRT SCanneR")

target = input(str("Target Ip: "))

#Banner
print("_" * 50)
print("Scanning Target: " + target)
print("Scanning Target started at: " + (datetime.now()))
print("_" * 50)

try:
#Scan part

    for port in range(165545):
        socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefualttimeout(0.5)
            #How to turn back open port
        result = s.connect_ex(target,port)
        if result == 0:
            print("[*] Port is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\n Exiting :(")
    sys.exit()
except socket.error:
    print("\n Host not responding :(")
    sys.exit()