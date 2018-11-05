import numpy as np
from operator import itemgetter
import copy as cp

def gen_set(size):
	data = np.full((size, size), False)
	allowed = np.random.randint(1, 4, size=size)

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
		# node = node, val = bool
		for node, val in enumerate(el):
			# symmetry break
			if index == node:
				break
			# count fit conditions
			if val == 'True' and solution[index] == solution[node]:
				fit += 1
	return fit

def one_point(data, iterations, pop):
	# one point crossover
	# mutation is present with prob of 0.1

	plot = []
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
			# add children to population
			rand_pos = np.random.randint(0,len(data[0]))
			children = [cp.copy(population[pair[counter]]), cp.copy(population[pair[counter+1]])]
			# children = [cp.copy(population[counter]), cp.copy(population[counter+1])]
			children[0]['path'][rand_pos], children[1]['path'][rand_pos] = children[1]['path'][rand_pos], children[0]['path'][rand_pos]
			for child in children:
				child['fitness'] = fit_calc(data, child['path'])

			# check for mutation
			for child in children:
				mutate = np.random.rand()
				if mutate <= 0.1:
					# random values
					rand_pos = np.random.randint(0,len(data[0]))
					rand_val = np.random.randint(0,3)
					while rand_val == child['path'][rand_pos]:
						rand_val = np.random.randint(0,3)

					child['path'][rand_pos] = rand_val
					child['fitness'] = fit_calc(data, child['path'])

			population += children

			counter+=2
		
		population = sorted(population, key=itemgetter('fitness'))
		chunk1 = population[:len(population)//2]
		# chunk2 = population[len(population)//2:]
		# population = chunk1[:len(chunk1)//2] + chunk2[:len(chunk2)//2]
		population = chunk1

		plot += [population[0]['fitness']]

	return population, plot

def two_point(data, iterations, pop):
	# two point crossover with starting pop of 2
	# mutation is present with prob of 0.1

	plot = []
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
			# add children to population
			rand_pos = np.random.randint(0,len(data[0]), size=2)
			rand_pos.sort()

			children = [cp.copy(population[pair[counter]]), cp.copy(population[pair[counter+1]])]
			while rand_pos[0] != rand_pos[1]:
				children[0]['path'][rand_pos], children[1]['path'][rand_pos] = children[1]['path'][rand_pos], children[0]['path'][rand_pos]
				rand_pos[0] += 1

			for child in children:
				child['fitness'] = fit_calc(data, child['path'])

			# check for mutation
			for child in children:
				mutate = np.random.rand()
				if mutate <= 0.1:
					# random values
					rand_pos = np.random.randint(0,len(data[0]))
					rand_val = np.random.randint(0,3)
					while rand_val == child['path'][rand_pos]:
						rand_val = np.random.randint(0,3)

					child['path'][rand_pos] = rand_val
					child['fitness'] = fit_calc(data, child['path'])

			population += children

			counter+=2
		
		population = sorted(population, key=itemgetter('fitness'))
		chunk1 = population[:len(population)//2]
		chunk2 = population[len(population)//2:]
		population = chunk1[:len(chunk1)//2] + chunk2[:len(chunk2)//2]

		plot += [population[0]['fitness']]

	return population, plot