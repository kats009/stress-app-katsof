# Genera recomendaciones según los resultados.
"""
Módulo de recomendaciones para Stress App.

Genera consejos de organización, bienestar y relajación
según el nivel de estrés académico del estudiante.
"""


def generar_recomendaciones(nivel):
    """
    Genera recomendaciones según el nivel de estrés.

    Recibe:
        nivel: número entero entre 1 y 10.

    Devuelve:
        Una lista de recomendaciones en español.
        Una lista vacía si el nivel es inválido.
    """

    # Validar que el nivel sea numérico
    if isinstance(nivel, bool):
        return []

    try:
        nivel = float(nivel)

    except (ValueError, TypeError):
        return []

    # Validar rango y número entero
    if not nivel.is_integer() or nivel < 1 or nivel > 10:
        return []

    nivel = int(nivel)

    # Estrés bajo
    if 1 <= nivel <= 3:

        recomendaciones = [
            "Mantén una rutina de sueño constante.",
            "Continúa organizando tus actividades escolares.",
            "Realiza actividad física que disfrutes.",
            "Dedica tiempo a tus pasatiempos.",
            "Mantén descansos durante tus sesiones de estudio."
        ]

    # Estrés moderado
    elif 4 <= nivel <= 6:

        recomendaciones = [
            "Organiza tus tareas según su fecha de entrega.",
            "Divide los proyectos grandes en actividades pequeñas.",
            "Realiza pausas entre sesiones de estudio.",
            "Prueba ejercicios suaves de respiración.",
            "Evita dejar todas tus actividades para el último momento."
        ]

    # Estrés alto
    else:

        recomendaciones = [
            "Haz una pausa y dedica unos minutos a descansar.",
            "Divide tus pendientes en pasos pequeños y manejables.",
            "Prueba un ejercicio de respiración suave.",
            "Habla con una persona de confianza sobre cómo te sientes.",
            "Si el estrés continúa o afecta tu vida diaria, busca orientación de un profesional o del personal de orientación escolar."
        ]

    return recomendaciones
