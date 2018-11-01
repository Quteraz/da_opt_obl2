import find_opt_solution as op
import csv
import sys

print('\nReading files')
with open('datasets/data_100', 'r') as csvfile:
	reader = csv.reader(csvfile)
	data_file = {'test':list(reader)}
# with open('datasets/data_1000', 'r') as csvfile:
# 	reader = csv.reader(csvfile)
# 	data_file['short'] = list(reader)
# with open('datasets/data_5000', 'r') as csvfile:
# 	reader = csv.reader(csvfile)
# 	data_file['medium'] = list(reader)
# with open('datasets/data_10000', 'r') as csvfile:
# 	reader = csv.reader(csvfile)
# 	data_file['large'] = list(reader)
print('Done\n-------------------------------------------------------------------------------------')

print('\nTesting')
print('-------------------------------------------------------------------------------------')

# specify what data is being used
# data_set = str(sys.argv[1])
data_set = 'test'
data = data_file[data_set]

test = op.one_point(data, 3, 4)

print('Random')

# random_length = op.calc_length(random_data, data)
print('Fitness in',data_set,':',test)

print('-------------------------------------------------------------------------------------\n')