"""Página de análisis de los registros de Stress App."""

import streamlit as st

from src.data_manager import cargar_registros
from src.stress_analysis import (
    analizar_tendencia,
    calcular_mediana,
    calcular_promedio,
    clasificar_estres,
)


def mostrar_analisis():
    """Muestra estadísticas y la evolución histórica del estrés."""
    st.title("📈 Análisis")
    st.write("Consulta un resumen de tus niveles de estrés registrados.")
    registros = cargar_registros()
    if registros.empty:
        st.info("Todavía no tienes registros para analizar.")
        return

    # Trabajar sobre una copia evita modificar los registros originales.
    datos = registros.sort_values("fecha").copy()
    promedio = calcular_promedio(datos)
    mediana = calcular_mediana(datos)
    frecuente = datos["nivel_estres"].mode().iloc[0]
    tendencia = analizar_tendencia(datos)

    columna_1, columna_2, columna_3 = st.columns(3)
    columna_1.metric("Promedio", f"{promedio:.1f}/10")
    columna_2.metric("Mediana", f"{mediana:.1f}/10")
    columna_3.metric("Nivel más frecuente", f"{frecuente}/10")

    st.subheader("Evolución del estrés")
    st.line_chart(datos.set_index("fecha")[["nivel_estres"]])

    clasificacion = clasificar_estres(promedio)
    mensajes = {
        "bajo": "Tu promedio de estrés se encuentra en un nivel bajo.",
        "moderado": "Tu promedio de estrés se encuentra en un nivel moderado.",
        "alto": "Tu promedio de estrés se encuentra en un nivel alto.",
    }
    st.write(mensajes[clasificacion])
    if tendencia is None:
        st.caption("Agrega más registros para conocer la tendencia.")
    else:
        st.caption(f"La tendencia de tus registros {tendencia}.")


mostrar_analisis()
