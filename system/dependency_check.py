"""
=====================================================
PROJECT : SN DESIGN HAMSTER BOT
MODULE  : system/dependency_check.py
VERSION : 1.0.0
STATUS  : PRODUCTION
LAST FIX: Dependency checker
=====================================================
"""

import importlib


def check_dependencies():

    modules = [
        "requests",
        "aiohttp",
        "colorama"
    ]

    for m in modules:

        try:
            importlib.import_module(m)
        except:
            print(f"[ERROR] Missing module: {m}")
            exit()
