# =====================================================
# MODULE  : banner.py
# VERSION : 1.1.5
# STATUS  : STABLE
# FIX     : Banner alignment (center terminal)
# =====================================================

import os
import shutil


# ANSI COLOR
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

    lines = [
        f"{RED} ███████╗███╗   ██╗{RESET}",
        f"{RED} ██╔════╝████╗  ██║{RESET}",
        f"{RED} ███████╗██╔██╗ ██║{RESET}",
        f"{RED} ╚════██║██║╚██╗██║{RESET}",
        f"{RED} ███████║██║ ╚████║{RESET}",
        f"{RED} ╚══════╝╚═╝  ╚═══╝{RESET}",
        "",
        f"{CYAN}SN DESIGN STUDIO{RESET}",
        f"{GREEN}Automation Engine{RESET}",
        f"{YELLOW}Hamster Farming System{RESET}",
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
        ""
    ]

    for line in lines:
        print(center(line, width))
