import json
import requests
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("FOOD_API_KEY")

SERVICE = "COOKRCP01"

URL = (
    "https://openapi.foodsafetykorea.go.kr/api/"
    "{API_KEY}/{SERVICE}/json/{start}/{end}"
)

ROOT = Path(__file__).resolve().parent.parent

SAVE_PATH = Path(ROOT / "data" / "raw" / "recipes.json")


def fetch():
    recipes = []

    start = 1
    batch = 1000

    while True:
        url = URL.format(
            API_KEY=API_KEY,
            SERVICE=SERVICE,
            start=start,
            end=start + batch - 1,
        )

        rows = requests.get(url).json()[SERVICE].get("row", [])

        if len(rows) == 0:
            break

        recipes.extend(rows)
        print(len(recipes))

        start += batch
    print(f"Fetched {len(recipes)} recipes")
    SAVE_PATH.parent.mkdir(exist_ok=True, parents=True)

    with open(SAVE_PATH, "w", encoding="utf-8") as f:
        json.dump(recipes, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    fetch()
