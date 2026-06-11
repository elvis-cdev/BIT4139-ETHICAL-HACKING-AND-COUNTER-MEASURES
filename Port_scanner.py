import socket
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

target = input("Enter target (e.g. github.com): ")
print(f"\nScanning {target}")
print(f"Started at: {datetime.now()}\n")

open_ports = []

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} OPEN")
            open_ports.append(port)
        sock.close()
    except:
        pass

try:
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(scan_port, range(1, 1025))

except KeyboardInterrupt:
    print("\nScan interrupted.")
    sys.exit()

print(f"\nScan complete at: {datetime.now()}")
print(f"Open ports found: {sorted(open_ports)}")
