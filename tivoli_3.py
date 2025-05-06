import streamlit as st
import os
from PIL import Image

# Page config
st.set_page_config(page_title="Tivoli Segmentation Flow", layout="centered", initial_sidebar_state="collapsed")
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
    {"name": "Theatre", "img": "teater.png"},
    {"name": "Musicals", "img": "musical.png"},
    {"name": "Dance and Ballet", "img": "ballet.png"},
    {"name": "Revue and Comedy", "img": "revy.png"},
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
st.title("🌩️ Your Tivoli Profile")

# Step 0 – Welcome screen
if st.session_state.step == 0:
    st.markdown("**Note: You might need to click each button twice due to a Streamlit bug in some browsers!**")
    if centered_button("Start the test"):
        next_step()

# Step 1 – Visit frequency
elif st.session_state.step == 1:
    st.header("How many times do you think you’ll visit Tivoli this year?")
    if centered_button("Just once"): st.session_state.besoeg = "Just once"; next_step()
    if centered_button("Two to three times"): st.session_state.besoeg = "Two to three times"; next_step()
    if centered_button("Three or more times"): st.session_state.besoeg = "Three or more times"; next_step()
    if centered_button("I don’t know yet"): st.session_state.besoeg = "I don’t know yet"; next_step()

# Step 2 – Concerts
elif st.session_state.step == 2:
    st.header("Do you enjoy a good concert in Tivoli?")
    if centered_button("Absolutely!"): st.session_state.koncert = "Absolutely!"; go_to(21)
    if centered_button("Sometimes"): st.session_state.koncert = "Sometimes"; go_to(21)
    if centered_button("Not really my thing"): st.session_state.koncert = "Not really my thing"; next_step()

# Step 21 – Artist preference
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

# Step 3 – Food preferences
elif st.session_state.step == 3:
    st.header("What type of dining experiences are you most interested in at Tivoli?")
    if centered_button("Food stalls and Tivoli Food Hall"): st.session_state.mad = "Food stalls and Tivoli Food Hall"; next_step()
    if centered_button("Gourmet and fine dining"): st.session_state.mad = "Gourmet and fine dining"; next_step()
    if centered_button("Both"): st.session_state.mad = "Both"; next_step()
    if centered_button("I rarely eat at Tivoli"): st.session_state.mad = "I rarely eat at Tivoli"; next_step()

# Step 4 – Rides
elif st.session_state.step == 4:
    st.header("How important are rides for your Tivoli visit?")
    if centered_button("I love them – a must"): st.session_state.forlystelser = "I love them – a must"; next_step()
    if centered_button("I enjoy a few"): st.session_state.forlystelser = "I enjoy a few"; next_step()
    if centered_button("I rarely or never use them"): st.session_state.forlystelser = "I rarely or never use them"; next_step()

# Step 5 – Shows and performances
elif st.session_state.step == 5:
    st.header("Are you interested in shows like theatre, dance, or musicals?")
    if centered_button("Yes, that’s one of the best parts"): st.session_state.forestillinger = "Yes, that’s one of the best parts"; go_to(51)
    if centered_button("Sometimes, if it fits in"): st.session_state.forestillinger = "Sometimes, if it fits in"; go_to(51)
    if centered_button("Not really for me"): st.session_state.forestillinger = "Not really for me"; go_to(6)

# Step 51 – Performance interest
elif st.session_state.step == 51:
    if st.session_state.performance_index < len(performances):
        perf = performances[st.session_state.performance_index]
        st.subheader(f"🎭 {perf['name']}")
        show_image(perf["img"])
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("👍 Interested", key=f"inter_{perf['name']}", use_container_width=True):
                st.session_state.performance_hot[perf['name']] = 1
                st.session_state.performance_index += 1
        with col2:
            if st.button("👎 Not for me", key=f"not_inter_{perf['name']}", use_container_width=True):
                st.session_state.performance_hot[perf['name']] = 0
                st.session_state.performance_index += 1
        if st.session_state.performance_index >= len(performances):
            st.session_state.performance_index = 0
            go_to(6)

# Step 6 – Result
elif st.session_state.step == 6:
    st.header("🌟 Your Tivoli Profile")
    tags = []

    if any(st.session_state.artist_hot.get(n["name"]) for n in artists[:3]):
        tags.append("Friday Rock")
    if st.session_state.artist_hot.get("Fraads"):
        tags.append("Mint")
    if st.session_state.artist_hot.get("Poul Krebs"):
        tags.append("Saturday Hits")

    if st.session_state.mad in ["Food stalls and Tivoli Food Hall", "Both"]:
        tags.append("Casual Dining")
    if st.session_state.mad in ["Gourmet and fine dining", "Both"]:
        tags.append("Gourmet")

    if st.session_state.forlystelser in ["I love them – a must", "I enjoy a few"]:
        tags.append("Rides")

    for perf, interested in st.session_state.performance_hot.items():
        if interested:
            tags.append(perf)

    st.success("Your Tivoli Profile:")
    st.write(", ".join(tags) if tags else "No relevant segments yet.")
    st.markdown(f"**Visit frequency:** {st.session_state.get('besoeg', 'Not answered')}")
