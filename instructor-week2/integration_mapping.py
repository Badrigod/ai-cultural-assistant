"""Connect museum artifact IDs to cultural research records."""

from pathlib import Path
import pandas as pd

from integration_loader import load_cultural_data

INTEGRATION_DIR = Path(__file__).resolve().parent
MAPPING_FILE = INTEGRATION_DIR / "artifact_mapping.csv"


def get_linked_artifact(museum_id):
    mapping = pd.read_csv(MAPPING_FILE)

    matches = mapping[mapping["museum_id"] == museum_id]

    if len(matches) != 1:
        return None

    cultural_id = matches.iloc[0]["cultural_csv_id"]

    if pd.isna(cultural_id):
        return None

    artifacts = load_cultural_data()["artifacts"]

    linked = artifacts[
        pd.to_numeric(
            artifacts["artifact_id"], errors="coerce"
        ) == int(cultural_id)
    ]

    if len(linked) != 1:
        return None

    return linked.iloc[0].to_dict()


if __name__ == "__main__":
    for museum_id in ["KHH-001", "KHH-002", "KHH-003"]:
        artifact = get_linked_artifact(museum_id)

        if artifact:
            print(
                f"{museum_id} -> "
                f"{artifact['artifact_name']} "
                f"(CSV ID {artifact['artifact_id']})"
            )
        else:
            print(f"{museum_id} -> No verified mapping")
