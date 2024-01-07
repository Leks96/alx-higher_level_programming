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
	add_calc = add(a, b)
	sub_calc = sub(a, b)
	mul_calc = mul(a, b)
	div_calc = div(a, b)

#display results
	print("{} + {} = {}".format(a, b, add_calc))
	print("{} - {} = {}".format(a, b, sub_calc))
	print("{} * {} = {}".format(a, b, mul_calc))
	print("{} / {} = {}".format(a, b, div_calc))
