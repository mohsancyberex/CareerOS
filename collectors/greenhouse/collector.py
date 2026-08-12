import requests


def collect_jobs(board_token: str):
    url = f"https://boards-api.greenhouse.io/v1/boards/{board_token}/jobs"
    response = requests.get(url, timeout=20)
    response.raise_for_status()

    jobs = response.json().get("jobs", [])

    return [
        {
            "source": "greenhouse",
            "source_id": str(job["id"]),
            "title": job.get("title", ""),
            "company": board_token,
            "location": job.get("location", {}).get("name"),
            "url": job.get("absolute_url", ""),
        }
        for job in jobs
    ]


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python3 collectors/greenhouse/collector.py <board_token>")
        raise SystemExit(1)

    jobs = collect_jobs(sys.argv[1])

    print(f"Collected {len(jobs)} jobs")

    for job in jobs[:10]:
        print(
            f"{job['title']} | "
            f"{job['location']} | "
            f"{job['url']}"
        )
