"""Tests para la función mean(values) -> float."""

import pytest

from src.calculator import mean


# --- EJEMPLO (no borrar) ---
def test_mean_lista_simple():
    """Ejemplo: el promedio de [2, 4, 6] debe dar 4.0."""
    assert mean([2, 4, 6]) == 4.0


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Lista con un solo elemento (el resultado debe ser ese mismo elemento)
#   - Lista con números negativos
#   - Lista con números decimales (float)
#   - Lista vacía → debe lanzar ValueError
#
# Pista: para testear excepciones usá pytest.raises:
#
# def test_mean_lista_vacia():
#     with pytest.raises(ValueError):
#         mean([])

@pytest.mark.parametrize("values, expected", [
    ([10], 10.0),                  # Lista con un solo elemento
    ([-2, -4, -6], -4.0),          # Lista con números negativos
    ([1.5, 2.5, 5.0], 3.0)         # Lista con números decimales (float)
])
def test_mean_casos_multiples(values, expected):
    """Prueba múltiples casos de promedios usando parametrización."""
    assert mean(values) == expected

def test_mean_lista_vacia():
    """Verifica que una lista vacía lance ValueError."""
    with pytest.raises(ValueError):
        mean([])