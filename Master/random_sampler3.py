import random

def random_sampler(filename, k):
	sample = []
	with open(filename, 'r') as f:
		f.seek(0, 2)
		filesize = f.tell()

		random_set = sorted(random.sample(range(filesize), k))

		for i in range(k):
			f.seek(random_set[i])
			# Skip current line (because we might be in the middle of a line) 
			f.readline()
			# Append the next line to the sample set 
			sample.append(f.readline().rstrip())

	return sample
