from termcolor import colored
from modules.req import get
import subprocess

repo = "https://github.com/"

def logo():
    print()
    print(colored("           ██████╗ ████████╗███████╗", "light_blue"))
    print(colored("          ██╔═══██╗╚══██╔══╝██╔════╝" ,"light_blue"))
    print(colored("          ██║   ██║   ██║   █████╗ " , "light_blue"))
    print(colored("          ██║▄▄ ██║   ██║   ██╔══╝ " , "light_blue"))
    print(colored("          ╚██████╔╝   ██║   ██║ " , "light_blue"))
    print(colored("           ╚══▀▀═╝    ╚═╝   ╚═╝ ", "light_blue"))

    print()
    print("     Made by Skyrix                       simple tool about requests and responces with python") 
 
    print(colored(f"     Get source code from: {repo}", "dark_grey") + colored('                     type "help" to get commands', "yellow"))
    print(colored('     type "quit" to quit', "yellow"))
    print()  







