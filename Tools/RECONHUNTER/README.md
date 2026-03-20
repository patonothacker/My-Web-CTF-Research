```
██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ 
 ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
 ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
 ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
 ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
 ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                      Created by Pato
```
***ReconHunter*** is a powerful, multi-threaded reconnaissance suite designed to automate the initial phases of a security assessment. By chaining subdomain enumeration, intelligent port scanning, and directory fuzzing, it provides a seamless workflow from discovery to vulnerability identification.

# Key Features
- ***Subdomain Discovery***: High-speed brute-forcing using custom wordlists to map out an organization's attack surface.
- ***Intelligent Port Scanning***: Leverages Banner Grabbing to identify running services and their specific versions (SSH, FTP, HTTP, etc.).
- ***Automated Directory Fuzzing***: Detects hidden paths, configuration files, and sensitive directories on discovered web servers.
- ***Smart Chain Logic***: The "All-in-One" mode automatically pipes discovered subdomains into the port scanner and triggers directory fuzzing only when web services are detected.

# Installation
ReconHunter is optimized for Kali Linux. Ensure you have Python 3 installed.
1. Clone the repository:
```
git clone https://github.com/patonothacker/My-Web-CTF-Research.git
cd My-Web-CTF-Research/Tools/RECONHUNTER
```
2. Install dependencies:
```
pip install requests
```
# Usage
1. Wordlist
```
sudo apt install wordlists
```

2. Master Control (All-in-One Mode)

   This mode automates the entire recon process: ***Subdomains -> Ports -> Paths***.
```
python3 ReconHunter.py
```
3. Standalone Modules

   You can also run each tool independently; for more detailed usage instructions, please use the -h option:
   - Subdomain Hunter:
     ```python3 subhunter.py -d target.com -w /path/to/wordlist -o results.txt```
     
   - Port Hunter (with Banner Grabbing):
     ```python3 scanport.py -t 0.0.0.0 -sp 1 -ep 1000```
     
   - Directory Hunter:
     ```python3 Dirhunter.py -u host -w wordlists```

# Disclaimer
This tool is intended for educational purposes and authorized security testing only. The author (Pato) is not responsible for any misuse or damage caused by this program. Always obtain proper authorization before scanning any network or web application.

