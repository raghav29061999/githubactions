import pytest
from src.math_operations import add, subtract, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 5) == 4
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 3) == -3
    assert subtract(3, 3) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(1, 4) == 0.25

    # Test divide by zero error
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)