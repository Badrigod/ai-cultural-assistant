import streamlit as st
from core import (
    ROOT,
    answer,
    draft_example_answer,
    event_counts,
    load_artifact,
    log_event,
    release_ready,
)


st.set_page_config(
    page_title="Khayrhaye Living Heritage | Private Pilot",
    page_icon="🏛️",
    layout="centered",
)

# Artifact identifiers allowed in the private pilot.
ARTIFACT_FILES = {
    "KHH-001": "dhiil.json",
    "KHH-002": "dambiil.json",
    "KHH-003": "kabad.json",
    "KHH-004": "jalxaad.json",
    "KHH-005": "xedho.json",
}

# Navigation to the artifact explorer.
if st.sidebar.button("Museum home / Bogga hore"):
    st.query_params.clear()
    st.query_params["page"] = "home"
    st.rerun()

if st.query_params.get("page") == "home":
    home_language = st.radio(
        "Language / Luqad",
        ["English", "Somali"],
        horizontal=True,
        key="home_language",
    )
    somali = home_language == "Somali"

    st.title("Khayrhaye Living Heritage")
    st.write(
        "Sahami shanta shay ee tijaabada ah."
        if somali
        else "Explore the five pilot artifacts in Somali and English."
    )
    st.info(
        "Tani waa nuqul qabyo ah. Qoraalka dhaqanka iyo oggolaanshaha "
        "sawirrada waxay sugayaan dib-u-eegista madxafka."
        if somali
        else "Private draft preview. Cultural content and image permissions "
        "await museum review."
    )

    st.subheader("Sahaminta agabka" if somali else "Artifact Explorer")
    search = st.text_input(
        "Raadi agabka" if somali else "Search artifacts",
        placeholder=(
            "Magac, aqoonsi, qayb, ama adeegsi"
            if somali
            else "Name, ID, category, or use"
        ),
    )
    matches = 0

    for item_id, filename in ARTIFACT_FILES.items():
        item = load_artifact(ROOT / "data" / filename)
        searchable = " ".join(
            str(item.get(field, ""))
            for field in (
                "name_so",
                "name_en",
                "category",
                "brief_description",
                "traditional_use",
                "cultural_significance",
            )
        )
        searchable = f"{item_id} {searchable}".casefold()

        if search.strip() and search.strip().casefold() not in searchable:
            continue

        matches += 1
        st.write(f"**{item['name_so']}** · {item_id}")
        st.caption(item.get("brief_description", ""))

        button_label = "Fur" if somali else "Open"
        if st.button(
            f"{button_label} {item['name_so']}",
            key=f"open_{item_id}",
        ):
            st.query_params.clear()
            st.query_params["artifact"] = item_id
            st.rerun()

    if matches == 0:
        st.info(
            "Ma jiro shay ku habboon raadintaada."
            if somali
            else "No artifact matches this search."
        )

    st.stop()

requested_id = st.query_params.get("artifact", "KHH-005")

# Reject unknown identifiers instead of accepting file paths from the URL.
if requested_id not in ARTIFACT_FILES:
    st.error("Unknown artifact identifier.")
    st.stop()

artifact_path = ROOT / "data" / ARTIFACT_FILES[requested_id]
record = load_artifact(artifact_path)
artifact_id = record["artifact_id"]

if artifact_id != requested_id:
    st.error("Artifact identifier does not match the requested record.")
    st.stop()

if st.session_state.get("last_visited_artifact") != artifact_id:
    log_event("page_view", artifact_id)
    st.session_state.last_visited_artifact = artifact_id

st.title(record["name_so"])
st.caption("Khayrhaye Living Heritage · Private pilot · " + artifact_id)
st.image(
    str(ROOT / record["image"]["path"]),
    caption=record["image"]["caption"],
    width="stretch",
)

ready = release_ready(record)
if not ready:
    st.warning(
        "Private draft: cultural content awaits museum review. "
        "Do not publish this page or distribute its QR code."
    )

language = st.radio(
    "Language / Luqad",
    ["English", "Somali"],
    index=1 if st.session_state.get("home_language") == "Somali" else 0,
    horizontal=True,
)
lang = "so" if language == "Somali" else "en"

if st.session_state.get("language") != lang:
    log_event("language_selected", artifact_id)
    st.session_state.language = lang

st.subheader("Story" if lang == "en" else "Sheeko")
story = record.get("story_" + lang, "").strip()

st.write(
    story
    if story and (ready or record["status"] == "draft")
    else (
        "Sheekada waxaa sugaya ansixinta matxafka."
        if lang == "so"
        else "The story is awaiting museum approval."
    )
)

if story and not ready:
    st.info(
        "Tusaale laga qoray diiwaanka; lama ansixin."
        if lang == "so"
        else "Sample based on the inventory record; not museum approved."
    )

if artifact_id == "KHH-005" and record.get("cultural_significance"):
    st.subheader("Cultural context / Macnaha dhaqanka")
    st.write(record["cultural_significance"])
    st.caption("Draft English text · UNESCO-02001 · Museum review pending")
    st.markdown(
        "[Read the UNESCO Xeedho entry]"
        "(https://ich.unesco.org/en/USL/xeedho-02001)"
    )

    with st.expander(
        "Explore related traditions / Sahami dhaqamada la xiriira"
    ):
        st.write("Xeedho — a wedding tradition documented in Djibouti.")
        st.caption(
            "Related by name and cultural context. The museum has not "
            "confirmed that artifact KHH-005 was used in this tradition."
        )
        st.markdown(
            "[Source: UNESCO-02001]"
            "(https://ich.unesco.org/en/USL/xeedho-02001)"
        )

