import urllib.parse
import json
from utils.logger import log

ACCOUNTS_FILE = "data/accounts.txt"

def parse_account(line):
    parsed = urllib.parse.parse_qs(line)

    user_data = parsed.get("user",[None])[0]

    if user_data:
        user_json = urllib.parse.unquote(user_data)
        user = json.loads(user_json)
    else:
        user = {}

    account = {
        "raw": line,
        "user": user,
        "auth_date": parsed.get("auth_date",[None])[0],
        "hash": parsed.get("hash",[None])[0],
    }

    return account


def load_accounts():
    accounts = []

    try:
        with open(ACCOUNTS_FILE,"r",encoding="utf-8") as f:
            for line in f:
                line=line.strip()

                if not line:
                    continue

                accounts.append(parse_account(line))

        log(f"Loaded {len(accounts)} accounts")

    except FileNotFoundError:
        log("accounts.txt not found")

    return accounts
