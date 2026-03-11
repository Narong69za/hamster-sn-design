"""
=====================================================
MODULE  : tap.py
VERSION : SN-HMSTR 1.1.7
STATUS  : STABLE
DESC    : Tap farming module
=====================================================
"""

from core.api import HamsterAPI


class TapModule:

    def __init__(self, api: HamsterAPI):
        self.api = api

    def run(self):

        print("Running TAP")

        data = self.api.sync()

        if not data:
            print("sync failed")
            return

        print("tap sync ok")

        self.api.random_sleep()
