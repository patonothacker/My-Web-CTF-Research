import subprocess
import os
import socket

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def get_valid_path(prompt):
    while True:
        path = input(prompt)
        if os.path.exists(path):
            return path
        print(f"Error: File not found at '{path}'. Please try again!")

def main_menu():
    while True:
        clear_screen()
        print("="*60)
        print("          RECON TOOL BY PATO")
        print("="*60)
        print(" 1. Run SUBHUNTER   (Subdomain Discovery)")
        print(" 2. Run SCANPORT    (Port & Banner Scanning)")
        print(" 3. Run DIRHUNTER   (Directory Fuzzing)")
        print(" 4. ALL-IN-ONE      (Full Chain: Sub -> Port -> Dir)")
        print("-" * 60)
        
        choice = input("Select an option (1-4): ")

        if choice == '1':
            domain = input("Enter Domain (e.g., google.com): ")
            w_list = get_valid_path("Enter Subdomain Wordlist path: ")
            output = input("Output filename (e.g., subs.txt): ")
            subprocess.run(f"python3 subhunter.py -d {domain} -w {w_list} -o {output}", shell=True)

        elif choice == '2':
            target = input("Enter Target IP or Hostname: ")
            sp = input("Start Port (default 1): ") or "1"
            ep = input("End Port (default 65535): ") or "65535"
            subprocess.run(f"python3 scanport.py -t {target} -sp {sp} -ep {ep}", shell=True)

        elif choice == '3':
            url = input("Enter Target URL (must include 'test'): ")
            w_list = get_valid_path("Enter Directory Wordlist path: ")
            subprocess.run(f"python3 dirhunter.py -u {url} -w {w_list}", shell=True)

        elif choice == '4':
            
            domain = input("Enter Target Domain (e.g., google.com): ")
            sub_w = get_valid_path("Enter Subdomain Wordlist: ")
            dir_w = get_valid_path("Enter Directory Wordlist: ")
            sub_file = "found_subs.txt"

            if os.path.exists(sub_file): os.remove(sub_file)

            print(f"\nPHASE 1: Enumerating Subdomains...")
            subprocess.run(f"python3 subhunter.py -d {domain} -w {sub_w} -o {sub_file}", shell=True)

            if not os.path.exists(sub_file) or os.path.getsize(sub_file) == 0:
                print("No subdomains found. Terminating process.")
            else:
                with open(sub_file, "r") as f:
                    subdomains = [line.strip() for line in f if line.strip()]
                
                print(f"\nPHASE 2 & 3: Port Scan & Path Fuzzing for {len(subdomains)} subdomains...")
                for sub in subdomains:
                    print(f"\n" + "-"*40 + f"\n[!] TARGET: {sub}\n" + "-"*40)
                   
                    subprocess.run(f"python3 scanport.py -t {sub} -sp 80 -ep 443", shell=True)
                    
                    
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(1)
                    if s.connect_ex((sub, 80)) == 0:
                        print(f"Web Service Detected! Launching DirHunter...")
                        subprocess.run(f"python3 dirhunter.py -u http://{sub}/test -w {dir_w}", shell=True)
                    s.close()

        input("\nPress Enter to return to Menu...")

if __name__ == "__main__":
    main_menu()
