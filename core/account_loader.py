"""
=====================================================
MODULE  : account_loader.py
VERSION : SN-HMSTR 1.1.5
STATUS  : STABLE
DESC    : Load hamster accounts
=====================================================
"""

import urllib.parse
import json


ACCOUNTS_FILE = "data/accounts.txt"


def parse_account(line):

    parsed = urllib.parse.parse_qs(line)

    user = {}

    user_data = parsed.get("user", [None])[0]

    if user_data:
        try:
            user_json = urllib.parse.unquote(user_data)
            user = json.loads(user_json)
        except Exception:
            user = {}

    account = {
        "raw": line,
        "user": user,
        "auth_date": parsed.get("auth_date", [None])[0],
        "hash": parsed.get("hash", [None])[0],
    }

    return account


def load_accounts():

    accounts = []

    try:

        with open(ACCOUNTS_FILE, "r", encoding="utf-8") as f:

            for line in f:

                line = line.strip()

                if not line:
