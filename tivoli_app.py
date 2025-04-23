
import streamlit as st

st.set_page_config(page_title="Tivoli Segmenteringsflow", layout="centered")

st.title("🎡 Velkommen til Tivoli")

besoeg = st.radio("🔸 Hvor mange gange tror du, du kommer til at besøge Tivoli i år?", [
    "Bare én gang", "To til tre gange", "Tre eller flere gange", "Det ved jeg ikke endnu"
])

koncert = st.radio("🔸 Er du typen, der nyder en god koncert i Tivoli?", [
    "Ja, helt sikkert", "Af og til", "Nej, det er ikke lige mig"
])

kunstner_svar = []
if koncert in ["Ja, helt sikkert", "Af og til"]:
    st.subheader("🎵 Hvilke af disse kunstnere kan du lide?")
    kunstner_svar = st.multiselect("Vælg dem du kan lide", [
        "Hans Philip", "Thomas Helmig", "Tom Jones", "Fraads", "Poul Krebs"
    ])

mad = st.radio("🔸 Hvilken type madoplevelser er du mest interesseret i i Tivoli?", [
    "Casual mad som boder og Food Hall", "Gourmet og fine dining", "Begge dele", "Jeg spiser sjældent i Tivoli"
])

forlystelser = st.radio("🔸 Hvor meget betyder forlystelser for dit besøg i Tivoli?", [
    "Jeg elsker dem – det er et must", "Jeg prøver gerne et par stykker", "Jeg bruger dem sjældent eller aldrig"
])

forestillinger = st.radio("🔸 Er du interesseret i forestillinger som teater, dans eller musicals i haven?", [
    "Ja, det er noget af det bedste", "Nogle gange, hvis det passer ind", "Nej, det er ikke lige mig"
])

scenevalg = []
if forestillinger != "Nej, det er ikke lige mig":
    st.subheader("🎭 Hvilke typer forestillinger interesserer dig?")
    scenevalg = st.multiselect("Vælg en eller flere", [
        "Teater", "Musicals", "Dans og Ballet", "Revy og Comedy"
    ])

if st.button("🔍 Generér min Tivoli-profil"):
    tags = []
    if "Hans Philip" in kunstner_svar or "Thomas Helmig" in kunstner_svar:
        tags.append("Fredagsrock")
    if "Fraads" in kunstner_svar:
        tags.append("Mint")
    if "Poul Krebs" in kunstner_svar:
        tags.append("Lørdagshits")

    if mad == "Casual mad som boder og Food Hall" or mad == "Begge dele":
        tags.append("Street Food")
    if mad == "Gourmet og fine dining" or mad == "Begge dele":
        tags.append("Gourmet")

    tags += scenevalg
    st.success("🎯 Din profil:")
    st.write(", ".join(tags) if tags else "Ingen relevante segmenter endnu.")
