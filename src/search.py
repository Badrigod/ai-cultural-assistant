import pandas as pd
from data_loader import load_all_data


def search_artifacts(query):
    data = load_all_data()
    artifacts = data["artifacts"]

    query = query.lower().strip()

    searchable_columns = [
        "artifact_name",
        "category",
        "description",
        "material",
        "traditional_use"
    ]

    mask = pd.Series(False, index=artifacts.index)

    for column in searchable_columns:
        mask = mask | artifacts[column].fillna("").astype(str).str.lower().str.contains(
            query, regex=False
        )

    return artifacts[mask]


if __name__ == "__main__":
    query = input("Search for an artifact: ")

    results = search_artifacts(query)

    if results.empty:
        print("\nNo matching artifact found.")
    else:
        print(f"\nFound {len(results)} matching artifact(s):\n")

        for _, artifact in results.iterrows():
            print(f"Name: {artifact['artifact_name']}")
            print(f"Category: {artifact['category']}")
            print(f"Description: {artifact['description']}")
            print(f"Material: {artifact['material']}")
            print(f"Traditional Use: {artifact['traditional_use']}")
            print("-" * 50)
