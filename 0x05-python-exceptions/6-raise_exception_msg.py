#!/usr/bin/python
class CustomException(Exception):
	pass

def raise_exception_msg(message=""):
	"""raises a name exception with a message."""
	raise CustomException(message)
