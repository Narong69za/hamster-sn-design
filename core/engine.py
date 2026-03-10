# =====================================================
# PROJECT : SN DESIGN STUDIO
# MODULE  : core/engine.py
# VERSION : SN-HMSTR 1.1.5
# STATUS  : FIXED
# LAST FIX: Prevent double engine start
# =====================================================

import time
from modules.tap import run_tap
from modules.tasks import run_tasks
from modules.promo import run_promo
from utils.logger import log

ENGINE_RUNNING = False


def start_engine():

    global ENGINE_RUNNING

    if ENGINE_RUNNING:
        return

    ENGINE_RUNNING = True

    log("Initializing Hamster Bot Engine...")

    while True:

        log("Running Tap Module")
        run_tap()

        log("Running Task Module")
        run_tasks()

        log("Running Promo Module")
        run_promo()

        log("Cycle finished - sleep 600s")

        time.sleep(600)
