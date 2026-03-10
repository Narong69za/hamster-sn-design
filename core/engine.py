import time

from core.account_loader import load_accounts
from modules.tap import run_tap
from modules.tasks import run_tasks
from modules.promo import run_promo

from utils.logger import log


def start_engine():

    accounts = load_accounts()

    if not accounts:
        log("No accounts loaded")
        return

    log(f"Starting engine with {len(accounts)} accounts")

    while True:

        for account in accounts:

            username = account["user"].get("username","unknown")

            log(f"Running account: {username}")

            run_tap(account)
            run_tasks(account)
            run_promo(account)

        log("Cycle finished - sleep 600s")
        time.sleep(600)
