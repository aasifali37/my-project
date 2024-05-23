from socket import *

def retBanner(ip, port):
    try:
        setdefaulttimeout(20)
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((ip, port))
        banner = sock.recv(1024)
        sock.close()
        return banner
    except timeout:
        return "Connection timed out"
    except Exception as e:
        return f"Error: {e}"
    
def main():
    port = 443
    ip = "8.8.8.8"
    banner = retBanner(ip, port)
    if banner:
        if isinstance(banner, bytes):
            banner = banner.decode('utf-8', 'ignore')
        print(f"[+] {ip}:{port} - {banner}")
    else:
        print(f"[-] {ip}:{port} - No banner received")

if __name__ == "__main__":
    main()
