"""
=====================================================
PROJECT : SN DESIGN STUDIO
MODULE  : core/engine.py
VERSION : 1.1
STATUS  : ACTIVE
DESC    : Hamster Farming Automation Engine
LAST FIX: Integrated reward + player state
=====================================================
"""

import time

from core.account_loader import load_accounts

from modules.tap import run_tap
from modules.tasks import run_tasks
from modules.promo import run_promo

# NEW MODULES
from modules.rewards.reward_checker import check_rewards
from modules.state.player_state import show_player_state

from utils.logger import log


def start_engine():

    log("Initializing Hamster Bot Engine...")

    accounts = load_accounts()
    log(f"Loaded {len(accounts)} accounts")

    if not accounts:
        log("No accounts loaded")
        return

    log(f"Loaded {len(accounts)} accounts")
    log(f"Starting engine with {len(accounts)} accounts")

    while True:

        for account in accounts:

            username = account["user"].get("username", "unknown")

            log(f"Running account: {username}")

            # TAP FARM
            log(f"[{username}] Tap farming started")
            run_tap(account)

            # TASKS
            log(f"[{username}] Checking tasks")
            run_tasks(account)

            # PROMO
            log(f"[{username}] Checking promo")
            run_promo(account)

            # REWARDS
            log(f"[{username}] Checking rewards")
            try:
                check_rewards(account)
            except Exception as e:
                log(f"[{username}] reward error: {e}")

            # PLAYER STATE
            log(f"[{username}] Updating player state")
            try:
                show_player_state(username)
            except Exception as e:
                log(f"[{username}] state error: {e}")

        log("Cycle finished - sleep 600s")
        time.sleep(600)
