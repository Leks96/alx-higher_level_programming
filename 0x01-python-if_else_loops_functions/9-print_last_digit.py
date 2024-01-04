#!/usr/bin/python3
# 9-print_last_digit.py
# Saidi Sodiq <saidisodiq96@gmail.com>

def print_last_digit(number):
	"""prints the last digit of a number."""
	last_digit = number % 10
	print(last_digit, end='')
	return last_digit
