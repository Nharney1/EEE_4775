import os
import random


files = 100

for file in range(files):
	file_name = "{}-{:03d}{}".format('input', file, '.txt')
	f = open(file_name, 'w')
	numTasks = random.randint(2,6)
	for Tid in range(numTasks):
		computationTime = random.randint(1, 3)
		relativeDeadline = random.randint(4*computationTime + 1, 5*computationTime + 1)
		period = random.randint(2*relativeDeadline, 3*relativeDeadline)
		f.write(str(Tid) + ' ' + str(computationTime) + ' ' + str(period) + ' ' + str(relativeDeadline) + '\n')
	f.close()
