"""Tests para la función mul(a, b) -> float."""

import pytest

from src.calculator import mul


# --- EJEMPLO (no borrar) ---
def test_mul_positivos():
    """Ejemplo: 3 * 4 debe dar 12."""
    assert mul(3, 4) == 12


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Multiplicar por cero
#   - Multiplicar dos números negativos (resultado positivo)
#   - Multiplicar un positivo y un negativo (resultado negativo)
#   - Multiplicar por 1 (elemento neutro)
#   - Multiplicar dos decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.

@pytest.mark.parametrize("a, b, expected", [
    (10, 0, 0),        
    (-3, -4, 12),      
    (-5, 2, -10),      
    (7, 1, 7),         
    (2.5, 2.0, 5.0)    
])
def test_mul_casos_multiples(a, b, expected):
    """Prueba múltiples casos de multiplicación usando parametrización."""
    assert mul(a, b) == expected