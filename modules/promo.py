"""
=====================================================
MODULE  : promo.py
VERSION : SN-HMSTR 1.1.7
STATUS  : STABLE
DESC    : Promo reward module
=====================================================
"""

from utils.logger import log

def run_promo(account):

    name = account.get("name")

    log(f"[{name}] promo module running")
