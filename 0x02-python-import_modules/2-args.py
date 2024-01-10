#!/usr/bin/python3
# 2-args.py
# Saidi Sodiq <saidisodiq96@gmail.com>

if __name__ == "__main__":
	"""prints the number of and the list of its arguments."""
	import sys
	ofArg = sys.argv
	noOfArg = len(ofArg) - 1

	case_dict = {
		0: "0 arguments.",
		1: "1 argument:",
		2: "{:d} arguments:".format(noOfArg)
	}

	case_key = min(2, noOfArg)

	print(case_dict[case_key])

	if noOfArg > 0:

		for i in range(1, noOfArg + 1):
			print("{:d}: {}".format(i, ofArg[i]))
