
import math


class Shape:

	def area(self):
		pass

	def perimeter(self):
		pass


class Circle(Shape):

	def __init__(self, radius):
		self.radius = radius

	def area(self):
		return math.pi * math.pow(self.radius, 2)

	def perimeter(self):
		return 2 * math.pi * self.radius


class Rectangle(Shape):

	def __init__(self, length, breadth):
		self.length = length
		self.breadth = breadth

	def area(self):
		return self.length * self.breadth

	def perimeter(self):
		return 2 * (self.length + self.breadth)


class Square(Rectangle):

	def __init__(self, side_length):
		super().__init__(side_length, side_length)

	def area(self):
		return super().area()

	def perimeter(self):
		return super().perimeter()
