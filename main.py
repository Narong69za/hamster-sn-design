"""
=====================================================
PROJECT : SN DESIGN HAMSTER BOT
MODULE  : main.py
VERSION : 1.0.0
STATUS  : PRODUCTION
LAST FIX: Initial production commit
=====================================================
"""

from system.banner import show_banner
from system.license_check import verify_license
from system.dependency_check import check_dependencies
from core.account_manager import load_accounts
from core.engine import start_engine


def main():

    show_banner()

    check_dependencies()

    verify_license()

    accounts = load_accounts()

    start_engine(accounts)


if __name__ == "__main__":
    main()
