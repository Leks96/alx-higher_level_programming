#!/usr/bin/python3
import dis, marshal

def get_names(file_path):
	"""prints all the names defined by the compiled module hidden_4.pyc"""
	with open(file_path, 'rb') as file:
		code_object = marshal.load(file)
		return [name for name in code_object.co_names if not name.startswith('__')]


if __name__ == "__main__":
	file_path = 'hidden_4.pyc'
	names = get_names(file_path)


	for name in sorted(names):
		print(name)
