import pytest
import math

from ..source import shapes as shapes
# from ..source import service
# import service as service

import unittest.mock as mock


@mock.patch(".service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
	mock_get_user_from_db.return_value = "Mocked Alice"
	user_name = service.get_user_from_db(1)

	assert user_name == "Mocked Alice"


@pytest.fixture
def my_rectangle():
	return shapes.Rectangle(10, 20)

@pytest.fixture
def my_square():
	return shapes.Square(20)


class TestShape:

	def setup_method(self, method):
		self.circle = shapes.Circle(10)

	def teardown_method(self, method):
		print(f'Teardown up {method} \n')
		del self.circle

	def test_one(self):
		assert self.circle.area() == math.pi * math.pow(10, 2)

	def test_two(self):
		assert self.circle.perimeter() == 2 * math.pi * 10

	def test_rectange_area(self, my_rectangle):
		assert my_rectangle.area() == 10 * 20

	def test_rectange_perimeter(self, my_rectangle):
		assert my_rectangle.perimeter() == 2 * (10 + 20)

	def test_square_area(self, my_square):
		print(my_square.area())
		assert my_square.area() == 400

	def test_square_perimeter(self, my_square):
		print(my_square.perimeter())
		assert my_square.perimeter() == 80


def test_area(my_rectangle):
	assert my_rectangle.area() == 10 * 20


def test_perimeter(my_rectangle):
	assert my_rectangle.perimeter() == 2 * (10 + 20)


@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (4, 16), (9, 81)])
def test_multiple_square_area(side_length, expected_area):
	print(side_length)
	assert shapes.Square(side_length).area() == expected_area


@pytest.mark.parametrize("side_length, expected_perimeter", [(3, 12), (4, 16), (5, 20)])
def test_multiple_perimeters(side_length, expected_perimeter):
	print(side_length)
	assert shapes.Square(side_length).perimeter() == expected_perimeter
