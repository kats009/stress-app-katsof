import streamlit as st

st.set_page_config(
    page_title="Stress App",
    page_icon="🌿",
    layout="wide")

st.title("🌿 Stress App")

st.write(
    "Una aplicación diseñada para ayudarte a registrar, "
    "comprender y manejar tu estrés académico.")

st.subheader("¿Cómo te sientes hoy?")

nivel = st.slider(
    "Selecciona tu nivel de estrés:",
    min_value=1,
    max_value=10,
    value=5)

if st.button("Registrar"):
    st.success(f"Tu nivel de estrés de hoy es {nivel}/10.")