with st.expander("Sources and review / Ilaha iyo dib-u-eegista"):
    st.write("Artifact status:", record.get("status", "unknown"))
    approval = record.get("approval", {})
    st.write("Museum reviewer:", approval.get("reviewer") or "Pending")
    st.write("Review date:", approval.get("date") or "Pending")

    for source in record.get("sources", []):
        st.write(
            f"{source.get('id', 'Unknown ID')} — "
            f"{source.get('title', 'Untitled source')}"
        )
        st.caption(
            f"Category: {source.get('source_category', 'Unclassified')} · "
            f"Approved: {'Yes' if source.get('approved') else 'No'}"
        )
        location = source.get("location", "")
        if location.startswith("https://"):
            st.markdown(f"[Open source]({location})")

# Draft demonstration audio for the two narrated artifacts.
artifact_slug = ARTIFACT_FILES[artifact_id].removesuffix(".json")

if artifact_id == "KHH-005" and lang == "so":
    process_audio = ROOT / "assets" / "xedho_process.m4a"
    if process_audio.is_file():
        st.subheader("How Xedho is made — Somali audio")
        st.caption(
            "Somali audio recorded from the UNESCO Xeedho video. "
            "Video credit: © Ministère de la jeunesse et de la culture, "
            "Djibouti, 2022. Transcript and museum review pending."
        )
        st.audio(str(process_audio), format="audio/mp4")

if artifact_id == "KHH-001" and lang == "en":
    dhiil_audio = ROOT / "assets" / "dhiil_ima_en.m4a"
    if dhiil_audio.is_file():
        st.subheader("Dhiil — English audio")
        st.caption(
            "Audio recorded from the Islamic Museum of Australia's "
            "'Object of the Week: Dhiil' video featuring Dr Mahmoud Mohammed. "
            "It describes their Dhiil; the link to artifact KHH-001 awaits "
            "museum review."
        )
        st.audio(str(dhiil_audio), format="audio/mp4")

audio = ROOT / "assets" / f"{artifact_slug}_{lang}.mp3"
if ready and audio.exists():
    if st.button(
        "Play narration" if lang == "en" else "Dhageyso sheekada"
    ):
        log_event("audio_play", artifact_id)
        st.audio(str(audio))

transcript = record.get("transcript_" + lang, "").strip()
if ready and transcript:
    with st.expander("Transcript" if lang == "en" else "Qoraalka codka"):
        st.write(transcript)

st.subheader(
    "Ask about this artifact"
    if lang == "en"
    else "Wax ka weydii shaygan"
)
question = st.chat_input(
    "Your question" if lang == "en" else "Su'aashaada"
)

if question:
    log_event("question_asked", artifact_id)
    response, source = (
        answer(question, record, lang)
        if ready
        else draft_example_answer(question, record, lang)
    )
    st.write(response)
    if source:
        label = (
            "Approved source / Il la ansixiyey: "
            if ready
            else "Draft inventory source / Ilaha diiwaanka hordhaca ah: "
        )
        st.caption(label + source)

if st.sidebar.checkbox("Private team dashboard"):
    st.sidebar.warning(
        "Local development only. Protect this view before any public deployment."
    )
    st.sidebar.write(
        "Event counts (no questions or personal identifiers stored):"
    )
    st.sidebar.dataframe(
        [
            {"artifact": a, "event": e, "count": n}
            for a, e, n in event_counts()
        ],
        hide_index=True,
    )


# WEEK 2 CULTURAL ASSISTANT INTEGRATION
# Research-only search; not part of museum-approved answers.
import sys

integration_dir = str(ROOT.parent)
if integration_dir not in sys.path:
    sys.path.insert(0, integration_dir)

from integration_search import search_culture

st.divider()
st.subheader(
    "Cultural Research Preview"
    if lang == "en"
    else "Hordhaca Cilmi-baarista Dhaqanka"
)

st.warning(
    "Research material only. Results are not museum approved."
    if lang == "en"
    else "Xog cilmi-baaris ah oo keliya. Matxafku weli ma ansixin."
)

cultural_query = st.text_input(
    "Search artifacts, traditions, regions, and dances"
    if lang == "en"
    else "Raadi agab, dhaqan, gobollo iyo ciyaaro",
    key="week2_cultural_search",
)

if cultural_query.strip():
    results = search_culture(cultural_query)

    if results:
        for result in results[:15]:
            st.write(
                f"**{result['name']}** — {result['category']}"
            )
            st.caption(result["review_status"])
    else:
        st.info(
            "No research records found."
            if lang == "en"
            else "Wax xog cilmi-baaris ah lama helin."
        )


# WEEK 2 LINKED CULTURAL ARTIFACT
from integration_mapping import get_linked_artifact

linked_artifact = get_linked_artifact(artifact_id)

if linked_artifact:
    st.divider()
    st.subheader(
        "Linked Cultural Record"
        if lang == "en"
        else "Diiwaanka Dhaqanka ee La Xiriiriyey"
    )

    st.warning(
        "Research preview only. This record has not been museum approved."
        if lang == "en"
        else "Xog cilmi-baaris ah oo keliya. Matxafku ma ansixin."
    )

    st.write("**Artifact:**", linked_artifact.get("artifact_name", ""))
    st.write("**Cultural CSV ID:**", linked_artifact.get("artifact_id", ""))

    for field, label in [
        ("category", "Category"),
        ("description", "Description"),
        ("material", "Material"),
        ("traditional_use", "Traditional use"),
    ]:
        value = linked_artifact.get(field)
        if value is not None and str(value).strip() and str(value) != "nan":
            st.write(f"**{label}:** {value}")
