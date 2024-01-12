#!/usr/bin/python3
def common_elements(set_1, set_2):
	'''returns a set of common elements in two sets.'''
	a = set(set_1)
	b = set(set_2)

	return (a & b)
