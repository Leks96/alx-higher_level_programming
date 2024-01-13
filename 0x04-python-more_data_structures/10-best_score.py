#!/usr/bin/python3
def best_score(a_dictionary):
	'''returns a key with the biggest integer value.'''
	if a_dictionary is None or not isinstance(a_dictionary, dict):
		return None

	highest_value = float('-inf')
	
	best_key = None

	for key, value in a_dictionary.items():
		if isinstance(value, list):
			max_val_in_list = max(value)
			if max_val_in_list > highest_value:
				highest_value = max_val_in_list
				best_key = key

		elif isinstance(value, int) and value > highest_value:
			highest_value = value
			best_key = key

	return best_key
