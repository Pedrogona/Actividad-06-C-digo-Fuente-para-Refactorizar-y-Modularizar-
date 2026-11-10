"""
Módulo de procesamiento y análisis estadístico básico.
Aplica principios de separación de responsabilidades y PEP 8.
"""

from typing import Dict, List, Optional


def clean_numerical_data(raw_data: List[Optional[float]]) -> List[float]:
    """Filtra los valores nulos y negativos (considerados códigos de error)

    y convierte los elementos restantes a tipo float.

    Args:
        raw_data (List[Optional[float]]): Lista de datos de entrada crudos.

    Returns:
        List[float]: Lista de datos numéricos limpios y válidos.
    """
    valid_data = []
    for value in raw_data:
        if value is not None and value >= 0:
            valid_data.append(float(value))
    return valid_data


def calculate_statistics(values: List[float]) -> Optional[Dict[str, float]]:
    """Calcula la media, la varianza poblacional y la desviación estándar

    a partir de una lista de valores numéricos limpios.

    Args:
        values (List[float]): Lista de valores numéricos limpios.

    Returns:
        Optional[Dict[str, float]]: Diccionario con métricas estadísticas o
        None si la lista está vacía.
    """
    count = len(values)
    if count == 0:
        return None

    mean = sum(values) / count
    variance = sum((x - mean) ** 2 for x in values) / count
    standard_deviation = variance**0.5

    return {
        "mean": mean,
        "variance": variance,
        "std_deviation": standard_deviation,
    }


def analyze_dataset(raw_data: List[Optional[float]]) -> Optional[Dict[str, float]]:
    """Función orquestadora que coordina la limpieza de datos y

    el posterior cálculo estadístico.
    """
    clean_values = clean_numerical_data(raw_data)
    return calculate_statistics(clean_values)


if __name__ == "__main__":
    datos_xyz = [12.5, -999, 15.0, None, 18.2, 20.1, -5, 14.8]
    resultado = analyze_dataset(datos_xyz)
    print("Resultado del análisis:", resultado)
