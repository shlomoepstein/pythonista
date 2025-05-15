import sys
import json


def peek(file):
	position = file.tell()
	line = file.readline()
	file.seek(position)
	return line


with open(sys.argv[1]) as file:
	print(peek(file))
	print(peek(file))

