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
    "Welcome! Ask questions about cultural artifacts in the collection."
)

st.info(
    "Try questions such as: "
    "'What is Dhiil?', "
    "'Tell me about Dambiil', or "
    "'What is Kebed/Kabad?'"
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
    else:
        st.warning("Please enter a question.")

st.divider()

st.caption(
    "AI Cultural Assistant — Cultural Knowledge Prototype"
)
