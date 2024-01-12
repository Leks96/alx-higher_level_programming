#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
	'''prints a dictionary by ordered keys.'''
	for k in sorted(a_dictionary.keys()):
		value = a_dictionary[k]
		print('{} : {}'.format(k, value))
