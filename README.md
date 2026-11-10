# Módulo de Análisis Estadístico Modular

Pequeño proyecto en Python diseñado bajo los principios de **modularización**, **separación de responsabilidades** y cumplimiento estricto de las normas de estilo **PEP 8**.

##  Estructura del Proyecto

* `estadistica.py`: Contiene la lógica desacoplada (limpieza de datos y cálculos estadísticos).
* `README.md`: Documentación del proyecto.

##  Principios Aplicados

1. **Separación de Responsabilidades (SoC):** 
   - `clean_numerical_data`: Responsable únicamente de sanitizar el conjunto de datos (eliminación de nulos y valores negativos de control).
   - `calculate_statistics`: Responsable exclusivamente de la computación matemática.
   - `analyze_dataset`: Función orquestadora que une ambas capas.
2. **Legibilidad y Tipado:** Uso completo de `typing` y nomenclaturas claras en `snake_case`.

## Uso

Ejecuta el script directamente desde tu terminal:

```bash
python estadistica.py
