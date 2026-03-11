import requests
import json

BASE_URL = "https://api.hamsterkombat.io"


class HamsterAPI:

    def __init__(self, token):

        self.token = token

        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }

    def request(self, method, endpoint, payload=None):

        url = f"{BASE_URL}{endpoint}"

        if method == "GET":
            r = requests.get(url, headers=self.headers)

        else:
            r = requests.post(url, json=payload, headers=self.headers)

        if r.status_code == 200:
            return r.json()

        return None

    def sync(self):
        return self.request("POST", "/player/sync")

    def tap(self, count=10):

        payload = {
            "count": count
        }

        return self.request("POST", "/click", payload)

    def tasks(self):
        return self.request("GET", "/tasks")

    def check_task(self, task_id):

        payload = {
            "task_id": task_id
        }

        return self.request("POST", "/tasks/check", payload)

    def promo(self):
        return self.request("GET", "/promo")
