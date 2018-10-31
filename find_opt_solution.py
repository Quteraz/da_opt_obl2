import numpy as np

def gen_set(size):
	data = np.full((size, size), False)
	allowed = np.random.randint(1, 6, size=size)

	for index, val in enumerate(allowed):
		# iterate val times
		min_val = index + 1
		
		for _ in range(val):
			allowed[index] = 0
			# check if any connections are left
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
	# generate a random coloring solution
	return np.random.randint(0,3, size=len(data[0]))

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
	# one point crossover with starting pop of 2
	# mutation is present with prob of 0.1

	population = gen_pop(data, pop)
	fitness = []

	# calc fitness of population
	for count in range(pop):
		fitness.append(fit_calc(data, population[count]))

	# one point part
	for _ in range(iterations):

	return fit

def two_point(data, iterations):
	# two point crossover with starting pop of 2
	# mutation is present with prob of 0.1

	population = gen_pop(data, 2)