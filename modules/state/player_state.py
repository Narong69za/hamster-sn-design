from utils.logger import log

def show_player_state(username):
    log(f"[{username}] State check started")

    # placeholder state
    coins = "unknown"
    diamonds = "unknown"
    energy = "unknown"

    log(f"[{username}] Coins : {coins}")
    log(f"[{username}] Diamonds : {diamonds}")
    log(f"[{username}] Energy : {energy}")

    log(f"[{username}] State check finished")
