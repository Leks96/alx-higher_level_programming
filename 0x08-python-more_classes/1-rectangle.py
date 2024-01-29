#!/usr/bin/python3
"""
Module with a functionless Rectangle
"""
class Rectangle:
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
