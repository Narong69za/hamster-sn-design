"""
=====================================================
PROJECT : SN DESIGN HAMSTER BOT
MODULE  : core/account_manager.py
VERSION : 1.0.0
STATUS  : PRODUCTION
LAST FIX: Account loader
=====================================================
"""

import json


def load_accounts():

    with open("data/accounts.json") as f:
        accounts = json.load(f)

    print(f"[INFO] Loaded {len(accounts)} account(s)")

    return accounts
