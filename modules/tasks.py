from utils.logger import log

def run_tasks(account):

    username = account["user"].get("username","unknown")

    log(f"[{username}] Checking tasks")
