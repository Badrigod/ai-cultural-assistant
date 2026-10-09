import pandas as pd
from data_loader import load_all_data


def search_dataframe(dataframe, query, columns):
    """Search selected columns of a dataframe."""
    query = query.lower().strip()

    mask = pd.Series(False, index=dataframe.index)

    for column in columns:
        if column in dataframe.columns:
            mask = mask | (
                dataframe[column]
                .fillna("")
                .astype(str)
                .str.lower()
                .str.contains(query, regex=False)
            )

    return dataframe[mask]


def search_artifacts(query):
    data = load_all_data()

    return search_dataframe(
        data["artifacts"],
        query,
        [
            "artifact_name",
            "category",
            "description",
            "material",
            "traditional_use"
        ]
    )


def search_regions(query):
    data = load_all_data()

    return search_dataframe(
        data["regions"],
        query,
        [
            "region_name",
            "country_location",
            "description",
            "communities",
            "languages"
        ]
    )


def search_traditions(query):
    data = load_all_data()
    traditions = data["traditions"].copy()

    # Exclude records without verified supporting sources
    if "validation_status" in traditions.columns:
        traditions = traditions[
            traditions["validation_status"]
            .fillna("")
            .str.lower()
            .ne("pending source verification")
        ]

    # Keep newly researched hospitality content out of
    # public answers until cultural review is complete.
    traditions = traditions[
        traditions["tradition_id"] != "T003"
    ]

    return search_dataframe(
        traditions,
        query,
        [
            "tradition_name",
            "tradition_category",
            "description",
            "community",
            "cultural_significance",
            "occasion"
        ]
    )


def search_dances(query):
    data = load_all_data()

    return search_dataframe(
        data["dances"],
        query,
        [
            "dance_name",
            "description",
            "community",
            "occasion_purpose",
            "music_instruments",
            "clothing"
        ]
    )


if __name__ == "__main__":
    print("Cultural Information Search")
    print("---------------------------")

    query = input("Search: ")

    print("\nARTIFACTS")
    print(search_artifacts(query).to_string(index=False))

    print("\nREGIONS")
    print(search_regions(query).to_string(index=False))

    print("\nTRADITIONS")
    print(search_traditions(query).to_string(index=False))

    print("\nDANCES")
    print(search_dances(query).to_string(index=False))
