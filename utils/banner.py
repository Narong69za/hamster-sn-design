# =====================================================
# MODULE  : banner.py
# VERSION : 1.1.6
# STATUS  : STABLE
# FIX     : Logo center / Info left / ANSI color fix
# =====================================================

import os
import shutil


RED = "\033[91m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def center(text, width):
    return text.center(width)


def show_banner():

    os.system("clear")

    width = shutil.get_terminal_size((80, 20)).columns

    logo = [
        f"{RED}███████╗███╗   ██╗{RESET}",
        f"{RED}██╔════╝████╗  ██║{RESET}",
        f"{RED}███████╗██╔██╗ ██║{RESET}",
        f"{RED}╚════██║██║╚██╗██║{RESET}",
        f"{RED}███████║██║ ╚████║{RESET}",
        f"{RED}╚══════╝╚═╝  ╚═══╝{RESET}",
    ]

    title = [
        f"{CYAN}SN DESIGN STUDIO{RESET}",
        f"{GREEN}Automation Engine{RESET}",
        f"{YELLOW}Hamster Farming System{RESET}",
    ]

    info = [
        "",
        "Version   : SN-HMSTR 1.1.5",
        "Developer : SN DESIGN STUDIO",
        "Platform  : Termux / Linux",
        "",
        "Mode      : Personal Farming",
        "",
        "────────────────────────────────────────────",
        "",
        "CONTACT",
        "",
        "YouTube   : SN DESIGN STUDIO",
        "Facebook  : ต้องดีแค่ไหน โลกถึงจะจำ",
        "",
        "────────────────────────────────────────────",
    ]

    # LOGO
    for line in logo:
        print(center(line, width))

    print()

    # TITLE
    for line in title:
        print(center(line, width))

    print()

    # INFO
    for line in info:
        print(line)
