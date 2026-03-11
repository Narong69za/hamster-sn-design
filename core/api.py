import requests
import time
import random


class HamsterAPI:

    def __init__(self, token, user_agent):
        self.base_url = "https://api.g.hamsterverse.io"
        self.token = token

        self.headers = {
            "Authorization": f"Bearer {token}",
            "User-Agent": user_agent,
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Origin": "https://app-nginx.g.hamsterverse.io",
            "Referer": "https://app-nginx.g.hamsterverse.io/"
        }

    def post(self, endpoint, payload=None):

        url = f"{self.base_url}{endpoint}"

        try:
            r = requests.post(
                url,
                json=payload,
                headers=self.headers,
                timeout=30
            )

            if r.status_code == 200:
                return r.json()

            print("API ERROR:", r.status_code)
            return None

        except Exception as e:
            print("REQUEST ERROR:", e)
            return None

    def sync(self):

        return self.post("/verse/sync")

    def random_sleep(self, a=5, b=15):
        time.sleep(random.randint(a, b))
