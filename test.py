import find_opt_solution as op
import csv
import sys

print('\nReading files')
with open('datasets/data_50', 'r') as csvfile:
	reader = csv.reader(csvfile)
	data_file = {'test':list(reader)}
with open('datasets/data_100', 'r') as csvfile:
	reader = csv.reader(csvfile)
	data_file['small'] = list(reader)
with open('datasets/data_1000', 'r') as csvfile:
	reader = csv.reader(csvfile)
	data_file['medium'] = list(reader)
# with open('datasets/data_5000', 'r') as csvfile:
# 	reader = csv.reader(csvfile)
# 	data_file['large'] = list(reader)
print('Done\n-------------------------------------------------------------------------------------')

print('\nTesting')
print('-------------------------------------------------------------------------------------')

# specify what data is being used
data_set = str(sys.argv[1])
# data_set = 'small'
data = data_file[data_set]

# test = op.gen_path(data)
# print(test)

one_point = op.one_point(data, 1000, 100)
two_point = op.two_point(data, 1000, 100)

print('One Point')
print('Fitness in',data_set,':',one_point[0])

print('-------------------------------------------------------------------------------------')
print('Two Point')
print('Fitness in',data_set,':',two_point[0])
print('-------------------------------------------------------------------------------------\n')