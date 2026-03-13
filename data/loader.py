import json


def load_accounts():
    try:
        with open("accounts.json", "r") as f:
            data = json.load(f)

        if isinstance(data, list):
            return data
        else:
            return []

    except Exception as e:
        print(f"ACCOUNT LOAD ERROR: {e}")
        return []
