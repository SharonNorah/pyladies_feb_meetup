from calc import add, multiply
import pytest

@pytest.mark.suite1
def test_add():
	assert add(2, 3) == 5

@pytest.mark.suite2
def test_multiply():
	assert multiply(2, 3) == 6