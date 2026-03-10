"""
=====================================================
MODULE  : reward_checker.py
VERSION : SN-HMSTR 1.1.2
STATUS  : STABLE
DESC    : Reward status checker
=====================================================
"""

from utils.logger import log


def check_rewards(account):
    """
    Check reward status for an account
    """

    try:

        username = account["user"].get("username", "unknown")

        log(f"[{username}] Reward check started")

        # Placeholder reward states
        daily_reward = account.get("daily_reward", "unknown")
        task_reward = account.get("task_reward", "unknown")
        promo_reward = account.get("promo_reward", "unknown")

        log(f"[{username}] Daily reward : {daily_reward}")
        log(f"[{username}] Task reward : {task_reward}")
        log(f"[{username}] Promo reward : {promo_reward}")

        log(f"[{username}] Reward check finished")

    except Exception as e:

        log("Reward check error")
        log(str(e))
