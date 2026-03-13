"""
=====================================================
PROJECT : SN DESIGN HAMSTER BOT
MODULE  : core/api_client.py
VERSION : 1.0.0
STATUS  : PRODUCTION
LAST FIX: API client
=====================================================
"""

import requests
from config.settings import API_BASE


def request(endpoint, token):

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    url = API_BASE + endpoint

    r = requests.get(url, headers=headers)

    return r.json()

















































