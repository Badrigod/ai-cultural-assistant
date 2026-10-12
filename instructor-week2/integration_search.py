"""Cultural research preview for the integrated museum pilot."""

from integration_loader import load_cultural_data


def search_culture(query):
    query = query.strip().casefold()

    if not query:
        return []

    data = load_cultural_data()
    results = []

    for category in ("artifacts", "dances", "regions", "traditions"):
        df = data[category]

        # Do not expose records awaiting source verification
        # or the hospitality record awaiting cultural review.
        if category == "traditions":
            if "validation_status" in df.columns:
                df = df[
                    df["validation_status"].fillna("")
                    .astype(str).str.casefold()
                    .ne("pending source verification")
                ]
            if "tradition_id" in df.columns:
                df = df[df["tradition_id"] != "T003"]

        for _, row in df.iterrows():
            values = row.fillna("").astype(str)
            if any(query in value.casefold() for value in values):
                name_field = {
                    "artifacts": "artifact_name",
                    "dances": "dance_name",
                    "regions": "region_name",
                    "traditions": "tradition_name",
                }[category]

                results.append({
                    "category": category,
                    "name": str(row.get(name_field, "")),
                    "review_status": "Research preview - not museum approved",
                })

    return results


if __name__ == "__main__":
    for result in search_culture("Dhiil"):
        print(result)
