#!/usr/bin/python3
# 8-uppercase.py
# Saidi Sodiq <saidisodiq96@gmail.com>

def uppercase(str):
	"""prints a string in uppercase followed by a new line."""
	for char in str:
		if 'a' <= char <= 'z':
			upperCase = chr(ord(char) - ord('a') + ord('A'))
			print(upperCase, end='')
		else:
			print(char, end='')
	print()
