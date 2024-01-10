#!/usr/bin/python3
def multiple_returns(sentence):
	"""returns a tuple with the length of
		a string and its first character.
	"""
	if sentence:
		a = len(sentence)
		b = sentence[0]
		return a, b
	else:
	 	return None, None
