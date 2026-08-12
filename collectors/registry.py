import json
from pathlib import Path

from collectors.greenhouse.collector import collect_jobs as collect_greenhouse


BASE_DIR = Path(__file__).resolve().parents[1]
CONFIG_FILE = BASE_DIR / "config" / "sources.json"


def load_sources():
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)["sources"]


def collect_all():
    results = []

    for source in load_sources():
        if not source.get("enabled"):
            continue

        if source["type"] == "greenhouse":
            config_file = BASE_DIR / "config" / "greenhouse.json"

            with open(config_file, "r", encoding="utf-8") as f:
                boards = json.load(f)["boards"]

            for board in boards:
                jobs = collect_greenhouse(board)

                for job in jobs:
                    job["source_board"] = board

                results.extend(jobs)

    return results


if __name__ == "__main__":
    jobs = collect_all()

    print(f"Total jobs collected: {len(jobs)}")

    by_source = {}

    for job in jobs:
        key = f"{job['source']}:{job.get('source_board', 'unknown')}"
        by_source[key] = by_source.get(key, 0) + 1

    for source, count in by_source.items():
        print(f"{source}: {count}")
