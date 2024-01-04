#!/usr/bin/python3
# 3-print_alphabt.py
# Saidi Sodiq <saidisodiq96@gmail.com>

"""prints the ASCII alphabet, in lowercase, not followed by a new line."""
for alphabets in range(97, 123):
	_alpha = chr(alphabets)
	if _alpha not in 'qe':
		print(_alpha, end='')
