# =====================================================
# PROJECT : SN DESIGN STUDIO
# MODULE  : utils/logger.py
# VERSION : SN-HMSTR 1.1.5
# STATUS  : STABLE
# LAST FIX: Clean logging output
# =====================================================

from colorama import Fore, Style, init

init(autoreset=True)


def log(message):
    print(f"{Fore.GREEN}[SN ENGINE]{Style.RESET_ALL} {message}")
