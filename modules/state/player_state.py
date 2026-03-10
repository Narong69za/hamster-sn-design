from utils.logger import log


def show_player_state(account):

    username = account["user"].get("username", "unknown")

    log(f"[{username}] State check started")

    coins = account.get("coins", 0)
    diamonds = account.get("diamonds", 0)
    energy = account.get("energy", 0)

    log(f"[{username}] Coins : {coins}")
    log(f"[{username}] Diamonds : {diamonds}")
    log(f"[{username}] Energy : {energy}")

    log(f"[{username}] State check finished")
