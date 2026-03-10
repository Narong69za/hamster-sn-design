"""
=====================================================
PROJECT : SN DESIGN STUDIO
MODULE  : main.py
VERSION : 1.1
STATUS  : ACTIVE
DESC    : Application Entry Point
LAST FIX: Banner + Version update
=====================================================
"""

from utils.banner import show_banner
from core.engine import start_engine


def main():

    show_banner()
    print("\n[SN] Initializing Hamster Bot Engine...\n")
    start_engine()


if __name__ == "__main__":
    main()
