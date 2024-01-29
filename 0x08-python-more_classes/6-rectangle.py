#!/usr/bin/python3
"""
Module with a functionless Rectangle
"""
class Rectangle:
	number_of_instances = 0
	"""
	defines a rectangle.
	"""

	def __init__(self, width=0, height=0):
		"""
		Checks params and init some vals

		Args:
			width(int, optional): Rectangle's width.
			height(int, optional): Rectangle's height.
		"""
		self._rec_width = width
		self._rec_height = height

		self.width = width
		self.height = height

		Rectangle.number_of_instances += 1

	@property
	def width(self):
		"""
		Returns the width of the rectangle
		"""
		return self._rec_width

	@width.setter
	def width(self, value):

		"""
		Checks for param and set it

		Args:
			value(int): The width of the rectangle
	
		Raises:
			TypeError: if `value` type is not `int`.
			ValueError: if `value` is < 0.
		"""
		if not isinstance(value, int):
			raise TypeError("width must be an integer")
	
		if value < 0:
			raise ValueError("width must be >= 0")

		self._rec_width = value

	@property
	def height(self):
		"""
		Returns the height of the rectangle
		"""

		return self._rec_height

	@height.setter
	def height(self, value):

		"""
		Checks for param and set it

		Args:
			value(int): The height of the rectangle.

		Raises:
			TypeError: if `value` type is not `int`.
			ValueError: if `value` is < 0.
		"""
		
		if not isinstance(value, int):
			raise TypeError("width must be an integer")

		if value < 0:
			raise ValueError("width must be >= 0")

		self._rec_height = value

	def area(self):
		"""
		Returns the area of the rectangle
		"""
		return self._rec_width * self._rec_height

	def perimeter(self):
		if self._rec_width == 0 or self._rec_height == 0:
			return 0
		return 2 * (self._rec_width + self._rec_height)

	def __str__(self):
		"""
		Returns new string object of the rectangle
		"""
		if self._rec_width == 0 or self._rec_height == 0:
			return ""
		else:
			return "\n".join(["#" * self._rec_width] * self._rec_height)

	def __repr__(self):
		"""
		Return the string rep of rectangle
		"""
		return f"Rectangle({self._rec_width}, {self._rec_height})"

	def __del__(self):
		"""
		Prints a message when an instance of rectangle is deleted
		"""
		print("Bye rectangle...")
		Rectangle.number_of_instances -= 1