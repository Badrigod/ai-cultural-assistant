import streamlit as st

st.set_page_config(
    page_title="Khayrhaye Living Heritage",
    page_icon="🏛️",
    layout="wide"
)

st.title("🏛️ Khayrhaye Living Heritage")
st.subheader("AI Cultural Assistant + Digital Artifact Pilot")

st.info(
    "Instructor demonstration using fictional sample data. "
    "Original museum records and media are not published."
)

st.markdown("### Project Overview")
st.write(
    "This practicum project integrates a cultural research "
    "assistant with a digital museum artifact experience."
)

artifacts = {
    "DEMO-001": "Sample Woven Container",
    "DEMO-002": "Sample Decorative Basket",
    "DEMO-003": "Sample Textile",
    "DEMO-004": "Sample Cultural Ornament",
    "DEMO-005": "Sample Heritage Object",
}

st.markdown("### Explore Sample Artifacts")

selected = st.selectbox(
    "Choose an artifact",
    list(artifacts.keys()),
    format_func=lambda x: artifacts[x]
)

st.write("**Artifact ID:**", selected)
st.write("**Artifact name:**", artifacts[selected])
st.write("**Status:** Fictional demonstration record")

st.markdown("### Cultural Research Search")

query = st.text_input("Search sample artifacts")

if query:
    results = [
        (key, name)
        for key, name in artifacts.items()
        if query.casefold() in name.casefold()
    ]

    if results:
        for key, name in results:
            st.write(f"{key} — {name}")
    else:
        st.warning("No matching sample artifacts found.")

st.divider()
st.caption(
    "Khayrhaye Living Heritage | Week 2 Practicum "
    "| Public-safe instructor demonstration"
)
