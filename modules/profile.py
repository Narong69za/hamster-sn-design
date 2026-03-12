# =====================================================
# MODULE : modules/profile.py
# FIXED  : API response + JSON parsing
# =====================================================

import requests
from utils.logger import log

API_URL = "https://api.hamsterkombatgame.io/season2/sync"

def get_profile(account):

    name = account["name"]
    token = account["token"]

    headers = {
        "Authorization": f"tma {token}",
        "Content-Type": "application/json",
        "Origin": "https://season2.hamsterkombatgame.io",
        "Referer": "https://season2.hamsterkombatgame.io/",
        "User-Agent": "Mozilla/5.0"
    }

    try:

        r = requests.post(API_URL, headers=headers, json={})

        if r.status_code != 200:
            log(f"[{name}] PROFILE HTTP ERROR : {r.status_code}")
            return

        data = r.json()

        user = data.get("clickerUser", {})

        coins = user.get("balanceCoins", 0)
        diamonds = user.get("balanceDiamonds", 0)
        energy = user.get("availableTaps", 0)

        log(f"[{name}] COINS   : {coins}")
        log(f"[{name}] DIAMOND : {diamonds}")
        log(f"[{name}] ENERGY  : {energy}")

    except Exception as e:

        log(f"[{name}] PROFILE ERROR : {e}")
