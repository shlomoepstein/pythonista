import json

with open('time-clock.jsonl') as infile:
	for line in infile:
		entry = json.loads(line)
		print('type: ' + entry['type'].split('-')[0] +
					' ' + entry['type'].split('-')[1])
		print('date: ' + entry['date-time'].split('T')[0])
		print('time: ' + entry['date-time'].split('T')[1] + '\n')

