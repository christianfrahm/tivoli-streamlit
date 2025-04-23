
import streamlit as st
import os
from PIL import Image

st.set_page_config(page_title="Tivoli Segmenteringsflow", layout="centered", initial_sidebar_state="collapsed")

# Fixed sizes
IMG_WIDTH = 400
LOGO_WIDTH = 200

# Helper: Show centered image with fixed size
def show_image(path, logo=False):
    if os.path.exists(path):
        img = Image.open(path)
        width = LOGO_WIDTH if logo else IMG_WIDTH
        height = int((width / img.width) * img.height)
        col = st.columns([1, 3, 1])[1]
        with col:
            st.image(img.resize((width, height)), use_container_width=False)

# Helper: Show centered full-width button using markdown for fixed width
def styled_button(label, key):
    col = st.columns([1, 3, 1])[1]
    return col.button(label, key=key)

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

for key, default in {
    "step": 1,
    "artist_index": 0,
    "performance_index": 0,
    "artist_hot": {},
    "performance_hot": {},
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

def next_step(): st.session_state.step += 1
def go_to(step): st.session_state.step = step

show_image("tivoli_logo.png", logo=True)
st.title("🎡 Din Tivoli-profil")

# Step 1
if st.session_state.step == 1:
    st.header("Spørgsmål 1")
    if styled_button("Bare én gang", key="s1a"): st.session_state.besoeg = "Bare én gang"; next_step()
    if styled_button("To til tre gange", key="s1b"): st.session_state.besoeg = "To til tre gange"; next_step()
    if styled_button("Tre eller flere gange", key="s1c"): st.session_state.besoeg = "Tre eller flere gange"; next_step()
    if styled_button("Det ved jeg ikke endnu", key="s1d"): st.session_state.besoeg = "Det ved jeg ikke endnu"; next_step()

# Step 2
elif st.session_state.step == 2:
    st.header("Spørgsmål 2")
    if styled_button("Ja, helt sikkert", key="s2a"): st.session_state.koncert = "Ja, helt sikkert"; go_to(21)
    if styled_button("Af og til", key="s2b"): st.session_state.koncert = "Af og til"; go_to(21)
    if styled_button("Nej, det er ikke lige mig", key="s2c"): st.session_state.koncert = "Nej, det er ikke lige mig"; next_step()

# Step 21 – Artist Preference
elif st.session_state.step == 21:
    if st.session_state.artist_index < len(artists):
        artist = artists[st.session_state.artist_index]
        st.subheader(f"🎤 {artist['name']}")
        show_image(artist["img"])
        col1, col2 = st.columns([1, 3, 1])[1].columns(2)
        if col1.button("🔥 Hot", key=f"hot_{artist['name']}"):
            st.session_state.artist_hot[artist["name"]] = 1
            st.session_state.artist_index += 1
        if col2.button("❌ Not", key=f"not_{artist['name']}"):
            st.session_state.artist_hot[artist["name"]] = 0
            st.session_state.artist_index += 1
        if st.session_state.artist_index >= len(artists):
            st.session_state.artist_index = 0
            go_to(3)

# Step 3 – Food
elif st.session_state.step == 3:
    st.header("Spørgsmål 3")
    if styled_button("Casual mad som boder og Food Hall", key="s3a"): st.session_state.mad = "Casual mad som boder og Food Hall"; next_step()
    if styled_button("Gourmet og fine dining", key="s3b"): st.session_state.mad = "Gourmet og fine dining"; next_step()
    if styled_button("Begge dele", key="s3c"): st.session_state.mad = "Begge dele"; next_step()
    if styled_button("Jeg spiser sjældent i Tivoli", key="s3d"): st.session_state.mad = "Jeg spiser sjældent i Tivoli"; next_step()

# Step 4 – Rides
elif st.session_state.step == 4:
    st.header("Spørgsmål 4")
    if styled_button("Jeg elsker dem – det er et must", key="s4a"): st.session_state.forlystelser = "Jeg elsker dem – det er et must"; next_step()
    if styled_button("Jeg prøver gerne et par stykker", key="s4b"): st.session_state.forlystelser = "Jeg prøver gerne et par stykker"; next_step()
    if styled_button("Jeg bruger dem sjældent eller aldrig", key="s4c"): st.session_state.forlystelser = "Jeg bruger dem sjældent eller aldrig"; next_step()

# Step 5 – Show Interest
elif st.session_state.step == 5:
    st.header("Spørgsmål 5")
    if styled_button("Ja, det er noget af det bedste", key="s5a"): st.session_state.forestillinger = "Ja, det er noget af det bedste"; go_to(51)
    if styled_button("Nogle gange, hvis det passer ind", key="s5b"): st.session_state.forestillinger = "Nogle gange, hvis det passer ind"; go_to(51)
    if styled_button("Nej, det er ikke lige mig", key="s5c"): st.session_state.forestillinger = "Nej, det er ikke lige mig"; go_to(6)

# Step 51 – Show Preferences
elif st.session_state.step == 51:
    if st.session_state.performance_index < len(performances):
        perf = performances[st.session_state.performance_index]
        st.subheader(f"🎭 {perf['name']}")
        show_image(perf["img"])
        col1, col2 = st.columns([1, 3, 1])[1].columns(2)
        if col1.button("👍 Interesseret", key=f"inter_{perf['name']}"):
            st.session_state.performance_hot[perf["name"]] = 1
            st.session_state.performance_index += 1
        if col2.button("👎 Ikke mig", key=f"not_inter_{perf['name']}"):
            st.session_state.performance_hot[perf["name"]] = 0
            st.session_state.performance_index += 1
        if st.session_state.performance_index >= len(performances):
            st.session_state.performance_index = 0
            go_to(6)

# Step 6 – Output
elif st.session_state.step == 6:
    st.header("🎯 Din Tivoli-profil")
    tags = []

    if any(st.session_state.artist_hot.get(n["name"]) for n in artists[:3]):
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
