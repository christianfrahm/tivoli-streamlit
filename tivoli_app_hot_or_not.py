
import streamlit as st

st.set_page_config(page_title="Tivoli Segmenteringsflow", layout="centered", initial_sidebar_state="collapsed")

# Define the artists and performance categories
artists = ["Hans Philip", "Thomas Helmig", "Tom Jones", "Fraads", "Poul Krebs"]
performances = ["Teater", "Musicals", "Dans og Ballet", "Revy og Comedy"]

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 1
if "artist_index" not in st.session_state:
    st.session_state.artist_index = 0
if "performance_index" not in st.session_state:
    st.session_state.performance_index = 0
if "artist_hot" not in st.session_state:
    st.session_state.artist_hot = {}
if "performance_hot" not in st.session_state:
    st.session_state.performance_hot = {}
if "kunstner_section" not in st.session_state:
    st.session_state.kunstner_section = False
if "scene_section" not in st.session_state:
    st.session_state.scene_section = False
if "koncert" not in st.session_state:
    st.session_state.koncert = ""
if "forestillinger" not in st.session_state:
    st.session_state.forestillinger = ""

st.markdown(
    """
    <style>
        .stButton > button {
            width: 45%;
            padding: 0.75em;
            font-size: 1.1em;
            margin: 0.5em;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎡 Din Tivoli-profil")

if st.session_state.step == 1:
    st.header("Spørgsmål 1")
    besoeg = st.radio("Hvor mange gange tror du, du kommer til at besøge Tivoli i år?", [
        "Bare én gang", "To til tre gange", "Tre eller flere gange", "Det ved jeg ikke endnu"
    ])
    if besoeg:
        st.session_state.besoeg = besoeg
        st.session_state.step = 2

elif st.session_state.step == 2:
    st.header("Spørgsmål 2")
    koncert = st.radio("Er du typen, der nyder en god koncert i Tivoli?", [
        "Ja, helt sikkert", "Af og til", "Nej, det er ikke lige mig"
    ])
    if koncert:
        st.session_state.koncert = koncert
        st.session_state.kunstner_section = koncert in ["Ja, helt sikkert", "Af og til"]
        st.session_state.step = 21 if st.session_state.kunstner_section else 3

elif st.session_state.step == 21:
    if st.session_state.artist_index < len(artists):
        artist = artists[st.session_state.artist_index]
        st.subheader(f"🎤 {artist}")
        col1, col2 = st.columns(2)
        if col1.button("🔥 Hot"):
            st.session_state.artist_hot[artist] = 1
            st.session_state.artist_index += 1
        if col2.button("❌ Not"):
            st.session_state.artist_hot[artist] = 0
            st.session_state.artist_index += 1
    else:
        st.session_state.step = 3

elif st.session_state.step == 3:
    st.header("Spørgsmål 3")
    mad = st.radio("Hvilken type madoplevelser er du mest interesseret i i Tivoli?", [
        "Casual mad som boder og Food Hall", "Gourmet og fine dining", "Begge dele", "Jeg spiser sjældent i Tivoli"
    ])
    if mad:
        st.session_state.mad = mad
        st.session_state.step = 4

elif st.session_state.step == 4:
    st.header("Spørgsmål 4")
    forlystelser = st.radio("Hvor meget betyder forlystelser for dit besøg i Tivoli?", [
        "Jeg elsker dem – det er et must", "Jeg prøver gerne et par stykker", "Jeg bruger dem sjældent eller aldrig"
    ])
    if forlystelser:
        st.session_state.forlystelser = forlystelser
        st.session_state.step = 5

elif st.session_state.step == 5:
    st.header("Spørgsmål 5")
    forestillinger = st.radio("Er du interesseret i forestillinger som teater, dans eller musicals i haven?", [
        "Ja, det er noget af det bedste", "Nogle gange, hvis det passer ind", "Nej, det er ikke lige mig"
    ])
    if forestillinger:
        st.session_state.forestillinger = forestillinger
        st.session_state.scene_section = forestillinger != "Nej, det er ikke lige mig"
        st.session_state.step = 51 if st.session_state.scene_section else 6

elif st.session_state.step == 51:
    if st.session_state.performance_index < len(performances):
        show = performances[st.session_state.performance_index]
        st.subheader(f"🎭 {show}")
        col1, col2 = st.columns(2)
        if col1.button("👍 Interesseret"):
            st.session_state.performance_hot[show] = 1
            st.session_state.performance_index += 1
        if col2.button("👎 Ikke mig"):
            st.session_state.performance_hot[show] = 0
            st.session_state.performance_index += 1
    else:
        st.session_state.step = 6

elif st.session_state.step == 6:
    st.header("🎯 Din Tivoli-profil")
    tags = []

    if st.session_state.artist_hot.get("Hans Philip") or st.session_state.artist_hot.get("Thomas Helmig"):
        tags.append("Fredagsrock")
    if st.session_state.artist_hot.get("Fraads"):
        tags.append("Mint")
    if st.session_state.artist_hot.get("Poul Krebs"):
        tags.append("Lørdagshits")

    if st.session_state.mad == "Casual mad som boder og Food Hall" or st.session_state.mad == "Begge dele":
        tags.append("Street Food")
    if st.session_state.mad == "Gourmet og fine dining" or st.session_state.mad == "Begge dele":
        tags.append("Gourmet")

    for perf, interested in st.session_state.performance_hot.items():
        if interested:
            tags.append(perf)

    st.success("Din Tivoli-profil:")
    st.write(", ".join(tags) if tags else "Ingen relevante segmenter endnu.")
