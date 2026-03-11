"""
=====================================================
MODULE  : promo.py
VERSION : SN-HMSTR 1.1.7
STATUS  : STABLE
DESC    : Promo reward module
=====================================================
"""

import time


def run_promo(account, api):

    promos = api.promo()

    if promos:
        print("[PROMO] rewards found")

    time.sleep(1)
