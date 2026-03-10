from colorama import Fore, Style
import os

def show_banner():
    os.system("clear")
    print(Fore.RED + r"""
 ███████╗███╗   ██╗
 ██╔════╝████╗  ██║
 ███████╗██╔██╗ ██║
 ╚════██║██║╚██╗██║
 ███████║██║ ╚████║
 ╚══════╝╚═╝  ╚═══╝
""")
    print(Fore.WHITE + "SN DESIGN STUDIO")
    print(Fore.WHITE + "Automation Engine")
    print(Fore.WHITE + "Hamster Farming System")
    print(Fore.WHITE + "Version : SN-HMSTR 1.0\n")
    print(Fore.YELLOW + "Developer : SN DESIGN STUDIO")
    print(Fore.YELLOW + "Platform  : Termux / Linux")
    print(Fore.YELLOW + "Mode      : Personal Farming\n")
    print(Style.RESET_ALL)
