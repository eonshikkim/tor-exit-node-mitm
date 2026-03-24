import requests
import socks
import socket

# Configuring the local Tor container's proxy
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket

def send_plaintext():
    target_url = "http://httpbin.org/post"
    test_data = {
        'username': 'admin', 
        'password': 'password1234'
    }

    try:
        res = requests.post(target_url, data=test_data, timeout=10)
        if res.status_code == 200:
            print("[*] Request successful (200 OK)")
        else:
            print(f"[-] Unexpected status code: {res.status_code}")
            
    except Exception as e:
        print(f"[-] Connection failed. Is Tor running? Error: {e}")

if __name__ == "__main__":
    send_plaintext()