import pytest
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
