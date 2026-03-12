import requests
from utils.logger import log

API_PROFILE = "https://api.hamsterkombatgame.io/auth/profile"

def get_profile(account):

    name = account.get("name")
    token = account.get("token")

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    try:

        r = requests.post(API_PROFILE, headers=headers)
        data = r.json()

        coins = data.get("coins", 0)
        diamonds = data.get("diamonds", 0)
        energy = data.get("energy", 0)
        level = data.get("level", 0)

        log(f"[{name}] PROFILE")
        log(f"[{name}] COINS   : {coins}")
        log(f"[{name}] DIAMOND : {diamonds}")
        log(f"[{name}] ENERGY  : {energy}")
        log(f"[{name}] LEVEL   : {level}")

    except Exception as e:

        log(f"[{name}] PROFILE ERROR : {e}")
