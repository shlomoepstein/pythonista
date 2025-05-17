import json

with open('times.txt') as infile:
	with open('tempfile', 'w') as outfile:
		for line in infile:
			outfile.write(
				json.dumps(
					json.loads(line),
					separators=(',', ':')
				) + '\n'
			)

