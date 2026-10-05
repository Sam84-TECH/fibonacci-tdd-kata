import pytest

from fibonacci_kata.core import fibonacci


def test_fibonacci_10():
    assert fibonacci(10) == 55


def test_fibonacci_negative_raises():
    with pytest.raises(ValueError):
        fibonacci(-1)
