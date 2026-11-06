"""Página para consultar registros de estrés por fecha."""

from datetime import date

import streamlit as st

from src.data_manager import cargar_registros


def mostrar_calendario():
    """Muestra todos los registros correspondientes a la fecha elegida."""
    st.title("📅 Calendario")
    st.write("Selecciona una fecha para consultar tus registros de estrés.")
    fecha_seleccionada = st.date_input(
        "Fecha que deseas consultar", value=date.today()
    )
    registros = cargar_registros()
    if registros.empty:
        st.info("Todavía no tienes registros guardados.")
        return

    # Comparar solo la fecha permite consultar todos los registros del día.
    registros_fecha = registros[
        registros["fecha"].dt.date == fecha_seleccionada
    ].copy()
    if registros_fecha.empty:
        st.info("No hay registros para la fecha seleccionada.")
        return

    st.subheader(f"Registros del {fecha_seleccionada.strftime('%d/%m/%Y')}")
    registros_fecha["fecha"] = registros_fecha["fecha"].dt.strftime("%d/%m/%Y")
    st.dataframe(registros_fecha, use_container_width=True, hide_index=True)


mostrar_calendario()
