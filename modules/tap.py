from utils.logger import log
from utils.delay import random_delay

def run_tap(account):

    username = account["user"].get("username","unknown")

    log(f"[{username}] Tap farming started")

    random_delay()
