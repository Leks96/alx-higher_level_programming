#!/usr/bin/python3
# 2-args.py
# Saidi Sodiq <saidisodiq96@gmail.com>

if __name__ == "__main__":
	"""prints the number of and the list of its arguments."""
	import sys
	commandLineArguments = sys.argv
	numberOfArguments = len(commandLineArguments) - 1

	if numberOfArguments < 1
		print("0 arguments.")
	elif numberOfArguments == 1
		print("1 argumet:")
	else:
		print(f"{numberOfArguments} arguments:")

	if numberOfArguments > 0
		for argumentIndex in range(1, numberOfArguments + 1)
			print(f"{argumentIndex}: {commandLineArguments[argumentIndex]}")
