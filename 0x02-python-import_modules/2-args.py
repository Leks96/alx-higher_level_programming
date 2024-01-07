#!/usr/bin/python3
# 2-args.py
# Saidi Sodiq

if __name__ == "__main__":
	"""prints the number of and the list of its arguments."""
	import sys
	num_args = len(sys.argv) - 1

	case_dict = {
		0: "0 arguments.",
		1: "1 argument:",
		2: "{} arguments:".format(num_args)
	}

	case_key = min(2, num_args)

	print(case_dict[case_key])

	for i in range(1, num_args + 1):
		print("{}: {}".format(i, sys.argv[i]))
