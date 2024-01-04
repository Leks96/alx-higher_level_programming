#!/usr/bin/python3
# 1-calculation.py
# Saidi Sodiq <saidisodiq96@gmail.com>

if __name__ == "__main__":
	"""does some Maths, and prints the result"""
	from calculator_1 import add, sub, mul, div

# assign values to variables
	a = 10
	b = 5
# perform calculations and print results
	res_add = add(a, b)
	res_sub = sub(a, b)
	res_mul = mul(a, b)
	res_div = div(a, b)
#display results
	print("{} + {} = {}".format(a, b, res_add))
	print("{} - {} = {}".format(a, b, res_sub))
	print("{} * {} = {}".format(a, b, res_mul))
	print("{} / {} = {}".format(a, b, res_div))
