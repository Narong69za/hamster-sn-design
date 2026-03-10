# =====================================================
# PROJECT : SN DESIGN STUDIO
# MODULE  : utils/banner.py
# VERSION : SN-HMSTR 1.1.5
# STATUS  : FIXED
# =====================================================

import os


# ANSI COLOR
RED = "\033[91m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def show_banner():

    os.system("clear")

    print(f"""{RED}
 ███████╗███╗   ██╗
 ██╔════╝████╗  ██║
 ███████╗██╔██╗ ██║
 ╚════██║██║╚██╗██║
 ███████║██║ ╚████║
 ╚══════╝╚═╝  ╚═══╝
{RESET}
{CYAN}SN DESIGN STUDIO{RESET}
{GREEN}Automation Engine{RESET}        {YELLOW}Hamster Farming System{RESET}

Version   : SN-HMSTR 1.1.5
Developer : SN DESIGN STUDIO
Platform  : Termux / Linux

Mode      : Personal Farming

────────────────────────────────────────────

CONTACT

YouTube   : SN DESIGN STUDIO
Facebook  : ต้องดีแค่ไหน โลกถึงจะจำ

────────────────────────────────────────────
""")
