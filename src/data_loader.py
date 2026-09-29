import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")

def load_csv(filename):
    path = DATA_DIR / filename

    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")

    return pd.read_csv(path)


def load_all_data():
    data = {
        "artifacts": load_csv("artifacts.csv"),
        "dances": load_csv("dances.csv"),
        "regions": load_csv("regions.csv"),
        "traditions": load_csv("traditions.csv"),
        "sources": load_csv("sources.csv"),
    }

    return data


if __name__ == "__main__":
    data = load_all_data()

    print("AI Cultural Assistant - Data Check")
    print("----------------------------------")

    for name, dataframe in data.items():
        print(f"{name.capitalize()}: {len(dataframe)} records")
