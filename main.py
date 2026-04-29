
from termcolor import colored
from modules.req import get
import subprocess
from modules.logo import logo  
from modules.post import post
import time
from modules.help import help

time.sleep(2)
subprocess.run(["clear"])

islog = False


if __name__ == "__main__":
    islog = True
    logo()
else:
    print(colored("Please run the script as main, not imported!", "red"))




while islog:
    inp = input("qtf> ")

    if inp.lower() == "quit":
        print(colored("Quiting!", "yellow"))
        islog = False
    elif inp.lower() == "get":
        get()

    elif inp.lower() == "clear":
        subprocess.run(["clear"])
        logo()
    elif inp.lower() == "help":
        help()
    elif inp.lower() == "post":
        post()
    else:
        print(colored(f"{inp} : is not a valid command!", "red") + colored(' type "help" to get commands', "yellow"))

