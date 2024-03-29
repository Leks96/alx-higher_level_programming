#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
	"""prints a matrix of integers."""
	for row in matrix:
		if row:
			for num in row[:-1]:
				print("{:d}".format(num), end=" ")
			print("{:d}".format(row[-1]))
		else:
			print()
