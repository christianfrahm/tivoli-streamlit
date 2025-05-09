import streamlit as st
import os
from PIL import Image

# Page config
st.set_page_config(page_title="Tivoli Segmenteringsflow", layout="centered", initial_sidebar_state="collapsed")
st.markdown("""
    <style>
    .stApp {
        background-image: url("background.png");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
""", unsafe_allow_html=True)

# Image config
IMG_WIDTH = 400
LOGO_WIDTH = 200

def show_image(path, logo=False):
    if os.path.exists(path):
        img = Image.open(path)
        width = LOGO_WIDTH if logo else IMG_WIDTH
        height = int((width / img.width) * img.height)
        col = st.columns([1, 3, 1])[1]
        with col:
            st.image(img.resize((width, height)), use_container_width=False)

def centered_button(label, key=None):
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        return st.button(label, key=key, use_container_width=True)

# Data
artists = [
    {"name": "Hans Philip", "img": "hans_philip.png"},
    {"name": "Thomas Helmig", "img": "thomas_helmig.png"},
    {"name": "Tom Jones", "img": "tom_jones.png"},
    {"name": "Fraads", "img": "fraads.png"},
    {"name": "Poul Krebs", "img": "poul_krebs.png"},
]
performances = [
    {"name": "Teater", "img": "teater.png"},
    {"name": "Musicals", "img": "musical.png"},
    {"name": "Dans og Ballet", "img": "ballet.png"},
    {"name": "Revy og Comedy", "img": "revy.png"},
]

