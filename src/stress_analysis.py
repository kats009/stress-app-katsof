"""Funciones para analizar registros de estrés académico."""

import pandas as pd


def _niveles_validos(datos):
    """Devuelve una serie nueva con niveles numéricos válidos de 1 a 10."""
    if datos is None:
        return pd.Series(dtype="float64")
    if isinstance(datos, pd.DataFrame):
        if "nivel_estres" not in datos.columns:
            return pd.Series(dtype="float64")
        datos = datos["nivel_estres"]
    try:
        niveles = pd.to_numeric(pd.Series(datos), errors="coerce").dropna()
    except (TypeError, ValueError):
        return pd.Series(dtype="float64")
    return niveles[niveles.between(1, 10)]


def calcular_promedio(datos):
    """Calcula el promedio de los niveles válidos o devuelve None."""
    niveles = _niveles_validos(datos)
    return None if niveles.empty else float(niveles.mean())


def calcular_mediana(datos):
    """Calcula la mediana de los niveles válidos o devuelve None."""
    niveles = _niveles_validos(datos)
    return None if niveles.empty else float(niveles.median())


def clasificar_estres(nivel):
    """Clasifica un nivel como bajo, moderado o alto."""
    try:
        valor = float(nivel)
    except (TypeError, ValueError):
        return None
    if not 1 <= valor <= 10:
        return None
    if valor <= 3:
        return "bajo"
    if valor <= 6:
        return "moderado"
    return "alto"


def analizar_tendencia(datos):
    """Compara el primer y último nivel y describe su tendencia."""
    niveles = _niveles_validos(datos)
    if len(niveles) < 2:
        return None
    if niveles.iloc[-1] > niveles.iloc[0]:
        return "aumenta"
    if niveles.iloc[-1] < niveles.iloc[0]:
        return "disminuye"
    return "estable"
