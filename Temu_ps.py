import socket
from concurrent.futures import ThreadPoolExecutor
from functools import partial
import sys

#User guideline for Temu_ps (Temu_PortScanner)

#Demo syntax
    #python3 Temu_ps [ip_address] [specific port/port range] [# of threads]

#Multi-port scan 
    #Example use: python3 Temu_ps 192.168.1.4 1-500 10
    # 192.168.1.4 --> ip addr (you already know this but wtv)
    # 1-500 --> port range between 1 and 500
    # 10 --> The number of threads that will be used. Recommended is around  100-200, don't overdo it.
    
#Single-port scan
    #Example use: python3 Temu_ps 192.168.1.4 80 10
    # 192.168.1.4 --> ip addr 
    # 80 --> Specific port that you want to enumerate lightly
    # 10 --> Same as before, the number of threads you use


#Colors to make it less boring and a bit appealing ;)
CYAN = '\033[36m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[0m'


def port_status(addr, port):
    try:
        conn = socket.socket()
        status = conn.connect_ex((addr, port)) #gives an error number based on port reachability (example: 0, 113, 111...)
    
        if status == 0:
            return print(f"Port {CYAN}{port}{RESET} is {GREEN}OPEN{RESET}")
    finally:
        conn.close()

#the number of threads that will be used during the enumeration process
num_of_threads = int(sys.argv[3])
HOST = str(sys.argv[1])

if '-' in sys.argv[2]:

    #List for ports and the same host IP address to satisfy map requirements
    port_list = []
    Host_list = []
    PORT = str(sys.argv[2])
    
    try:
        port_val = PORT.split('-')
        for ports in range(int(port_val[0]), int(port_val[1])+1):
            port_list.append(ports)
            
            for vals in port_list:
                Host_list.append(HOST)

        with ThreadPoolExecutor(max_workers=num_of_threads) as executor:
            executor.map(port_status, Host_list, port_list)   
    finally:
        print(f"\nScan complete! {YELLOW}(If nothing is displayed then no ports were found){RESET}")

    
    #Single port scan
else:
    PORT = int(sys.argv[2])
    try:
        port_status(HOST, PORT)
    finally:
        print(f"\nScan complete! {YELLOW}(If nothing is displayed then no ports were found){RESET}")             
   
