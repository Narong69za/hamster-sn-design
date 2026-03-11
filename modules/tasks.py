"""
=====================================================
MODULE  : tasks.py
VERSION : SN-HMSTR 1.1.7
STATUS  : STABLE
DESC    : Task processing module
=====================================================
"""

from utils.logger import log

def run_tasks(account):

    name = account.get("name")

    log(f"[{name}] tasks module running")
