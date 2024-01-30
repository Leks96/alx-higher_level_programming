#!/usr/bin/python3
"""
defines a function that divides all elements of a matrix
"""
def matrix_divided(matrix, div):
	"""
	divides all elements of a matrix
	"""
	new_matrix = []
	
	for row in matrix:
		if not isinstance(row, list) or not all(isinstance(num, (int, float)) for num in row):
			raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

	if any(len(row) != len(matrix[0]) for row in matrix[1:]):
		raise TypeError("Each row of the matrix must have the same size")

	if not isinstance(div, (int, float)):
		raise TypeError("div must be a number")

	if div == 0:
		raise ZeroDivisionError("division by zero")

	for row in matrix:
		new_row = [round(num / div, 2) for num in row]
		new_matrix.append(new_row)

	return new_matrix
			
