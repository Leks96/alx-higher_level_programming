#!/usr/bin/python3
def safe_print_integer(value):
	"""prints an integer with "{:d}".format()."""
	try:
		print("{:d}".format(value))
		print()
		
		return True

	except: (ValueError, TypeError)

		return false
