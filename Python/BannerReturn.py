from socket import *

def retBanner(ip,port):
    try:
        setdefaulttimeout(2)
        sock = socket()
        sock.connect((ip,port))
        banner = sock.recv(1024)
        return banner
    except:
        return
    
def main():
    port = 22
    ip = "192.168.56.1"
    banner = retBanner(ip,port)
    if banner:
        print(f"[+] {ip}: {banner}")