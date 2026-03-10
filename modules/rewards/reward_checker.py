from utils.logger import log


def check_rewards(username):
    log(f"[{username}] Reward check started")

    # placeholder reward status
    daily_reward = "unknown"
    task_reward = "unknown"
    promo_reward = "unknown"

    log(f"[{username}] Daily reward : {daily_reward}")
    log(f"[{username}] Task reward : {task_reward}")
    log(f"[{username}] Promo reward : {promo_reward}")

    log(f"[{username}] Reward check finished")
