from socket import socket, AF_INET, SOCK_STREAM, setdefaulttimeout
from termcolor import colored

ip = "8.8.8.8"
port = 4
setdefaulttimeout(2)

try:
    sock = socket(AF_INET, SOCK_STREAM)
    result = sock.connect_ex((ip, port))
    if result == 0:
        print(colored("[+] Open!!", 'green'))
    else:
        print(colored("[-] Closed!!", 'red'))
    sock.close()
except Exception as e:
    print(colored(f"Error: {e}", 'red'))
