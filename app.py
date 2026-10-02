import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "src"))

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
    "'Tell me about Dhaanto', "
    "'Tell me about Afgooye', or "
    "'What is Xeer Ciise?'"
)

question = st.text_input(
    "Ask a cultural question:",
    placeholder="Tell me about Dhaanto"
)

if st.button("Ask Assistant"):
    if question.strip():
        with st.spinner("Searching the cultural collection..."):
            response = answer_question(question)

        st.subheader("Cultural Assistant")
        st.write(response)
    else:
        st.warning("Please enter a question.")

st.divider()

st.caption(
    "AI Cultural Assistant — Cultural Knowledge Prototype"
)
