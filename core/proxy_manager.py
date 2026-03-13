"""
=====================================================
PROJECT : SN DESIGN HAMSTER BOT
MODULE  : core/proxy_manager.py
VERSION : 1.0.0
STATUS  : PRODUCTION
LAST FIX: Proxy loader
=====================================================
"""

def load_proxies():

    try:

        with open("data/proxies.txt") as f:
            proxies = f.read().splitlines()

        return proxies

    except:
        return []
