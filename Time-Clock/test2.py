import sys

for i, arg in enumerate(sys.argv):
	print(f'arg {i}: {arg}')

with open(sys.argv[2]) as infile:
	print(infile.read())

