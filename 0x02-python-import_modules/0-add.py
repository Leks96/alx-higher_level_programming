#!/usr/bin/env python3
# 0-add.py
# Saidi Sodiq <saidisodiq92gmail.com>

# condition before import

if __name__ == "__main__":
	"""print the sum of 1 and 2"""
	from add_0 import add
# assign value
	a, b = 1, 2
# print result
	print("{} + {} = {}".format(a, b, add(a,b)))
