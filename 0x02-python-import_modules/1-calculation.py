#!/usr/bin/python3
# 1-calculation.py
# Saidi Sodiq <saidisodiq96@gmail.com>

if __name__ == "__main__":
	"""prints the result of add, sub, mul and div of 10 and 5"""
	from calculator_1 import add, sub, mul, div

# assign values to variables
	a = 10
	b = 5

#display results
	print("{} + {} = {}".format(a, b, add(a, b)))
	print("{} - {} = {}".format(a, b, sub(a, b)))
	print("{} * {} = {}".format(a, b, mul(a, b)))
	print("{} / {} = {}".format(a, b, div(a, b)))
