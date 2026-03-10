from utils.logger import log

def run_promo(account):

    username = account["user"].get("username","unknown")

    log(f"[{username}] Checking promo")
