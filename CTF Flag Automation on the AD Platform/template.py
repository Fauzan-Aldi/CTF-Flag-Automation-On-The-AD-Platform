import requests
import multiprocessing
import time
import os
import sys
from dotenv import load_dotenv
load_dotenv()

HOST        = f"{os.getenv('HOST')}"
TOKEN       = f"{os.getenv('TOKEN')}"
TEAM_NAME   = f"{os.getenv('TEAM')}"
FLAG_FORMAT = f"{os.getenv('FLAG')}"

ATTDEF_SERVER = f"https://{HOST}/api/user/"
CHALL_PORT = 0000     
if not TOKEN:
  print("[-] Token not found")
  sys.exit(1)

def exploit(target_ip, port):
  try:


    flag = "GEMASTIK{test}"
    if FLAG_FORMAT not in flag:
      raise Exception("Flag not found")
    
    return flag
  except Exception as e:
    print(f"[-] Error: {e} ({target_ip})")

def process_exploit(target_ip, port, target_id):
  try:
    print(f"[+] Target IP: {target_ip}")
      
    flag = exploit(target_ip, CHALL_PORT)
    
    if not flag:
      print(f"[-] Exploit failed to team {target_id} ({target_ip})")
      return
      
    print(f"[+] Flag: {target_id} {flag}")
      
    requests.post('http://localhost:3000/submit', json={'flag': [flag]})
  except Exception as e:
    print(f"[-] Error: {e}")

def main():
  target_ip_list = requests.get(ATTDEF_SERVER).json()['data']
  target_ip_list = { x['username']: x['ip'] for x in target_ip_list}
  target_ip_list.pop(TEAM_NAME)
  
  timer = 0
  while True:
    if timer > 0:
      print(f"[+] Next Exploit in: {timer} seconds", end="\r")
      timer -= 1
      time.sleep(1)
      continue
    
    for target_id, target_ip in target_ip_list.items():
      process = multiprocessing.Process(target=process_exploit, args=(target_ip, CHALL_PORT, target_id))
      process.start()

    timer = 300 # Tick in seconds

if __name__ == "__main__":
  main()