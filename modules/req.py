from termcolor import colored
import requests
import time

def get():
    url = input("Enter target url> ")


    response = requests.get(url)


    connected = False

    while not connected:
        if response.status_code == 200:
            print(colored("Success!","green"))
            print(f"Status code: {response.status_code}")
            print(response.json())
            connected = True
        else:
            print(colored("Failed!", "red"))
            print(colored("Please check the url that you entered!", "yellow"))
            time.sleep(3) 

