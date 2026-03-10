# =====================================================
# PROJECT : SN DESIGN STUDIO
# MODULE  : core/engine.py
# VERSION : SN-HMSTR 1.1.7
# STATUS  : FIXED
# LAST FIX: account argument for modules
# =====================================================

import time

from modules.tap import run_tap
from modules.tasks import run_tasks
from modules.promo import run_promo

from utils.accounts import load_accounts
from utils.logger import log


ENGINE_RUNNING = False


def start_engine():

    global ENGINE_RUNNING

    if ENGINE_RUNNING:
        return

    ENGINE_RUNNING = True

    log("Initializing Hamster Bot Engine...")

    accounts = load_accounts()

    log(f"Loaded {len(accounts)} accounts")

    while True:

        log(f"Starting engine with {len(accounts)} accounts")

        for account in accounts:

            name = account.get("name", "unknown")

            log(f"Running account: {name}")

            try:

                run_tap(account)

                run_tasks(account)

                run_promo(account)

            except Exception as e:

                log(f"[{name}] error: {e}")

        log("Cycle finished - sleep 600s")

        time.sleep(600)
