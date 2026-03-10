"""
=====================================================
MODULE  : player_state.py
VERSION : SN-HMSTR 1.1.5
STATUS  : STABLE
DESC    : Player state module
=====================================================
"""

from utils.logger import log


def show_player_state(account):

    try:

        if not isinstance(account, dict):
            log("state error: invalid account format")
            return

        user = account.get("user", {})
        username = user.get("username", "unknown")

        log(f"[{username}] State check started")

        coins = account.get("coins", 0)
        diamonds = account.get("diamonds", 0)
        energy = account.get("energy", 0)

        log(f"[{username}] Coins : {coins}")
        log(f"[{username}] Diamonds : {diamonds}")
        log(f"[{username}] Energy : {energy}")

        log(f"[{username}] State check finished")

    except Exception as e:

        log(f"[{username}] state error: {str(e)}")
