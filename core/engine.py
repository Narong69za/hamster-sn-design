import time
from modules.tap import run_tap
from modules.tasks import run_tasks
from modules.promo import run_promo
from utils.logger import log

def start_engine():
    log("Engine started")

    while True:
        log("Running Tap Module")
        run_tap()

        log("Running Task Module")
        run_tasks()

        log("Running Promo Module")
        run_promo()

        log("Sleeping 10 minutes...")
        time.sleep(600)
