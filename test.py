import find_opt_solution as op
import csv
import sys
import matplotlib.pyplot as plt

print('\nReading files')

# specify what data is being used
data_set = str(sys.argv[1])

if data_set == 'test':
	with open('datasets/data_50', 'r') as csvfile:
		reader = csv.reader(csvfile)
		data= list(reader)
elif data_set == 'small':
	with open('datasets/data_100', 'r') as csvfile:
		reader = csv.reader(csvfile)
		data = list(reader)
elif data_set == 'medium':
	with open('datasets/data_1000', 'r') as csvfile:
		reader = csv.reader(csvfile)
		data = list(reader)
elif data_set == 'large':
	with open('datasets/data_50000', 'r') as csvfile:
		reader = csv.reader(csvfile)
		data = list(reader)
else:
	print('error: no dataset with matching values. exiting')
	quit()


print('Done\n-------------------------------------------------------------------------------------')

print('\nOptimizing Coloring Solution')
print('-------------------------------------------------------------------------------------')

# test = op.gen_path(data)
# print(test)

print('One Point')

one_point, one_plt = op.one_point(data, 1000, 50)
print('Fitness in',data_set,':',one_point[0])

print('-------------------------------------------------------------------------------------')
print('Two Point')

two_point, two_plt = op.two_point(data, 1000, 50)
print('Fitness in',data_set,':',two_point[0])

print('-------------------------------------------------------------------------------------\n')
# plt.subplot(111)
plt.title('Graph Coloring Problem')
plt.xlabel('Generations')
plt.ylabel('Fitness')
plt.plot(one_plt)
plt.plot(two_plt, 'r')
plt.tight_layout()
plt.savefig('datasets/plotting.png')
plt.show()