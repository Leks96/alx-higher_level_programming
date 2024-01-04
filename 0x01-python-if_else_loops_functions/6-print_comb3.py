#!/usr/bin/python3
# 6-print_comb3.py
# Saidi Sodiq <saidisodiq96@gmail.com>

"""prints all possible different combinations of two digits."""
for s in range(10):
	for a in range(s+1, 10):
		print(f"{s}{a}", end=", " if a < 9 else "\n" if s == 8 and a == 9 else ', ')
