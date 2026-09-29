import re
from search import search_artifacts


def extract_search_term(question):
    """Extract the likely artifact name from a visitor question."""

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


def answer_question(question):
    search_term = extract_search_term(question)

    results = search_artifacts(search_term)

    if results.empty:
        return (
            f"I could not find information about '{search_term}' "
            "in the cultural artifact collection."
        )

    # Prefer an exact artifact-name match
    exact = results[
        results["artifact_name"]
        .fillna("")
        .str.lower()
        .str.strip()
        == search_term.lower().strip()
    ]

    if not exact.empty:
        artifact = exact.iloc[0]
    else:
        artifact = results.iloc[0]

    name = artifact["artifact_name"]
    category = artifact["category"]
    description = artifact["description"]
    material = artifact["material"]
    traditional_use = artifact["traditional_use"]

    answer = (
        f"{name} is an artifact in the {category} category.\n\n"
        f"Description: {description}\n\n"
        f"Material: {material}\n\n"
        f"Traditional Use: {traditional_use}"
    )

    return answer


if __name__ == "__main__":
    print("AI Cultural Assistant")
    print("---------------------")
    print("Ask me about an artifact in the collection.")
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
