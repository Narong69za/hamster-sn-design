"""
=====================================================
MODULE  : tasks.py
VERSION : SN-HMSTR 1.1.7
STATUS  : STABLE
DESC    : Task processing module
=====================================================
"""

class TaskModule:

    def __init__(self, api):
        self.api = api

    def run(self):

        print("Running Tasks")

        data = self.api.sync()

        if not data:
            print("task sync failed")
            return

        print("tasks checked")

        self.api.random_sleep()
