
import streamlit as st
import os
from PIL import Image

st.set_page_config(page_title="Tivoli Segmenteringsflow", layout="centered", initial_sidebar_state="collapsed")

# Constants for image widths
IMG_WIDTH = 400
LOGO_WIDTH = 200

# Helper: Centered image
def show_image(path, logo=False):
    if os.path.exists(path):
        img = Image.open(path)
        width = LOGO_WIDTH if logo else IMG_WIDTH
        height = int((width / img.width) * img.height)
        col = st.columns([1, 3, 1])[1]
        with col:
            st.image(img.resize((width, height)), use_container_width=False)

# Helper: Consistent-width button block with minimal vertical spacing
def styled_button_block(options, keys, actions):
    for label, key, action in zip(options, keys, actions):
        col = st.columns([1, 3, 1])[1]
        with col:
            if st.button(label, key=key):
                action()
        st.markdown("<div style='margin: -12px;'></div>", unsafe_allow_html=True)

# Setup artists and performances
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

# State init
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

# UI START
show_image("tivoli_logo.png", logo=True)
st.title("🎡 Din Tivoli-profil")

# Step 1
if st.session_state.step == 1:
    st.header("Spørgsmål 1")
    styled_button_block(
        ["Bare én gang", "To til tre gange", "Tre eller flere gange", "Det ved jeg ikke endnu"],
        ["s1a", "s1b", "s1c", "s1d"],
        [
            lambda: (st.session_state.__setitem__("besoeg", "Bare én gang"), next_step()),
            lambda: (st.session_state.__setitem__("besoeg", "To til tre gange"), next_step()),
            lambda: (st.session_state.__setitem__("besoeg", "Tre eller flere gange"), next_step()),
            lambda: (st.session_state.__setitem__("besoeg", "Det ved jeg ikke endnu"), next_step())
        ]
    )

# Step 2
elif st.session_state.step == 2:
    st.header("Spørgsmål 2")
    styled_button_block(
        ["Ja, helt sikkert", "Af og til", "Nej, det er ikke lige mig"],
        ["s2a", "s2b", "s2c"],
        [
            lambda: (st.session_state.__setitem__("koncert", "Ja, helt sikkert"), go_to(21)),
            lambda: (st.session_state.__setitem__("koncert", "Af og til"), go_to(21)),
            lambda: (st.session_state.__setitem__("koncert", "Nej, det er ikke lige mig"), next_step())
        ]
    )

# Step 21 – Artist Preference
elif st.session_state.step == 21:
    if st.session_state.artist_index < len(artists):
        artist = artists[st.session_state.artist_index]
        st.subheader(f"🎤 {artist['name']}")
        show_image(artist["img"])
        col1, col2 = st.columns([1, 1, 1], gap="small")[0:2]
        with col1:
            if st.button("🔥 Hot", key=f"hot_{artist['name']}"):
                st.session_state.artist_hot[artist["name"]] = 1
                st.session_state.artist_index += 1
        with col2:
            if st.button("❌ Not", key=f"not_{artist['name']}"):
                st.session_state.artist_hot[artist["name"]] = 0
                st.session_state.artist_index += 1
        if st.session_state.artist_index >= len(artists):
            st.session_state.artist_index = 0
            go_to(3)

# Step 3 – Food
elif st.session_state.step == 3:
    st.header("Spørgsmål 3")
    styled_button_block(
        ["Casual mad som boder og Food Hall", "Gourmet og fine dining", "Begge dele", "Jeg spiser sjældent i Tivoli"],
        ["s3a", "s3b", "s3c", "s3d"],
        [
            lambda: (st.session_state.__setitem__("mad", "Casual mad som boder og Food Hall"), next_step()),
            lambda: (st.session_state.__setitem__("mad", "Gourmet og fine dining"), next_step()),
            lambda: (st.session_state.__setitem__("mad", "Begge dele"), next_step()),
            lambda: (st.session_state.__setitem__("mad", "Jeg spiser sjældent i Tivoli"), next_step())
        ]
    )

# Step 4 – Rides
elif st.session_state.step == 4:
    st.header("Spørgsmål 4")
    styled_button_block(
        ["Jeg elsker dem – det er et must", "Jeg prøver gerne et par stykker", "Jeg bruger dem sjældent eller aldrig"],
        ["s4a", "s4b", "s4c"],
        [
            lambda: (st.session_state.__setitem__("forlystelser", "Jeg elsker dem – det er et must"), next_step()),
            lambda: (st.session_state.__setitem__("forlystelser", "Jeg prøver gerne et par stykker"), next_step()),
            lambda: (st.session_state.__setitem__("forlystelser", "Jeg bruger dem sjældent eller aldrig"), next_step())
        ]
    )

# Step 5 – Show Interest
elif st.session_state.step == 5:
    st.header("Spørgsmål 5")
    styled_button_block(
        ["Ja, det er noget af det bedste", "Nogle gange, hvis det passer ind", "Nej, det er ikke lige mig"],
        ["s5a", "s5b", "s5c"],
        [
            lambda: (st.session_state.__setitem__("forestillinger", "Ja, det er noget af det bedste"), go_to(51)),
            lambda: (st.session_state.__setitem__("forestillinger", "Nogle gange, hvis det passer ind"), go_to(51)),
            lambda: (st.session_state.__setitem__("forestillinger", "Nej, det er ikke lige mig"), go_to(6))
        ]
    )

# Step 51 – Show Preferences
elif st.session_state.step == 51:
    if st.session_state.performance_index < len(performances):
        perf = performances[st.session_state.performance_index]
        st.subheader(f"🎭 {perf['name']}")
        show_image(perf["img"])
        col1, col2 = st.columns([1, 1, 1], gap="small")[0:2]
        with col1:
            if st.button("👍 Interesseret", key=f"inter_{perf['name']}"):
                st.session_state.performance_hot[perf["name"]] = 1
                st.session_state.performance_index += 1
        with col2:
            if st.button("👎 Ikke mig", key=f"not_inter_{perf['name']}"):
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
