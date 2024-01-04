#!/usr/bin/python3
# Saidi Sodiq

if __name__ == "__main__":
	"""prints the number of and the list of its arguments."""
	import sys
	num_args = len(sys.argv) - 1

	print("{} argument{}".format(num_args, "s" if num_args != 1 else ""), end="")
	print("{}{}".format(":" if num_args > 0 else ".", "\n" if num_args > 0 else ""))

	for i in range(1, num_args + 1):
		print("{}: {}".format(i, sys.argv[i]))
