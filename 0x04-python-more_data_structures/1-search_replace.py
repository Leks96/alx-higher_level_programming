#!usr/bin/python3
def search_replace(my_list, search, replace):
	"""replaces all occurrences of an element by another in a new list."""
	new_list = []
	for i in my_list:
		new_list.append(replace if i == search else i)
	return new_list
