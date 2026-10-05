from fibonacci_kata.core import fibonacci
import pytest


def test_fibonacci_10():
    assert fibonacci(10) == 55


def test_fibonacci_negative_raises():
    with pytest.raises(ValueError):
        fibonacci(-1)
