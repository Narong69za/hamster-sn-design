import time
import requests
import urllib3

urllib3.disable_warnings()

CYCLE_DELAY = 60
TAP_COUNT = 50


def log(msg):
    print(msg, flush=True)


def request_api(url, headers, payload=None):

    try:

        r = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=15,
            verify=False
        )

        return r

    except Exception as e:

        log(f"NETWORK ERROR : {e}")
        return None


def sync_account(headers):

    url = "https://api.hamsterkombat.io/clicker/sync"

    r = request_api(url, headers)

    if not r:
        return None

    if r.status_code == 200:

        return r.json()

    log(f"SYNC FAIL : {r.status_code}")

    return None


def tap(headers, taps):

    url = "https://api.hamsterkombat.io/clicker/tap"

    payload = {
        "count": taps
    }

    r = request_api(url, headers, payload)

    if not r:
        return

    if r.status_code == 200:

        log("TAP SUCCESS")

    else:

        log(f"TAP FAIL : {r.status_code}")


def complete_tasks(headers):

    url = "https://api.hamsterkombat.io/clicker/task"

    r = request_api(url, headers)

    if not r:
        return

    if r.status_code == 200:

        log("TASK CHECKED")

    else:

        log(f"TASK ERROR : {r.status_code}")


def run_account(account):

    name = account.get("name", "account")
    user_id = account.get("user_id", "unknown")
    token = account.get("token")

    log("=" * 40)
    log(f"USER ID : {user_id}")
    log(f"ACCOUNT : {name}")
    log("-" * 20)

    if not token:

        log("TOKEN NOT FOUND")
        return

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10)",
        "Accept": "application/json",
        "Origin": "https://hamsterkombat.io",
        "Referer": "https://hamsterkombat.io/"
    }

    data = sync_account(headers)

    if not data:

        return

    try:

        user = data["clickerUser"]

        coins = user["balanceCoins"]
        energy = user["availableTaps"]

        log(f"COINS : {coins}")
        log(f"ENERGY : {energy}")

        taps = min(energy, TAP_COUNT)

        if taps > 0:

            tap(headers, taps)

        complete_tasks(headers)

    except Exception as e:

        log(f"PARSE ERROR : {e}")


def start_engine(accounts):

    log("=" * 40)
    log(f"ENGINE STARTED ({len(accounts)} accounts)")
    log("=" * 40)

    while True:

        for account in accounts:

            try:

                run_account(account)

            except Exception as e:

                log(f"ACCOUNT ERROR : {e}")

        log("-" * 40)
        log("Cycle finished - sleep 60s")
        log("-" * 40)

        time.sleep(CYCLE_DELAY)
