import pyfiglet
import sys
import socket
from datetime import datetime
from threading import Thread, Lock

target = input(str("Target IP:"))

# Create a lock to synchronize access to lst
lst_lock = Lock()
lst = []

# Banner
print("_" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("_" * 50)

def scan_ports(target, ports_range):
    try:
        for port in ports_range:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)

            result = s.connect_ex((target, port))
            s.close()

            if result == 0:
                with lst_lock:
                    if port not in lst:
                        print("[*] Port {} is open".format(port))
                        lst.append(port)

    except KeyboardInterrupt:
        print("\nExiting :(")
        sys.exit()

    except socket.error:
        print("Host not responding :(")
        sys.exit()

def divide_ports(num_threads, total_ports):
    ports_per_thread = total_ports // num_threads
    port_ranges = []

    for i in range(num_threads):
        start_port = i * ports_per_thread + 1
        end_port = (i + 1) * ports_per_thread if i < num_threads - 1 else total_ports
        port_ranges.append(range(start_port, end_port + 1))

    return port_ranges

threads = []
num_threads = 6  # You can adjust the number of threads for performance
total_ports = 65535  # Total number of ports

port_ranges = divide_ports(num_threads, total_ports)

for port_range in port_ranges:
    t = Thread(target=scan_ports, args=(target, port_range))
    t.start()
    threads.append(t)

for t in threads:
    t.join() 