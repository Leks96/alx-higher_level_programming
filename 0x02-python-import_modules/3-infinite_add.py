#!/usr/bin/python3
import sys

def addArgs(_args):
	"""prints the result of the addition of all arguments"""
	return sum(int(args) for args in _args)

if __name__ == "__main__":
	_args = sys.argv[1:]
	result = addArgs(_args)
	print(result)
