from termcolor import colored
import requests
import time



def post():
    url = input("Enter target url> ")


    connected = False

    while not connected:
        print(colored("format: {str:Any} !", "yellow" ))
        data = input("Enter data with the json format>")
        request = requests.post(url, data)
        if request.status_code == 201:
            print(colored("Success!", "green"))
            print(f"code status: {request.status_code}")
            print(request.json())
            connected = True
        else:
            print(colored("Failed! ", "red") + colored(request.status_code, "red"))
            time.sleep(2)