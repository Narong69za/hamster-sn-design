# =====================================================
# PROJECT : SN DESIGN STUDIO
# MODULE  : core/engine.py
# VERSION : SN-HMSTR 1.2.0
# STATUS  : STABLE
# =====================================================

import time

from modules.tap import run_tap
from modules.tasks import run_tasks
from modules.promo import run_promo
from modules.profile import get_profile

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

        log("====================================")
        log(f"Starting engine with {len(accounts)} accounts")
        log("====================================")

        for account in accounts:

            name = account.get("name", "unknown")

            log("")
            log(f"[ACCOUNT] {name}")
            log("------------------------------------")

            try:

                # PROFILE STATUS
                get_profile(account)

                # MODULES
                run_tap(account)
                run_tasks(account)
                run_promo(account)

            except Exception as e:

                log(f"[{name}] ERROR : {e}")

        log("")
        log("Cycle finished - sleep 600s")
        log("")

        time.sleep(600)
