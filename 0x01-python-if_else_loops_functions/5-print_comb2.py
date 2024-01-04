#!/usr/bin/python3
# 5-print_comb2.py
# Saidi Sodiq <saidisodiq96@gmail.com>

"""prints numbers from 0 to 99."""
for s in range(100):
	print(f"{s:02d}", end=", " if s < 99 else "\n")
