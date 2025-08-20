import pytest

@pytest.mark.smoke
def add1(a, b):
    return a + b

def test_add1():
    assert add1(10, 5) == 15