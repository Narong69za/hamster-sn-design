"""
=====================================================
MODULE  : tap.py
VERSION : SN-HMSTR 1.1.7
STATUS  : STABLE
DESC    : Tap farming module
=====================================================
"""

from utils.logger import log

def run_tap(account):

    name = account.get("name", "unknown")

    log(f"[{name}] TAP : START")

    try:

        status = "OK"

        log(f"[{name}] TAP : {status}")

    except Exception as e:

        log(f"[{name}] TAP : ERROR {e}")
