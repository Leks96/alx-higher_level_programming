#!/usr/bin/python3
class Square:
	"""
	A class representing a square.

	Attributes:
		 __size (int): The size of the square.

	Methods:
		 __init__(self, size=0): Initializes a new instance of the Square class with an optional size.
	"""

	def __init__(self, size=0):
		"""
		Initializes a new instance of the Square class.

		Args:
			size (int, optional): The size of the square. Default is 0.

		Raises:
			TypeError: If size is not an integer.
			ValueError: If size is less than 0.
		"""
		if not isinstance(size, int):
			raise TypeError("size must be an integer")

		if size < 0:
			raise ValueError("size must be >= 0")

		self.__size = size
