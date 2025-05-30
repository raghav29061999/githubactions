import pytest

from src.math_operations import add, divide, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 5) == 4
    

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 3) == -3
    

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    

    # Test divide by zero error
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)