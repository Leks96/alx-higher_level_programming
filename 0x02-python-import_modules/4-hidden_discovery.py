#!/usr/bin/python3
import hidden_4
"""prints all the names defined by the compiled module hidden_4.pyc"""

if __name__ == "__main__":
	def_names = dir(hidden_4)

	for name in sorted(def_names):
		if not name.startswith("__"):
			print(name)
