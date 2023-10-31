import pytest
import time

from ..source import operation


def test_addition():
	result = operation.add_number(2, 7)
	assert result == 9


def test_division():

	with pytest.raises(ValueError):
		result = operation.divide_number(25, 0)
	# assert result == 0


def test_add_strings():
	result = operation.add_number("I like ", "Pizza.")
	assert result == "I like Pizza."


@pytest.mark.slow
def test_very_slow():
	time.sleep(2)
	result = operation.add_number(10, 5)
	assert result == 15


@pytest.mark.skip(reason="This feature is currently broken.")
def test_add_skip():
	assert operation.add_number(1, 2) == 1


@pytest.mark.xfail(reason='We know we cannot divide by zero')
def test_divide_zero_broken():
	operation.divide_number(5, 0)
