"""Tests para la función add(a, b) -> float."""

import pytest

from src.calculator import add


# --- EJEMPLO (no borrar) ---
def test_add_suma_positivos():
    """Ejemplo: 1 + 2 debe dar 3."""
    assert add(1, 2) == 3


import pytest
from src.calculator import add

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (-5, -5, -10),
    (0, 0, 0),
    (2.5, 2.5, 5.0)
])
def test_add(a, b, expected):
    assert add(a, b) == expected
