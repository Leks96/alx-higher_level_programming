#!/usr/bin/python3
"""defines a function that prints a string
"""
def say_my_name(first_name, last_name=""):
	"""
	prints first name and last name
	"""

	if not isinstance(first_name, str):
		raise TypeError("first_name must be a string")
	
	if not isinstance(last_name, str):
		raise TypeError("last_name must be a string")

	if first_name == "":
		raise ValueError("first_name cannot be an empty string")

	print("My name is {} {}".format(first_name, last_name))
