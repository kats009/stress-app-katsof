"""
Página de recomendaciones de Stress App.

Muestra recomendaciones generales de bienestar,
organización y relajación según el último nivel
de estrés registrado por el estudiante.
"""

import streamlit as st

from src.data_manager import cargar_registros
from src.recommendations import generar_recomendaciones


def mostrar_recomendaciones():
    """
    Muestra recomendaciones según el nivel de estrés.

    Recibe:
        No recibe parámetros directamente.

    Devuelve:
        None. Muestra las recomendaciones en Streamlit.
    """

    st.title("🌿 Recomendaciones")
    st.write(
        "Pequeñas acciones pueden ayudarte a organizar "
        "tus actividades y cuidar tu bienestar."
    )

    # Cargar registros anteriores
    registros = cargar_registros()

    if registros.empty:

        st.info(
            "Todavía no tienes registros de estrés. "
            "Primero completa tu registro diario."
        )

        return

    # Obtener el registro más reciente
    registros = registros.sort_values(
        by="fecha",
        ascending=True
    )

    ultimo_registro = registros.iloc[-1]

    nivel = ultimo_registro["nivel_estres"]

    # Mostrar el nivel de estrés
    st.subheader("Tu último registro")

    st.metric(
        label="Nivel de estrés",
        value=f"{nivel}/10"
    )

    # Clasificar el nivel
    if nivel <= 3:
        st.success("Tu nivel registrado de estrés es bajo.")

    elif nivel <= 6:
        st.warning("Tu nivel registrado de estrés es moderado.")

    else:
        st.error(
            "Tu nivel registrado de estrés es alto. "
            "Recuerda que puedes pedir apoyo si lo necesitas."
        )

    st.divider()

    # Generar recomendaciones
    recomendaciones = generar_recomendaciones(nivel)

    st.subheader("✨ Mostrar recomendaciones")

    if recomendaciones:

        for numero, recomendacion in enumerate(
            recomendaciones, start=1
        ):

            st.markdown(
                f"**{numero}.** {recomendacion}"
            )

    else:
        st.info(
            "No hay recomendaciones disponibles "
            "para este registro."
        )

    st.caption(
        "Estas recomendaciones son orientativas y no "
        "sustituyen la atención de un profesional."
    )


# Ejecutar la página
mostrar_recomendaciones()
