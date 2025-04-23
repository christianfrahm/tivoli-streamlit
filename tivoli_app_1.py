
import streamlit as st

st.set_page_config(page_title="Tivoli Segmenteringsflow", layout="centered", initial_sidebar_state="collapsed")

artists = ["Hans Philip", "Thomas Helmig", "Tom Jones", "Fraads", "Poul Krebs"]
performances = ["Teater", "Musicals", "Dans og Ballet", "Revy og Comedy"]

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

st.markdown(
    """
    <style>
        .stButton > button {
            width: 100%;
            padding: 0.75em;
            font-size: 1.1em;
            margin-top: 0.5em;
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
    if st.button("Bare én gang"):
        st.session_state.besoeg = "Bare én gang"
        st.session_state.step = 2
    if st.button("To til tre gange"):
        st.session_state.besoeg = "To til tre gange"
        st.session_state.step = 2
    if st.button("Tre eller flere gange"):
        st.session_state.besoeg = "Tre eller flere gange"
        st.session_state.step = 2
    if st.button("Det ved jeg ikke endnu"):
        st.session_state.besoeg = "Det ved jeg ikke endnu"
        st.session_state.step = 2

elif st.session_state.step == 2:
    st.header("Spørgsmål 2")
    if st.button("Ja, helt sikkert"):
        st.session_state.koncert = "Ja, helt sikkert"
        st.session_state.step = 21
    if st.button("Af og til"):
        st.session_state.koncert = "Af og til"
        st.session_state.step = 21
    if st.button("Nej, det er ikke lige mig"):
        st.session_state.koncert = "Nej, det er ikke lige mig"
        st.session_state.step = 3

elif st.session_state.step == 21:
    if st.session_state.artist_index < len(artists):
        artist = artists[st.session_state.artist_index]
        st.subheader(f"🎤 {artist}")
        if st.button("🔥 Hot"):
            st.session_state.artist_hot[artist] = 1
            st.session_state.artist_index += 1
            if st.session_state.artist_index >= len(artists):
                st.session_state.artist_index = 0
                st.session_state.step = 3
        elif st.button("❌ Not"):
            st.session_state.artist_hot[artist] = 0
            st.session_state.artist_index += 1
            if st.session_state.artist_index >= len(artists):
                st.session_state.artist_index = 0
                st.session_state.step = 3
    else:
        st.session_state.artist_index = 0
        st.session_state.step = 3

elif st.session_state.step == 3:
    st.header("Spørgsmål 3")
    if st.button("Casual mad som boder og Food Hall"):
        st.session_state.mad = "Casual mad som boder og Food Hall"
        st.session_state.step = 4
    if st.button("Gourmet og fine dining"):
        st.session_state.mad = "Gourmet og fine dining"
        st.session_state.step = 4
    if st.button("Begge dele"):
        st.session_state.mad = "Begge dele"
        st.session_state.step = 4
    if st.button("Jeg spiser sjældent i Tivoli"):
        st.session_state.mad = "Jeg spiser sjældent i Tivoli"
        st.session_state.step = 4

elif st.session_state.step == 4:
    st.header("Spørgsmål 4")
    if st.button("Jeg elsker dem – det er et must"):
        st.session_state.forlystelser = "Jeg elsker dem – det er et must"
        st.session_state.step = 5
    if st.button("Jeg prøver gerne et par stykker"):
        st.session_state.forlystelser = "Jeg prøver gerne et par stykker"
        st.session_state.step = 5
    if st.button("Jeg bruger dem sjældent eller aldrig"):
        st.session_state.forlystelser = "Jeg bruger dem sjældent eller aldrig"
        st.session_state.step = 5

elif st.session_state.step == 5:
    st.header("Spørgsmål 5")
    if st.button("Ja, det er noget af det bedste"):
        st.session_state.forestillinger = "Ja, det er noget af det bedste"
        st.session_state.step = 51
    if st.button("Nogle gange, hvis det passer ind"):
        st.session_state.forestillinger = "Nogle gange, hvis det passer ind"
        st.session_state.step = 51
    if st.button("Nej, det er ikke lige mig"):
        st.session_state.forestillinger = "Nej, det er ikke lige mig"
        st.session_state.step = 6

elif st.session_state.step == 51:
    if st.session_state.performance_index < len(performances):
        show = performances[st.session_state.performance_index]
        st.subheader(f"🎭 {show}")
        if st.button("👍 Interesseret"):
            st.session_state.performance_hot[show] = 1
            st.session_state.performance_index += 1
        elif st.button("👎 Ikke mig"):
            st.session_state.performance_hot[show] = 0
            st.session_state.performance_index += 1
    else:
        st.session_state.performance_index = 0
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
