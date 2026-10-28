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

# Copilot, desarrolla la pantalla principal de Stress App
# utilizando Python y Streamlit.
#
# Objetivo:
# Crear una aplicación para ayudar a estudiantes
# de preparatoria a registrar y comprender su
# estrés académico.
#
# Función: main()
#
# Recibe:
# - No recibe parámetros directamente.
# - Utiliza las interacciones del usuario.
#
# Devuelve:
# - Una interfaz visual de Streamlit.
#
# Funcionalidades:
# - Mostrar el título "Stress App".
# - Presentar una bienvenida.
# - Explicar el objetivo de la aplicación.
# - Mostrar instrucciones de navegación.
# - Integrar las páginas de registro diario,
#   análisis, calendario, recomendaciones
#   y respiración.
#
# Casos borde:
# - Datos inexistentes.
# - Archivos faltantes.
# - Errores al cargar las páginas.
#
# Requisitos:
# - Usar Streamlit.
# - Mantener un diseño sencillo y agradable.
# - Evitar colores demasiado llamativos.
# - Incluir docstring en español.
# - Agregar comentarios en español.
# - No duplicar funciones de otros archivos.
