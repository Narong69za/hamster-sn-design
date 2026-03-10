"""
=====================================================
PROJECT : SN DESIGN STUDIO
MODULE  : utils/banner.py
VERSION : 1.1
STATUS  : ACTIVE
DESC    : CLI Banner / Identity Header
LAST FIX: Added contact + version sync
=====================================================
"""

def show_banner():

    banner = r"""
\033[95m
 ███████╗███╗   ██╗
 ██╔════╝████╗  ██║
 ███████╗██╔██╗ ██║
 ╚════██║██║╚██╗██║
 ███████║██║ ╚████║
 ╚══════╝╚═╝  ╚═══╝
\033[0m

\033[96mSN DESIGN STUDIO\033[0m
Automation Engine                         Hamster Farming System

Version   : SN-HMSTR 1.1
Developer : SN DESIGN STUDIO
Platform  : Termux / Linux

Mode      : Personal Farming

────────────────────────────────────────────

CONTACT

YouTube   : SN DESIGN STUDIO
Facebook  : ต้องดีแค่ไหน โลกถึงจะจำ

────────────────────────────────────────────
"""
    print(banner)
