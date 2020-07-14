import numpy as np
from benchmark import get_domain, get_function, get_optmial_solution_text, get_optmial_solution
import matplotlib.pyplot as plt

class ABC:
	'''
	Artificial Bee Colony
	'''

	def __init__(self, n_bees=20, problem_dimension=10, benchmark='Ackley', max_iterations=100, max_food_iteration=0):
		'''

		:param n_bees:                      NP, Number of Bees
		:param problem_dimension:           D, Number of attributes to be optimize.
		:param benchmark:                   The function that PSO will optimizes. Default value = 'Ackley'. Possible values = ['Ackley', 'Alpine', 'Schwefel', 'Happy Cat', 'Brown', 'Exponential'].
		'''

		self.n_bees = n_bees
		self.problem_dimension = problem_dimension
		self.benchmark_name = benchmark
		self.benchmark_domain = get_domain(benchmark)
		self.benchmark_function = get_function(benchmark)
		self.food_number = int(n_bees / 2)

		if max_food_iteration == 0:
			self.max_food_iteration = (n_bees * problem_dimension)/2    # number total of iterations until the food source be avoided
		else:
			self.max_food_iteration = max_food_iteration
		self.max_iterations = max_iterations                        # number of iteration until the optimization stops

		# initialization
		self.food_source = np.zeros([self.food_number, problem_dimension])
		self.food_fitness = np.zeros(self.food_number)
		self.food_f_x = np.zeros(self.food_number)
		self.food_probability = np.zeros(self.food_number)
		self.food_iteration = np.zeros(self.food_number)


		# find food source
		for i in range(self.food_number):
			food_source, food_fitness = self.find_food_source_randonmly()
			self.food_source[i] = food_source
			self.food_fitness[i] = food_fitness

		# calculating probabilities
		self.calculate_probability()

		# best solution
		self.best_source = np.copy(self.food_source[np.argmax(self.food_fitness)])
		self.best_fitness = max(self.food_fitness)

	def run_stop_criterion(self, print_solution=False, iterations_without_improving=20):
		'''
		Find best solution. Stop criterion is: run until best_source does not update for 'n' iterations.

		:iterations_without_improving:          Number of iterations without improvement.
		'''

		iterations = 0
		while iterations <= iterations_without_improving:

			# --- printing
			if print_solution:
				plt.clf()

				negative_discount = np.abs(self.benchmark_domain[0] * 0.2)
				positive_discount = self.benchmark_domain[1] * 0.2

				if negative_discount == 0:
					negative_discount = 2
				if positive_discount == 0:
					positive_discount = 2

				plt.ylim(self.benchmark_domain[0] - negative_discount, self.benchmark_domain[1] + positive_discount)
				plt.xlim(self.benchmark_domain[0] - negative_discount, self.benchmark_domain[1] + positive_discount)
				plt.scatter(self.food_source[:, 0], self.food_source[:, 1])
				plt.scatter(self.best_source[0], self.best_source[1], label= 'g_best fitness: ' + str(self.benchmark_function(self.best_source)))
				plt.scatter(get_optmial_solution(self.benchmark_name)[0], get_optmial_solution(self.benchmark_name)[1], label='optimal solution: ' + get_optmial_solution_text(self.benchmark_name))
				plt.title(self.benchmark_name)
				plt.legend()
				plt.pause(0.1)
			# ---
			# employed bees
			for j in range(self.food_number):
				new_food_source, new_food_source_fitness = self.update_food_source(j)

				# if new source is better than the current one
				if new_food_source_fitness > self.food_fitness[j]:
					self.food_source[j] = new_food_source
					self.food_fitness[j] = new_food_source_fitness
					self.food_iteration[j] = 0
				else:
					# if new source is not better than the current one
					self.food_iteration[j] += 1

			# calculating probabilities
			self.calculate_probability()

			# onlooker bees
			for j in range(self.food_number):

				# getting random food source
				random_source = np.random.choice(self.food_number, 1, p=self.food_probability)[0]

				# update random food source
				new_food_source, new_food_source_fitness = self.update_food_source(random_source)

				# if new source is better than the current one
				if new_food_source_fitness > self.food_fitness[random_source]:
					self.food_source[random_source] = new_food_source
					self.food_fitness[random_source] = new_food_source_fitness
					self.food_iteration[random_source] = 0
				else:
					self.food_iteration[random_source] += 1

			# memorizing best solution
			if max(self.food_fitness) > self.best_fitness:
				self.best_fitness = max(self.food_fitness)
				self.best_source = np.copy(self.food_source[np.argmax(self.food_fitness)])
				iterations = 0
			else:
				iterations += 1


			# if food source is empty get new food source
			if max(self.food_iteration) > self.max_food_iteration:
				food_source, food_fitness = self.find_food_source_randonmly()

				self.food_source[np.argmax(self.food_fitness)] = food_source
				self.food_fitness[np.argmax(self.food_fitness)] = food_fitness
				self.food_iteration[np.argmax(self.food_fitness)] = 0


	def run(self, print_solution=False):
		'''
		Find best optmization
		'''

		for i in range(self.max_iterations):

			# --- printing
			if print_solution:
				plt.clf()

				negative_discount = np.abs(self.benchmark_domain[0] * 0.2)
				positive_discount = self.benchmark_domain[1] * 0.2

				if negative_discount == 0:
					negative_discount = 2
				if positive_discount == 0:
					positive_discount = 2

				plt.ylim(self.benchmark_domain[0] - negative_discount, self.benchmark_domain[1] + positive_discount)
				plt.xlim(self.benchmark_domain[0] - negative_discount, self.benchmark_domain[1] + positive_discount)
				plt.scatter(self.food_source[:, 0], self.food_source[:, 1])
				plt.scatter(self.best_source[0], self.best_source[1], label= 'g_best fitness: ' + str(self.benchmark_function(self.best_source)))
				plt.scatter(get_optmial_solution(self.benchmark_name)[0], get_optmial_solution(self.benchmark_name)[1], label='optimal solution: ' + get_optmial_solution_text(self.benchmark_name))
				plt.title(self.benchmark_name + ', iteration ' + str(i))
				plt.legend()
				plt.pause(0.1)
			# ---
			# employed bees
			for j in range(self.food_number):
				new_food_source, new_food_source_fitness = self.update_food_source(j)

				# if new source is better than the current one
				if new_food_source_fitness > self.food_fitness[j]:
					self.food_source[j] = new_food_source
					self.food_fitness[j] = new_food_source_fitness
					self.food_iteration[j] = 0
				else:
					# if new source is not better than the current one
					self.food_iteration[j] += 1

			# calculating probabilities
			self.calculate_probability()

			# onlooker bees
			for j in range(self.food_number):

				# getting random food source
				random_source = np.random.choice(self.food_number, 1, p=self.food_probability)[0]

				# update random food source
				new_food_source, new_food_source_fitness = self.update_food_source(random_source)

				# if new source is better than the current one
				if new_food_source_fitness > self.food_fitness[random_source]:
					self.food_source[random_source] = new_food_source
					self.food_fitness[random_source] = new_food_source_fitness
					self.food_iteration[random_source] = 0
				else:
					self.food_iteration[random_source] += 1

			# memorizing best solution
			if max(self.food_fitness) > self.best_fitness:
				self.best_fitness = max(self.food_fitness)
				self.best_source = np.copy(self.food_source[np.argmax(self.food_fitness)])


			# if food source is empty get new food source
			if max(self.food_iteration) > self.max_food_iteration:
				food_source, food_fitness = self.find_food_source_randonmly()

				self.food_source[np.argmax(self.food_fitness)] = food_source
				self.food_fitness[np.argmax(self.food_fitness)] = food_fitness
				self.food_iteration[np.argmax(self.food_fitness)] = 0



	def update_food_source(self, food_source_id):
		'''
		Update food source.

		:param food_source_id:      Food Source ID
		:return:                    new_food_source, new_food_source_fitness
		'''

		# getting current food source
		food_source = np.copy(self.food_source[food_source_id])

		# selecting random attribute
		random_attribute = np.random.randint(0, self.problem_dimension, 1)[0]

		# selecting random food source, excluding self.food_source[food_source_id]
		probabilities = np.zeros(self.food_number) + (1/(self.food_number - 1))
		probabilities[food_source_id] = 0
		random_food_source = np.random.choice(self.food_number, 1, p=probabilities)[0]

		# getting random number between -1 and 1
		random_theta = np.random.uniform(-1,-1,1)

		# new food source
		new_food_source = food_source
		new_food_source[random_attribute] += random_theta * (food_source[random_attribute] - self.food_source[random_food_source][random_attribute])

		# kepping new attribute in the benchmark range
		if new_food_source[random_attribute] < self.benchmark_domain[0]:
			new_food_source[random_attribute] = self.benchmark_domain[0]
		if new_food_source[random_attribute] > self.benchmark_domain[1]:
			new_food_source[random_attribute] = self.benchmark_domain[1]

		return new_food_source, self.calculate_fitness(new_food_source)


	def find_food_source_randonmly(self):
		'''
		Find new food source randomly.
		:return: food_source, fitness
		'''

		rand = np.random.uniform(0, 1, self.problem_dimension)
		food_source = self.benchmark_domain[0] + rand * (self.benchmark_domain[1] - self.benchmark_domain[0])
		food_fitness = self.calculate_fitness(food_source)

		return food_source, food_fitness

	def calculate_fitness(self, food_source):
		'''
		Calculate fitness for food source.

		:param food_source:     food source.

		:return:    fitness
		'''

		f_x = self.benchmark_function(food_source)

		if f_x >= 0:
			fitness = (1/(1+f_x))
		else:
			fitness = 1 + np.abs(f_x)

		return fitness

	def calculate_probability(self):
		'''
		Calculate probability of each food source.
		'''

		for i in range(len(self.food_source)):
			self.food_probability[i] = self.food_fitness[i] / np.sum(self.food_fitness)