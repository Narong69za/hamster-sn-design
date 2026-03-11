"""
=====================================================
MODULE  : promo.py
VERSION : SN-HMSTR 1.1.7
STATUS  : STABLE
DESC    : Promo reward module
=====================================================
"""

class PromoModule:

    def __init__(self, api):
        self.api = api

    def run(self):

        print("Checking Promo")

        data = self.api.sync()

        if not data:
            print("promo sync failed")
            return

        print("promo checked")

        self.api.random_sleep()
