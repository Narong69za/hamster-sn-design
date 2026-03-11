"""
=====================================================
MODULE  : tap.py
VERSION : SN-HMSTR 1.1.7
STATUS  : STABLE
DESC    : Tap farming module
=====================================================
"""

import requests
from utils.logger import log

def run_tap(account):

    name = account.get("name")
    token = account.get("token")

    log(f"[{name}] tap module running")
