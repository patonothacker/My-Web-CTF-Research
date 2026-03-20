import requests
import argparse
import concurrent.futures 


def check_url(word, target_url):
    test_url = target_url.replace("test", word)
    try:
        
        response = requests.get(test_url, timeout=5)
        if response.status_code == 200:
            print(f"[+] Found: {test_url}")
    except requests.exceptions.RequestException:
        pass 

def main():
    parser = argparse.ArgumentParser(description="DirHunter - Targeted URL Discovery Tool")
    parser.add_argument("-u", "--url", required=True, help="Target URL (must contain 'test')")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to the wordlist file")
    
    parser.add_argument("-t", "--threads", type=int, default=20, help="Number of concurrent threads (default: 20)")
    
    args = parser.parse_args()
    target_url = args.url
    wordlist_file = args.wordlist
    threads = args.threads

    if "test" not in target_url:
        print("[-] Error: Invalid Target URL. It must include the 'test' placeholder to define the injection point.")
        print("[-] Example: python dirhunter.py -u http://target.com/test -w words.txt")
        return

    print(f"[*] Fuzzing target: {target_url} with {threads} threads...\n")

    try:
        
        with open(wordlist_file, "r") as file:
            words = [line.strip() for line in file if line.strip()]
        
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            
            for word in words:
                executor.submit(check_url, word, target_url)
                
    except FileNotFoundError:
        print(f"[-] Error: File not found. Please check the path to '{wordlist_file}'")

if __name__ == "__main__":
    main()
