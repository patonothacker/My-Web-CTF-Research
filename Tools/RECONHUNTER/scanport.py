import socket
import argparse
import concurrent.futures

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        s.settimeout(2) 
        
        result = s.connect_ex((target, port))
        
        if result == 0:
            try:
                
                banner = s.recv(1024).decode().strip()
                if banner:
                    print(f"[+] Port {port} is OPEN | Banner: {banner}")
                else:
                    print(f"[+] Port {port} is OPEN | (No banner returned)")
            except:
                
                print(f"[+] Port {port} is OPEN | (Not banner)")
            if port in [80, 443, 8080, 8443]:
                found_web = True
        s.close()
    except socket.error:
        pass
    return found_web

def main():
    parser = argparse.ArgumentParser(description="PortHunter - Minimalist TCP Port Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target IP or Hostname (e.g., 192.168.1.1 or scanme.nmap.org)")
    parser.add_argument("-sp", "--start-port", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("-ep", "--end-port", type=int, default=65535, help="End port (default: 65535)")
    
    args = parser.parse_args()
    target = args.target
    start_port = args.start_port
    end_port = args.end_port

    print(f"[*] Starting TCP port scan on target: {target}")
    print(f"[*] Scanning ports from {start_port} to {end_port} ...\n")

    
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, target, port)
            
    print("\n[*] Scan completed.")

if __name__ == "__main__":
    main()
