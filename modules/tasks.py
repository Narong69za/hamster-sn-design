"""
=====================================================
MODULE  : tasks.py
VERSION : SN-HMSTR 1.1.7
STATUS  : STABLE
DESC    : Task processing module
=====================================================
"""

import time


def run_tasks(account, api):

    tasks = api.tasks()

    if not tasks:
        return

    for task in tasks:

        task_id = task.get("id")

        api.check_task(task_id)

    time.sleep(1)
