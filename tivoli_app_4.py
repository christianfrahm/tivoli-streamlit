
import streamlit as st

st.set_page_config(page_title="Tivoli Segmenteringsflow", layout="centered", initial_sidebar_state="collapsed")

artists = ["Hans Philip", "Thomas Helmig", "Tom Jones", "Fraads", "Poul Krebs"]
performances = ["Teater", "Musicals", "Dans og Ballet", "Revy og Comedy"]

# Initialize session state
for key, default in {
    "step": 1,
    "artist_index": 0,
    "performance_index": 0,
    "artist_hot": {},
    "performance_hot": {},
    "last_button": ""
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

def advance_to(next_step):
    st.session_state.step = next_step

def advance():
    st.session_state.step += 1

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

# Step 1 – Visit Frequency
if st.session_state.step == 1:
    st.header("Spørgsmål 1")
    if st.button("Bare én gang", key="b1"): st.session_state.besoeg = "Bare én gang"; advance()
    if st.button("To til tre gange", key="b2"): st.session_state.besoeg = "To til tre gange"; advance()
    if st.button("Tre eller flere gange", key="b3"): st.session_state.besoeg = "Tre eller flere gange"; advance()
    if st.button("Det ved jeg ikke endnu", key="b4"): st.session_state.besoeg = "Det ved jeg ikke endnu"; advance()

# Step 2 – Music Interest
elif st.session_state.step == 2:
    st.header("Spørgsmål 2")
    if st.button("Ja, helt sikkert", key="b5"): st.session_state.koncert = "Ja, helt sikkert"; advance_to(21)
    if st.button("Af og til", key="b6"): st.session_state.koncert = "Af og til"; advance_to(21)
    if st.button("Nej, det er ikke lige mig", key="b7"): st.session_state.koncert = "Nej, det er ikke lige mig"; advance()

# Step 21 – Artist Preferences
elif st.session_state.step == 21:
    if st.session_state.artist_index < len(artists):
        artist = artists[st.session_state.artist_index]
        st.subheader(f"🎤 {artist}")
        col1, col2 = st.columns(2)
        if col1.button("🔥 Hot", key=f"hot_{artist}"):
            st.session_state.artist_hot[artist] = 1
            st.session_state.artist_index += 1
        if col2.button("❌ Not", key=f"not_{artist}"):
            st.session_state.artist_hot[artist] = 0
            st.session_state.artist_index += 1
        if st.session_state.artist_index >= len(artists):
            st.session_state.artist_index = 0
            advance()
    else:
        st.session_state.artist_index = 0
        advance()

# Step 3 – Food Preferences
elif st.session_state.step == 3:
    st.header("Spørgsmål 3")
    if st.button("Casual mad som boder og Food Hall", key="b8"): st.session_state.mad = "Casual mad som boder og Food Hall"; advance()
    if st.button("Gourmet og fine dining", key="b9"): st.session_state.mad = "Gourmet og fine dining"; advance()
    if st.button("Begge dele", key="b10"): st.session_state.mad = "Begge dele"; advance()
    if st.button("Jeg spiser sjældent i Tivoli", key="b11"): st.session_state.mad = "Jeg spiser sjældent i Tivoli"; advance()

# Step 4 – Rides
elif st.session_state.step == 4:
    st.header("Spørgsmål 4")
    if st.button("Jeg elsker dem – det er et must", key="b12"): st.session_state.forlystelser = "Jeg elsker dem – det er et must"; advance()
    if st.button("Jeg prøver gerne et par stykker", key="b13"): st.session_state.forlystelser = "Jeg prøver gerne et par stykker"; advance()
    if st.button("Jeg bruger dem sjældent eller aldrig", key="b14"): st.session_state.forlystelser = "Jeg bruger dem sjældent eller aldrig"; advance()

# Step 5 – Show Interest
elif st.session_state.step == 5:
    st.header("Spørgsmål 5")
    if st.button("Ja, det er noget af det bedste", key="b15"): st.session_state.forestillinger = "Ja, det er noget af det bedste"; advance_to(51)
    if st.button("Nogle gange, hvis det passer ind", key="b16"): st.session_state.forestillinger = "Nogle gange, hvis det passer ind"; advance_to(51)
    if st.button("Nej, det er ikke lige mig", key="b17"): st.session_state.forestillinger = "Nej, det er ikke lige mig"; advance_to(6)

# Step 51 – Show Preferences
elif st.session_state.step == 51:
    if st.session_state.performance_index < len(performances):
        show = performances[st.session_state.performance_index]
        st.subheader(f"🎭 {show}")
        col1, col2 = st.columns(2)
        if col1.button("👍 Interesseret", key=f"inter_{show}"):
            st.session_state.performance_hot[show] = 1
            st.session_state.performance_index += 1
        if col2.button("👎 Ikke mig", key=f"not_inter_{show}"):
            st.session_state.performance_hot[show] = 0
            st.session_state.performance_index += 1
        if st.session_state.performance_index >= len(performances):
            st.session_state.performance_index = 0
            advance_to(6)
    else:
        st.session_state.performance_index = 0
        advance_to(6)

# Step 6 – Profile Output
elif st.session_state.step == 6:
    st.header("🎯 Din Tivoli-profil")
    tags = []

    # Updated Fredagsrock logic
    if any(st.session_state.artist_hot.get(name) for name in ["Hans Philip", "Thomas Helmig", "Tom Jones"]):
        tags.append("Fredagsrock")
    if st.session_state.artist_hot.get("Fraads"):
        tags.append("Mint")
    if st.session_state.artist_hot.get("Poul Krebs"):
        tags.append("Lørdagshits")

    if st.session_state.mad in ["Casual mad som boder og Food Hall", "Begge dele"]:
        tags.append("Street Food")
    if st.session_state.mad in ["Gourmet og fine dining", "Begge dele"]:
        tags.append("Gourmet")

    for perf, interested in st.session_state.performance_hot.items():
        if interested:
            tags.append(perf)

    st.success("Din Tivoli-profil:")
    st.write(", ".join(tags) if tags else "Ingen relevante segmenter endnu.")
