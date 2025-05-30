# test_math_ops.py
import math

import pytest

from src.new_ops import log_func, pow, trig_funcs


def test_pow():
    assert pow(2, 3) == 8
    assert pow(5, 0) == 1
    assert pow(9, 0.5) == 3

def test_log_func():
    assert log_func(8, 2) == pytest.approx(3)
    assert log_func(100, 10) == pytest.approx(2)
    assert log_func(math.e, math.e) == pytest.approx(1)

    with pytest.raises(ValueError):
        log_func(-1, 10)  # log of negative number is invalid

    with pytest.raises(ValueError):
        log_func(10, -2)  # negative base is invalid

def test_trig_funcs():
    angle = math.pi / 4  # 45 degrees in radians
    sin_val, cos_val= trig_funcs(angle)
    assert sin_val == pytest.approx(math.sqrt(2)/2)
    assert cos_val == pytest.approx(math.sqrt(2)/2)
    # assert tan_val == pytest.approx(1)

    angle = 0
    sin_val, cos_val= trig_funcs(angle)
    assert sin_val == pytest.approx(0)
    assert cos_val == pytest.approx(1)
    # assert tan_val == pytest.approx(0)
