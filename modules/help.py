from termcolor import colored



def help():
    print("Help commands:") 

    print(colored("  clear,", "blue")+ colored("      Clears your interface."))

    print(colored("  get,", "blue")+ colored("        Get json data from an authorised webapp."))

    print(colored("  help,", "blue")+ colored("       Get help for commands"))  

    print(colored("  quit,", "blue")+ colored("       To quit the tool."))

    print(colored("  post,", "blue")+ colored("       Post json data to an authorised webapp."))
