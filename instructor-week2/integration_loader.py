"""Load cultural datasets from the original AI Cultural Assistant."""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CULTURAL_DATA_DIR = Path(__file__).resolve().parent / "cultural_data"


def load_cultural_data():
    filenames = {
        "artifacts": "artifacts.csv",
        "dances": "dances.csv",
        "regions": "regions.csv",
        "traditions": "traditions.csv",
        "sources": "sources.csv",
    }

    return {
        name: pd.read_csv(CULTURAL_DATA_DIR / filename)
        for name, filename in filenames.items()
    }


if __name__ == "__main__":
    data = load_cultural_data()

    for name, records in data.items():
        print(f"{name.capitalize()}: {len(records)} records")
