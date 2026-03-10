# ==========================================
# SN-HMSTR
# utils/accounts.py
# version 1.0
# ==========================================

import json
import os

ACCOUNTS_FILE = "accounts.json"


def load_accounts():
    if not os.path.exists(ACCOUNTS_FILE):
        print("accounts.json not found")
        return []

    with open(ACCOUNTS_FILE, "r") as f:
        data = json.load(f)

    return data
