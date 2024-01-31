#!/usr/bin/python3
"""
class with no class or object attribute
"""
class LockedClass:
	"""
	prevents users from dynamically creating
	new instances attribute
	"""
	__slots__ = ('first_name',)

	def __setattr__(self, name, value):
		if not hasattr(self, 'first_name') and name != 'first_name':
			raise AttributeError(f"'{self.__class__.__name__}' object has no attribute 'last_name'")
		object.__setattr__(self, name, value)
