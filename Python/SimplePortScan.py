from socket import *
from termcolor import colored

setdefaulttimeout(2)
sock = socket(AF_INET,SOCK_STREAM)
try:
    if(sock.connect_ex(("192.168.56.1",22))):
        print(colored("[-] Colosed!!",'red'))
except:
    print(colored("[+] Open!!",'green'))