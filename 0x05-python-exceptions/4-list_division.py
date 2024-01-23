#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
	"""divides element by element 2 lists."""
	result_list = []
	try:
		for i in range(list_length):
			try:
				el_1 = my_list_1[i]
				el_2 = my_list_2[i]
				result = el_1 / el_2
				result_list.append(result)
			except ZeroDivisionError:
				print("division by 0")
				result_list.append(0)
			except (TypeError, ValueError):
				print("Wrong type")
				result_list.append(0)
			except IndexError:
				print("out of range")
				result_list.append(0)
	finally:
		return result_list
