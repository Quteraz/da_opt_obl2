import numpy as np
from operator import itemgetter

def gen_set(size):
	data = np.full((size, size), False)
	allowed = np.random.randint(1, 6, size=size)

	for index, val in enumerate(allowed):
		# iterate val times
		min_val = index + 1
		
		for _ in range(val):
			# check if any connections are left
			allowed[index] = 0
			if all(v == 0 for v in allowed):
				break
			# set up node
			node = np.random.randint(min_val,size)
			while allowed[node] == 0:
				node = np.random.randint(min_val,size)
			# connect and reduce node
			data[node][index] = True
			allowed[node] -= 1
	return data

def gen_path(data):
	# generate a random coloring solution and fitness
	path = np.random.randint(0,3, size=len(data[0]))
	fitness = fit_calc(data, path)

	return {'path':path, 'fitness':fitness}

def gen_pop(data, size):
	population = []
	for _ in range(size):
		population.append(gen_path(data))
	return population

def fit_calc(data, solution):
	fit = 0
	# index = node, el = list
	for index, el in enumerate(data):
		# pos = node, node = val
		for pos, node in enumerate(el):
			# symmetry break
			if index == pos:
				break
			# count fit conditions
			if node and solution[index] == solution[pos]:
				fit += 1
	return fit

def one_point(data, iterations, pop):
	# one point crossover
	# mutation is present with prob of 0.1

	population = gen_pop(data, pop)

	# one point part
	for _ in range(iterations):
		# select pairs
		# generate children
		# sort and reduce pop by 2

		# generationg children for each pair
		pair = np.random.permutation(pop)
		counter = 0
		while counter < pop:
			rand_pos = np.random.randint(0,len(data[0]))
			child1, child2 = population[counter], population[counter+1]
			child1['path'][rand_pos], child2['path'][rand_pos] = child2['path'][rand_pos], child1['path'][rand_pos]
			child1['fitness'],child2['fitness'] = fit_calc(data, child1['path']),	fit_calc(data, child2['path'])
			population.append([child1,child2])
			counter+=2
		
		# sort_on = 'fitness'
		# decorated = [(dict_[sort_on], dict_) for dict_ in population]
		# decorated.sort()
		# population = [dict_ for (key, dict_) in decorated]

		# population.sort(key=lambda k: k[1])
		print(type(population[0]))
		population = sorted(population, key=itemgetter('fitness'))
		population = population[:len(population)//2]

	return population

def two_point(data, iterations, pop):
	# two point crossover with starting pop of 2
	# mutation is present with prob of 0.1

	population = gen_pop(data, 2)