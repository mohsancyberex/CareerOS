import requests


def collect_jobs(board_token: str):
    url = f"https://boards-api.greenhouse.io/v1/boards/{board_token}/jobs"
    response = requests.get(url, timeout=20)
    response.raise_for_status()
    return response.json().get("jobs", [])


if __name__ == "__main__":
    print("Greenhouse collector: OK")
