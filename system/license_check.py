"""
=====================================================
PROJECT : SN DESIGN HAMSTER BOT
MODULE  : system/license_check.py
VERSION : 1.0.0
STATUS  : PRODUCTION
LAST FIX: License verification
=====================================================
"""

import requests
from config.settings import LICENSE_SERVER


def verify_license():

    license_key = input("Enter license key: ")

    payload = {"license_key": license_key}

    r = requests.post(LICENSE_SERVER, json=payload)

    if r.status_code != 200:

        print("License invalid")
        exit()

    print("License verified")
