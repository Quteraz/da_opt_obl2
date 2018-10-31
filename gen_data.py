import numpy as np
import csv
import os
import find_opt_solution as op

os.makedirs('datasets', exist_ok=True)
print('\nGenerating data')
data_100 = op.gen_set(100)
data_1000 = op.gen_set(1000)
print('Done\n-------------------------------------------------------------------------------------')

print('\nWriting to file')


with open('datasets/data_100', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(data_100)

with open('datasets/data_1000', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(data_1000)

# with open('datasets/data_5000', 'w') as csvfile:
# 	writer = csv.writer(csvfile)
# 	writer.writerows(data_5000)
# with open('datasets/data_10000', 'w') as csvfile:
# 	writer = csv.writer(csvfile)
# 	writer.writerows(data_10000)
print('Done\n-------------------------------------------------------------------------------------\n')