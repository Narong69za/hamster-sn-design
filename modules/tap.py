"""
=====================================================
MODULE  : tap.py
VERSION : SN-HMSTR 1.1.7
STATUS  : STABLE
DESC    : Tap farming module
=====================================================
"""

import time


def run_tap(account, api):

    tap_result = api.tap(10)

    if tap_result:
        print("[TAP] coins:", tap_result.get("coins", 0))

    time.sleep(2)
