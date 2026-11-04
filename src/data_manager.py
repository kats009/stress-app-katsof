"""
Módulo para administrar los registros de estrés académico.

Permite guardar, cargar y validar los registros
de los estudiantes utilizando archivos CSV.
"""

import pandas as pd
from pathlib import Path

# Ruta principal del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Ubicación del archivo de registros
RUTA_ARCHIVO = BASE_DIR / "data" / "registros.csv"

# Columnas obligatorias
COLUMNAS = ["fecha", "nivel_estres", "nota"]


def validar_registro(fecha, nivel, nota=""):
    """
    Valida los datos de un registro de estrés.

    Recibe:
        fecha: fecha del registro.
        nivel: nivel de estrés del 1 al 10.
        nota: comentario opcional.

    Devuelve:
        True si los datos son válidos.
        False si existe algún dato incorrecto.
    """

    try:
        fecha_validada = pd.to_datetime(fecha, errors="coerce")

        if pd.isna(fecha_validada):
            return False

        nivel = float(nivel)

        if not nivel.is_integer():
            return False

        if nivel < 1 or nivel > 10:
            return False

        if nota is None:
            nota = ""

        if not isinstance(nota, str):
            return False

        return True

    except (ValueError, TypeError, OverflowError):
        return False


def cargar_registros():
    """
    Carga los registros almacenados en el archivo CSV.

    Devuelve:
        Un DataFrame de pandas con los registros.
        Si no existen registros, devuelve un DataFrame vacío.
    """

    # Crear la carpeta data si no existe
    RUTA_ARCHIVO.parent.mkdir(parents=True, exist_ok=True)

    # Crear DataFrame vacío
    datos_vacios = pd.DataFrame(columns=COLUMNAS)

    if not RUTA_ARCHIVO.exists():
        return datos_vacios

    try:
        datos = pd.read_csv(RUTA_ARCHIVO)

        # Comprobar que existan las columnas necesarias
        if not all(columna in datos.columns for columna in COLUMNAS):
            return datos_vacios

        # Conservar únicamente las columnas necesarias
        datos = datos[COLUMNAS].copy()

        # Validar fechas
        datos["fecha"] = pd.to_datetime(
            datos["fecha"], errors="coerce"
        )

        # Validar niveles de estrés
        datos["nivel_estres"] = pd.to_numeric(
            datos["nivel_estres"], errors="coerce"
        )

        datos = datos.dropna(
            subset=["fecha", "nivel_estres"]
        )

        # Conservar únicamente niveles enteros entre 1 y 10
        datos = datos[
            (datos["nivel_estres"] >= 1)
            & (datos["nivel_estres"] <= 10)
            & (datos["nivel_estres"] % 1 == 0)
        ]

        # Convertir el nivel a entero
        datos["nivel_estres"] = datos["nivel_estres"].astype(int)

        # Convertir notas vacías en cadenas
        datos["nota"] = datos["nota"].fillna("").astype(str)

        return datos.reset_index(drop=True)

    except (OSError, ValueError, pd.errors.ParserError, UnicodeError):
        return datos_vacios


def guardar_registro(fecha, nivel, nota=""):
    """
    Guarda un nuevo registro de estrés en el archivo CSV.

    Recibe:
        fecha: fecha del registro.
        nivel: nivel de estrés del 1 al 10.
        nota: comentario opcional.

    Devuelve:
        True si el registro se guarda correctamente.
        False si ocurre un error.
    """

    if not validar_registro(fecha, nivel, nota):
        return False

    try:
        # Crear la carpeta data si no existe
        RUTA_ARCHIVO.parent.mkdir(parents=True, exist_ok=True)

        # Cargar registros anteriores
        datos = cargar_registros()

        # Preparar el nuevo registro
        nuevo_registro = pd.DataFrame([{
            "fecha": pd.Timestamp(fecha).strftime("%Y-%m-%d"),
            "nivel_estres": int(float(nivel)),
            "nota": nota.strip()
        }])

        # Agregar el nuevo registro
        datos = pd.concat(
            [datos, nuevo_registro],
            ignore_index=True
        )

        # Guardar todos los registros
        datos.to_csv(
            RUTA_ARCHIVO,
            index=False,
            encoding="utf-8"
        )

        return True

    except (OSError, ValueError, TypeError):
        return False

