"""
Página de registro diario de Stress App.

Permite registrar el nivel de estrés académico
y guardar comentarios opcionales del estudiante.
"""

import streamlit as st
from datetime import date

from src.data_manager import (
    guardar_registro,
    cargar_registros
)


def mostrar_registro():
    """
    Muestra el formulario de registro diario.

    Recibe:
        No recibe parámetros.

    Devuelve:
        None. Muestra el formulario en Streamlit
        y guarda los registros mediante data_manager.
    """

    st.title("📝 Registro diario")
    st.write(
        "Registra cómo te has sentido hoy. "
        "Esto nos ayudará a comprender tu estrés académico."
    )

    # Crear formulario
    with st.form("formulario_registro"):

        fecha = st.date_input(
            "Fecha del registro",
            value=date.today()
        )

        nivel = st.slider(
            "¿Cuál es tu nivel de estrés hoy?",
            min_value=1,
            max_value=10,
            value=5
        )

        st.caption(
            "1 representa un nivel bajo de estrés "
            "y 10 un nivel alto."
        )

        nota = st.text_area(
            "¿Quieres agregar algún comentario?",
            placeholder="Escribe cómo te has sentido..."
        )

        enviar = st.form_submit_button(
            "Guardar registro"
        )

        if enviar:

            resultado = guardar_registro(
                fecha,
                nivel,
                nota
            )

            if resultado:
                st.success("¡Tu registro se guardó correctamente! 🌿")
            else:
                st.error(
                    "No fue posible guardar el registro. "
                    "Verifica los datos e inténtalo nuevamente."
                )

    # Mostrar historial
    st.divider()
    st.subheader("📊 Historial de registros")

    registros = cargar_registros()

    if registros.empty:
        st.info("Todavía no tienes registros guardados.")

    else:
        registros_mostrar = registros.copy()

        registros_mostrar["fecha"] = (
            registros_mostrar["fecha"].dt.strftime("%d/%m/%Y")
        )

        st.dataframe(
            registros_mostrar,
            use_container_width=True,
            hide_index=True
        )


# Ejecutar la página
mostrar_registro()