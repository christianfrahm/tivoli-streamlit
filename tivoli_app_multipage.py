
import streamlit as st

st.set_page_config(page_title="Tivoli Segmenteringsflow", layout="centered")

if "step" not in st.session_state:
    st.session_state.step = 1
if "kunstner_svar" not in st.session_state:
    st.session_state.kunstner_svar = []
if "scenevalg" not in st.session_state:
    st.session_state.scenevalg = []

st.title("🎡 Din Tivoli-profil")

if st.session_state.step == 1:
    st.header("Spørgsmål 1")
    besoeg = st.radio("Hvor mange gange tror du, du kommer til at besøge Tivoli i år?", [
        "Bare én gang", "To til tre gange", "Tre eller flere gange", "Det ved jeg ikke endnu"
    ])
    if st.button("Næste"):
        st.session_state.step = 2

elif st.session_state.step == 2:
    st.header("Spørgsmål 2")
    koncert = st.radio("Er du typen, der nyder en god koncert i Tivoli?", [
        "Ja, helt sikkert", "Af og til", "Nej, det er ikke lige mig"
    ])
    st.session_state.koncert = koncert
    if st.button("Næste"):
        if koncert in ["Ja, helt sikkert", "Af og til"]:
            st.session_state.step = 21
        else:
            st.session_state.step = 3

elif st.session_state.step == 21:
    st.header("Spørgsmål 2.1")
    st.session_state.kunstner_svar = st.multiselect("Hvilke af disse kunstnere kan du lide?", [
        "Hans Philip", "Thomas Helmig", "Tom Jones", "Fraads", "Poul Krebs"
    ])
    if st.button("Næste"):
        st.session_state.step = 3

elif st.session_state.step == 3:
    st.header("Spørgsmål 3")
    mad = st.radio("Hvilken type madoplevelser er du mest interesseret i i Tivoli?", [
        "Casual mad som boder og Food Hall", "Gourmet og fine dining", "Begge dele", "Jeg spiser sjældent i Tivoli"
    ])
    st.session_state.mad = mad
    if st.button("Næste"):
        st.session_state.step = 4

elif st.session_state.step == 4:
    st.header("Spørgsmål 4")
    forlystelser = st.radio("Hvor meget betyder forlystelser for dit besøg i Tivoli?", [
        "Jeg elsker dem – det er et must", "Jeg prøver gerne et par stykker", "Jeg bruger dem sjældent eller aldrig"
    ])
    st.session_state.forlystelser = forlystelser
    if st.button("Næste"):
        st.session_state.step = 5

elif st.session_state.step == 5:
    st.header("Spørgsmål 5")
    forestillinger = st.radio("Er du interesseret i forestillinger som teater, dans eller musicals i haven?", [
        "Ja, det er noget af det bedste", "Nogle gange, hvis det passer ind", "Nej, det er ikke lige mig"
    ])
    st.session_state.forestillinger = forestillinger
    if st.button("Næste"):
        if forestillinger != "Nej, det er ikke lige mig":
            st.session_state.step = 51
        else:
            st.session_state.step = 6

elif st.session_state.step == 51:
    st.header("Spørgsmål 5.1")
    st.session_state.scenevalg = st.multiselect("Hvilke typer forestillinger interesserer dig?", [
        "Teater", "Musicals", "Dans og Ballet", "Revy og Comedy"
    ])
    if st.button("Næste"):
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