# Session state defaults
for key, default in {
    "step": 0,
    "artist_index": 0,
    "performance_index": 0,
    "artist_hot": {},
    "performance_hot": {},
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

def next_step(): st.session_state.step += 1
def go_to(step): st.session_state.step = step

# Logo + Title
show_image("tivoli_logo2.png", logo=True)
st.title("🌩️ Din Tivoli-profil")

# Step 0 – Forside
if st.session_state.step == 0:
    st.markdown("**NB: Du skal trykke på hver knap to gange!")
    if centered_button("Start testen"):
        next_step()

# Step 1 – Antal besøg
elif st.session_state.step == 1:
    st.header("Hvor mange gange tror du, du kommer til at besøge Tivoli i år?")
    if centered_button("Bare én gang"): st.session_state.besoeg = "Bare én gang"; next_step()
    if centered_button("To til tre gange"): st.session_state.besoeg = "To til tre gange"; next_step()
    if centered_button("Tre eller flere gange"): st.session_state.besoeg = "Tre eller flere gange"; next_step()
    if centered_button("Det ved jeg ikke endnu"): st.session_state.besoeg = "Det ved jeg ikke endnu"; next_step()

# Step 2 – Koncerter
elif st.session_state.step == 2:
    st.header("Er du typen, der nyder en god koncert i Tivoli?")
    if centered_button("Ja, helt sikkert"): st.session_state.koncert = "Ja, helt sikkert"; go_to(21)
    if centered_button("Af og til"): st.session_state.koncert = "Af og til"; go_to(21)
    if centered_button("Nej, det er ikke lige mig"): st.session_state.koncert = "Nej, det er ikke lige mig"; next_step()

# Step 21 – Vurder artister
elif st.session_state.step == 21:
    if st.session_state.artist_index < len(artists):
        artist = artists[st.session_state.artist_index]
        st.subheader(f"🎤 {artist['name']}")
        show_image(artist["img"])
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("🔥 Hot", key=f"hot_{artist['name']}", use_container_width=True):
                st.session_state.artist_hot[artist["name"]] = 1
                st.session_state.artist_index += 1
        with col2:
            if st.button("❌ Not", key=f"not_{artist['name']}", use_container_width=True):
                st.session_state.artist_hot[artist["name"]] = 0
                st.session_state.artist_index += 1
        if st.session_state.artist_index >= len(artists):
            st.session_state.artist_index = 0
            go_to(3)

# Step 3 – Madoplevelser
elif st.session_state.step == 3:
    st.header("Hvilken type madoplevelser er du mest interesseret i i Tivoli?")
    if centered_button("Madboder og Tivolis Food Hall"): st.session_state.mad = "Madboder og Tivolis Food Hall"; next_step()
    if centered_button("Gourmet og fine dining"): st.session_state.mad = "Gourmet og fine dining"; next_step()
    if centered_button("Begge dele"): st.session_state.mad = "Begge dele"; next_step()
    if centered_button("Jeg spiser sjældent i Tivoli"): st.session_state.mad = "Jeg spiser sjældent i Tivoli"; next_step()

# Step 4 – Forlystelser
elif st.session_state.step == 4:
    st.header("Hvor meget betyder forlystelser for dit besøg i Tivoli?")
    if centered_button("Jeg elsker dem – det er et must"): st.session_state.forlystelser = "Jeg elsker dem – det er et must"; next_step()
    if centered_button("Jeg prøver gerne et par stykker"): st.session_state.forlystelser = "Jeg prøver gerne et par stykker"; next_step()
    if centered_button("Jeg bruger dem sjældent eller aldrig"): st.session_state.forlystelser = "Jeg bruger dem sjældent eller aldrig"; next_step()

# Step 5 – Forestillinger
elif st.session_state.step == 5:
    st.header("Er du interesseret i forestillinger som teater, dans eller musicals i haven?")
    if centered_button("Ja, det er noget af det bedste"): st.session_state.forestillinger = "Ja, det er noget af det bedste"; go_to(51)
    if centered_button("Nogle gange, hvis det passer ind"): st.session_state.forestillinger = "Nogle gange, hvis det passer ind"; go_to(51)
    if centered_button("Nej, det er ikke lige mig"): st.session_state.forestillinger = "Nej, det er ikke lige mig"; go_to(6)

# Step 51 – Vurder forestillinger
elif st.session_state.step == 51:
    if st.session_state.performance_index < len(performances):
        perf = performances[st.session_state.performance_index]
        st.subheader(f"🎭 {perf['name']}")
        show_image(perf["img"])
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("👍 Interesseret", key=f"inter_{perf['name']}", use_container_width=True):
                st.session_state.performance_hot[perf['name']] = 1
                st.session_state.performance_index += 1
        with col2:
            if st.button("👎 Ikke mig", key=f"not_inter_{perf['name']}", use_container_width=True):
                st.session_state.performance_hot[perf['name']] = 0
                st.session_state.performance_index += 1
        if st.session_state.performance_index >= len(performances):
            st.session_state.performance_index = 0
            go_to(6)

# Step 6 – Resultat
elif st.session_state.step == 6:
    st.header("🌟 Din Tivoli-profil")
    tags = []

    if any(st.session_state.artist_hot.get(n["name"]) for n in artists[:3]):
        tags.append("Fredagsrock")
    if st.session_state.artist_hot.get("Fraads"):
        tags.append("Mint")
    if st.session_state.artist_hot.get("Poul Krebs"):
        tags.append("Lørdagshits")

    if st.session_state.mad in ["Madboder og Tivolis Food Hall", "Begge dele"]:
        tags.append("Casual dining")
    if st.session_state.mad in ["Gourmet og fine dining", "Begge dele"]:
        tags.append("Gourmet")

    if st.session_state.forlystelser in ["Jeg elsker dem – det er et must", "Jeg prøver gerne et par stykker"]:
        tags.append("Forlystelser")

    for perf, interested in st.session_state.performance_hot.items():
        if interested:
            tags.append(perf)

    st.success("Din Tivoli-profil:")
    st.write(", ".join(tags) if tags else "Ingen relevante segmenter endnu.")
    st.markdown(f"**Antal besøg:** {st.session_state.get('besoeg', 'Ikke besvaret')}")
