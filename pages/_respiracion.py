"""Página de ejercicios suaves de respiración."""

import streamlit as st


EJERCICIOS = {
    "Respiración tranquila": (4, 6),
    "Respiración equilibrada": (5, 5),
}


def mostrar_respiracion():
    """Muestra una guía visual que no bloquea la aplicación."""
    st.title("🫁 Respiración")
    st.write(
        "Elige un ejercicio, respira con comodidad y detente si sientes malestar."
    )
    ejercicio = st.selectbox("Ejercicio", list(EJERCICIOS))
    ciclos = st.slider("Cantidad de ciclos", min_value=1, max_value=10, value=5)
    inhalar, exhalar = EJERCICIOS[ejercicio]
    st.write(f"Inhala suavemente {inhalar} segundos.")
    st.write(f"Exhala lentamente {exhalar} segundos. No contengas el aire.")
    st.caption(f"Duración aproximada: {(inhalar + exhalar) * ciclos} segundos.")

    if "respiracion_activa" not in st.session_state:
        st.session_state.respiracion_activa = False
    columna_1, columna_2 = st.columns(2)
    if columna_1.button("Iniciar", disabled=st.session_state.respiracion_activa):
        st.session_state.respiracion_activa = True
    if columna_2.button("Detener", disabled=not st.session_state.respiracion_activa):
        st.session_state.respiracion_activa = False

    if st.session_state.respiracion_activa:
        duracion = inhalar + exhalar
        st.markdown(
            f"""
            <style>
            @keyframes respirar {{
                0%, 100% {{ transform: scale(0.65); opacity: 0.65; }}
                {inhalar / duracion * 100:.0f}% {{
                    transform: scale(1); opacity: 1;
                }}
            }}
            .circulo-respiracion {{
                width: 150px; height: 150px; margin: 2rem auto;
                border-radius: 50%; background: #8fc7a7;
                animation: respirar {duracion}s ease-in-out {ciclos};
            }}
            </style>
            <div class="circulo-respiracion"></div>
            """,
            unsafe_allow_html=True,
        )
        st.success("Sigue el círculo: inhala al crecer y exhala al reducirse.")
    else:
        st.info("Presiona Iniciar cuando estés listo.")


mostrar_respiracion()
