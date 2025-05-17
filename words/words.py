with open('words_alpha.txt') as word_list:
	frequency = {}
	acq = []
	
	for word in word_list:
		if len(word.strip()) < 3:
			continue
			
		if word[0:3] not in frequency:
			frequency[word[0:3]] = 1
		else:
			frequency[word[0:3]] += 1
			
		if word[0:3] == 'acq':
			acq.append(word.strip())

	frequency2 = {}
	high_low = {}
	
	for key in frequency:
		if frequency[key] not in frequency2:
			frequency2[frequency[key]] = 1
		else:
			frequency2[frequency[key]] += 1
			
		if (frequency[key] <= 50
				or frequency[key] > 2000):
			if frequency[key] not in high_low:
				high_low[frequency[key]] = [key]
			else:
				high_low[frequency[key]].append(key)
				
#			print(f'{key}: {frequency[key]}')

	for key in sorted(frequency2):
		print(f'{key}: {frequency2[key]}')

	for key in sorted(high_low):
		print(f'{key}: {high_low[key]}')

	print(f'\nacq: {frequency["acq"]}\n')
	
	print(acq)

