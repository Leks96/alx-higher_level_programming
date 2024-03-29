#!/usr/bin/python3
def safe_print_division(a, b):
	"""divides 2 integers and prints the result."""
	result = None

	try:
		result = a / b
	except ZeroDivisionError:
		print("Error: Division by zero")
	except Exception as e:
		print(f"Error: {e}")
	finally:
		print("Inside result: {}".format(result))
		return result
