#!/usr/bin/python3
class Square:
	"""
	A class representing a square.

	Attributes:
		 __size (int): The size of the square.

	Methods:
		 __init__(self, size=0): Initializes a new instance
			of the Square class with an optional size.
		area(self): Returns the current square area
		size(self): Getter method to retrieve size.
		size(self, value): Setter method to set size attr.
	"""

	def __init__(self, size=0):
		"""
		Initializes a new instance of the Square class.

		Args:
			size (int, optional): The size of the square.
				Default is 0.

		Raises:
			TypeError: If size is not an integer.
			ValueError: If size is less than 0.
		"""
		if not isinstance(size, int):
			raise TypeError("size must be an integer")

		if size < 0:
			raise ValueError("size must be >= 0")

		self.__size = size

	@property
	def size(self):
		"""
		Getter method retrieve size attr.

		Return:
			int: size of the square.
		"""
		return self.__size

	@size.setter
	def size(self, value):
		"""
		Setter method to set size attr.

		Args:
			value (int): new size value.

		Raises:
			TypeError: If size is not an integer
			ValueError: If size is less than 0.
		"""
		if not isinstance(size, int):
			raise TypeError("size must be an integer")

		if value < 0:
			raise ValueError("size must be >= 0")

		self.__size = value

	def area(self):
		"""Returns the current square area

		Returns:
			int: The area of the square.
		"""
		return self.__size ** 2
