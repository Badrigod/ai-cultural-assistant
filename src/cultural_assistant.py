import re
from search import (
    search_artifacts,
    search_regions,
    search_traditions,
    search_dances
)


def extract_search_term(question):
    question = question.strip()

    patterns = [
        r"what is (.+?)[?]?$",
        r"what is a (.+?)[?]?$",
        r"tell me about (.+?)[?]?$",
        r"describe (.+?)[?]?$",
        r"what do you know about (.+?)[?]?$",
    ]

    for pattern in patterns:
        match = re.search(pattern, question, re.IGNORECASE)
        if match:
            return match.group(1).strip()

    return question.rstrip("?").strip()


def safe_value(value):
    if value is None:
        return "Not specified"

    value = str(value)

    if value.lower() == "nan":
        return "Not specified"

    return value


def answer_question(question):
    search_term = extract_search_term(question)

    # Search artifacts
    results = search_artifacts(search_term)

    if not results.empty:
        artifact = results.iloc[0]

        return (
            f"Artifact: {safe_value(artifact['artifact_name'])}\n\n"
            f"Category: {safe_value(artifact['category'])}\n\n"
            f"Description: {safe_value(artifact['description'])}\n\n"
            f"Material: {safe_value(artifact['material'])}\n\n"
            f"Traditional Use: {safe_value(artifact['traditional_use'])}"
        )

    # Search regions
    results = search_regions(search_term)

    if not results.empty:
        region = results.iloc[0]

        return (
            f"Region: {safe_value(region['region_name'])}\n\n"
            f"Location: {safe_value(region['country_location'])}\n\n"
            f"Description: {safe_value(region['description'])}\n\n"
            f"Communities: {safe_value(region['communities'])}\n\n"
            f"Related Traditions: {safe_value(region['related_traditions'])}"
        )

    # Search traditions
    results = search_traditions(search_term)

    if not results.empty:
        tradition = results.iloc[0]

        return (
            f"Tradition: {safe_value(tradition['tradition_name'])}\n\n"
            f"Description: {safe_value(tradition['description'])}\n\n"
            f"Community: {safe_value(tradition['community'])}\n\n"
            f"Cultural Significance: "
            f"{safe_value(tradition['cultural_significance'])}\n\n"
            f"Occasion: {safe_value(tradition['occasion'])}"
        )

    # Search dances
    results = search_dances(search_term)
    # Search dances
    results = search_dances(search_term)

    if not results.empty:
        dance = results.iloc[0]

        return (
            f"Dance / Performance: {safe_value(dance['dance_name'])}\n\n"
            f"Description: {safe_value(dance['description'])}\n\n"
            f"Region: {safe_value(dance['region'])}\n\n"
            f"Community: {safe_value(dance['community'])}\n\n"
            f"Clothing: {safe_value(dance['clothing'])}\n\n"
            f"Music / Instruments: "
            f"{safe_value(dance['music_instruments'])}\n\n"
            f"Movements: {safe_value(dance['movements'])}\n\n"
            f"Occasion / Purpose: "
            f"{safe_value(dance['occasion_purpose'])}\n\n"
            f"Historical Significance: "
            f"{safe_value(dance['historical_significance'])}\n\n"
            f"Video / Image Reference: "
            f"{safe_value(dance['video_image_reference'])}\n\n"
            f"Validation Status: "
            f"{safe_value(dance['validation_status'])}"
        )
    return (
        f"I could not find information about '{search_term}' "
        "in the cultural collection."
    )


if __name__ == "__main__":
    print("AI Cultural Assistant")
    print("---------------------")
    print(
        "Ask me about artifacts, dances, regions, "
        "or traditions."
    )
    print("Type 'exit' to stop.\n")

    while True:
        question = input("Visitor: ")

        if question.lower().strip() in ["exit", "quit"]:
            print("Cultural Assistant: Goodbye!")
            break

        response = answer_question(question)

        print("\nCultural Assistant:")
        print(response)
        print()
