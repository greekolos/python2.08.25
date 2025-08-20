import pytest


def add1(a, b):
    return a + b
@pytest.mark.smoke
def test_add1():
    assert add1(10, 5) == 15