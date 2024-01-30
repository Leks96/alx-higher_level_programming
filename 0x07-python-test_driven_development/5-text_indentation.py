#!/usr/bin/python3
"""
define a fuction that prints a text
followed by a new line
"""
def text_indentation(text):
	"""
	prints a text with 2 new lines after each of these characters: ., ? and :
	"""
	formatted_text = ""
	
	if not isinstance(text, str):
		raise TypeError("text must be a string")

	for char in text:
		formatted_text += char

		if char in [',', '.', '?', ':']:
			formatted_text += '\n\n'

	print(formatted_text.strip())
