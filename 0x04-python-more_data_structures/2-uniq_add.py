#!/usr/bin/python3
def uniq_add(my_list=[]):
	'''adds all unique integers in a
	   	list (only once for each integer).
	'''
	unique_elements = sorted(set(my_list))

	result = 0
	for i in unique_elements:
		result += i
	
	return result
