#!/usr/bin/python3
# 1-calculation.py
# Saidi Sodiq <saidisodiq96@gmail.com>

if __name__ == "__main__":
	"""prints the result of add, sub, mul and div of 10 and 5."""
	from calculator_1 import add, sub, mul, div

# assign values to variables
	a = 10
	b = 5

# perform the calculations
	operations = {
		'add': ('+', add),
		'sub': ('-', sub),
		'mul': ('*', mul),
		'div': ('/', div)
	}

	for operation_name, (symbol, operation_func) in operations.items():
		result = operation_func(a, b)
		print("{:d} {} {:d} = {}".format(a, symbol, b, result))
