import numpy as np
import csv
import os
import find_opt_solution as op

os.makedirs('datasets', exist_ok=True)
print('\nGenerating data')
data_50 = op.gen_set(50)
data_100 = op.gen_set(100)
data_1000 = op.gen_set(1000)
data_5000 = op.gen_set(5000)
print('Done\n-------------------------------------------------------------------------------------')

print('\nWriting to file')


with open('datasets/data_50', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(data_50)

with open('datasets/data_100', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(data_100)

with open('datasets/data_1000', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(data_1000)
with open('datasets/data_5000', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(data_5000)
print('Done\n-------------------------------------------------------------------------------------\n')