import time, sys, time, os

try:
    import requests
    from colorama import Fore, init
except (ModuleNotFoundError):
    os.system('pip install requests colorama')

from colorama import Fore, init
init(convert=True)
print(Fore.CYAN + """

 __          __  _     _____                       
 \ \        / / | |   / ____|                      
  \ \  /\  / /__| |__| (___  _ __   __ _ _ __ ___  
   \ \/  \/ / _ \ '_ \\___ \| '_ \ / _` | '_ ` _ \ 
    \  /\  /  __/ |_) |___) | |_) | (_| | | | | | |
     \/  \/ \___|_.__/_____/| .__/ \__,_|_| |_| |_|
                            | |                    
                            |_|                    

  
  """)
print(Fore.GREEN + "By PolarisWolf")
print(f'{Fore.CYAN}WebX:{Fore.RESET}\n\n1. {Fore.GREEN}Spam Webhook {Fore.RESET}[1]\n2. {Fore.RED}Delete Webhook {Fore.RESET}[2]\n')
print(f'\n{Fore.WHITE}Choice : {Fore.RESET}', end='')

choice = int(input(''))

if choice not in [1, 2]:
    print(f'---\n{Fore.BLUE}Webhook{Fore.RESET} -> {Fore.RED}Error{Fore.RESET} ')
    time.sleep(1)

if choice == 1:
    print(f"===========\n{Fore.RED}Webhook URL{Fore.RESET}")
    webhook = str(input(" > "))
    print(f"{Fore.BLUE}Message{Fore.RESET}")
    message = str(input(" > "))
    while True:
        _data = requests.post(webhook, json={'content': message}, headers={'Content-Type': 'application/json'})
        if _data.status_code == 204:
            print(f"{Fore.GREEN} Message Sended!")

if choice == 2:
  print(f"===========\n{Fore.RED}Webhook URL{Fore.RESET}")
  webhook = str(input(" > "))
  requests.delete(webhook)
