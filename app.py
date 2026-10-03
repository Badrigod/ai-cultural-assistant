import streamlit as st
import sys
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).parent
sys.path.append(str(BASE_DIR / "src"))

from cultural_assistant import answer_question

st.set_page_config(
    page_title="AI Cultural Assistant",
    page_icon="🏛️",
    layout="centered"
)

st.title("🏛️ AI Cultural Assistant")

st.write(
    "Welcome! Explore cultural information about artifacts, "
    "dances, regions, and traditions in the collection."
)

st.info(
    "Try questions such as: "
    "'What is Dhiil?', "
    "'Tell me about Dambiil', "
    "'Tell me about Dhaanto', "
    "'Tell me about Afgooye', or "
    "'What is Xeer Ciise?'"
)

question = st.text_input(
    "Ask a cultural question:",
    placeholder="What is Dhiil?"
)

if st.button("Ask Assistant"):
    if question.strip():
        with st.spinner("Searching the cultural collection..."):
            response = answer_question(question)

        st.subheader("Cultural Assistant")
        st.write(response)

        # Display an artifact image when available
        artifacts_file = BASE_DIR / "data" / "artifacts.csv"
        artifacts = pd.read_csv(artifacts_file)

        query = question.lower()

        for _, artifact in artifacts.head(5).iterrows():
            artifact_name = str(artifact["artifact_name"]).lower()

            if artifact_name != "to be determined" and artifact_name in query:
                image_reference = artifact.get("image_reference")

                if pd.notna(image_reference):
                    image_path = BASE_DIR / str(image_reference)

                    if image_path.exists():
                        st.image(
                            str(image_path),
                            caption=str(artifact["artifact_name"]),
                            width=400
                        )
                break
    else:
        st.warning("Please enter a question.")

st.divider()

st.caption(
    "AI Cultural Assistant — Cultural Knowledge Prototype"
)
