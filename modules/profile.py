# =====================================================
# MODULE : modules/profile.py
# FIXED  : API response + JSON parsing
# =====================================================

import requests
from utils.logger import log

API_URL = "https://api.hamsterkombatgame.io/clicker/sync"


def get_profile(account):

    name = account.get("name", "unknown")
    token = account.get("token")

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    try:

        r = requests.post(API_URL, headers=headers, json={}, timeout=15)

        if r.status_code != 200:
            log(f"[{name}] PROFILE HTTP ERROR : {r.status_code}")
            return

        data = r.json()

        user = data.get("clickerUser", {})

        coins = user.get("balanceCoins", 0)
        diamonds = user.get("balanceDiamonds", 0)
        energy = user.get("availableTaps", 0)
        level = user.get("level", 0)

        log(f"[{name}] PROFILE")
        log(f"[{name}] COINS   : {coins}")
        log(f"[{name}] DIAMOND : {diamonds}")
        log(f"[{name}] ENERGY  : {energy}")
        log(f"[{name}] LEVEL   : {level}")

    except Exception as e:

        log(f"[{name}] PROFILE ERROR : {str(e)}")
