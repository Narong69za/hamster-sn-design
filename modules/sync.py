import requests
from utils.logger import log

API = "https://api.hamsterkombatgame.io/season2/sync"


def run_sync(account):

    name = account["name"]
    token = account["token"]

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Origin": "https://season2.hamsterkombatgame.io",
        "Referer": "https://season2.hamsterkombatgame.io/"
    }

    r = requests.post(API, headers=headers, json={})

    log(f"[{name}] sync {r.status_code}")
