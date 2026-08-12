import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
CONFIG_DIR = BASE_DIR / "config"


def load_sources():
    with open(CONFIG_DIR / "sources.json", "r", encoding="utf-8") as f:
        return json.load(f)["sources"]
