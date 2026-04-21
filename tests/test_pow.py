"""Tests para la función pow_(a, b) -> float."""

import pytest

from src.calculator import pow_


# --- EJEMPLO (no borrar) ---
def test_pow_base_positiva():
    """Ejemplo: 2 ** 3 debe dar 8."""
    assert pow_(2, 3) == 8


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Cualquier número elevado a 0 (resultado: 1)
#   - Número elevado a 1 (resultado: el mismo número)
#   - Base negativa con exponente par (resultado positivo)
#   - Exponente decimal, ej: 9 ** 0.5 (raíz cuadrada)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.

@pytest.mark.parametrize("a, b, expected", [
    (5, 0, 1),         # Cualquier número elevado a 0 (resultado: 1)
    (7, 1, 7),         # Número elevado a 1 (resultado: el mismo número)
    (-2, 4, 16),       # Base negativa con exponente par (resultado positivo)
    (9, 0.5, 3.0)      # Exponente decimal (raíz cuadrada)
])
def test_pow_casos_multiples(a, b, expected):
    """Prueba múltiples casos de potencia usando parametrización."""
    assert pow_(a, b) == expected

     #ACLARACION En este test me ayude con la IA y en el de sqrt tambien