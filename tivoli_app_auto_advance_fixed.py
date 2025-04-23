
import streamlit as st

st.set_page_config(page_title="Tivoli Segmenteringsflow", layout="centered", initial_sidebar_state="collapsed")

if "step" not in st.session_state:
    st.session_state.step = 1
if "kunstner_svar" not in st.session_state:
    st.session_state.kunstner_svar = []
if "scenevalg" not in st.session_state:
    st.session_state.scenevalg = []

st.markdown(
    """
    <style>
        .stRadio > div {
            flex-direction: column;
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
    koncert_valg = st.radio("Er du typen, der nyder en god koncert i Tivoli?", [
        "Ja, helt sikkert", "Af og til", "Nej, det er ikke lige mig"
    ])
    if koncert_valg:
        st.session_state.koncert_valg = koncert_valg
        st.session_state.step = 21 if koncert_valg in ["Ja, helt sikkert", "Af og til"] else 3

elif st.session_state.step == 21:
    st.header("Spørgsmål 2.1")
    kunstner_svar = st.multiselect("Hvilke af disse kunstnere kan du lide?", [
        "Hans Philip", "Thomas Helmig", "Tom Jones", "Fraads", "Poul Krebs"
    ])
    if kunstner_svar:
        st.session_state.kunstner_svar = kunstner_svar
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
        st.session_state.step = 51 if forestillinger != "Nej, det er ikke lige mig" else 6

elif st.session_state.step == 51:
    st.header("Spørgsmål 5.1")
    scenevalg = st.multiselect("Hvilke typer forestillinger interesserer dig?", [
        "Teater", "Musicals", "Dans og Ballet", "Revy og Comedy"
    ])
    if scenevalg:
        st.session_state.scenevalg = scenevalg
        st.session_state.step = 6

elif st.session_state.step == 6:
    st.header("🎯 Din profil")
    tags = []

    if "Hans Philip" in st.session_state.kunstner_svar or "Thomas Helmig" in st.session_state.kunstner_svar:
        tags.append("Fredagsrock")
    if "Fraads" in st.session_state.kunstner_svar:
        tags.append("Mint")
    if "Poul Krebs" in st.session_state.kunstner_svar:
        tags.append("Lørdagshits")

    if st.session_state.mad == "Casual mad som boder og Food Hall" or st.session_state.mad == "Begge dele":
        tags.append("Street Food")
    if st.session_state.mad == "Gourmet og fine dining" or st.session_state.mad == "Begge dele":
        tags.append("Gourmet")

    tags += st.session_state.scenevalg
    st.success("Din Tivoli-profil:")
    st.write(", ".join(tags) if tags else "Ingen relevante segmenter endnu.")
