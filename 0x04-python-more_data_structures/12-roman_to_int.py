#!/usr/bin/python3
def roman_to_int(roman_string):
	'''converts a Roman numeral to an integer.'''
	roman_dict = {
		'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
		'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
		'C': 100, 'CD': 400, 'D': 500, 'CM': 900,
		'M': 1000
	}

	res = 0
	i = 0

	while i < len(roman_string):
		if i + 1 < len(roman_string) and roman_string[i:i+2] in roman_dict:
			res += roman_dict[roman_string[i:i+2]]
			i += 2
		else:
			res += roman_dict[roman_string[i]]
			i += 1
		
	return res
