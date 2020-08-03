import numpy as np
from benchmark import get_domain, get_function, get_optmial_solution_text, get_optmial_solution
import matplotlib.pyplot as plt

class PSO:
	'''
	Particle Swarm Optimization
	'''

	def __init__(self, n_particles=100, particle_dimension=10, momentum=0.2, c_pbest=0.5, c_gbest=0.5, benchmark='Ackley', stop_criterion=100):
		'''

		:param n_particles:             Number of particles.
		:param particle_dimension:      Number of attributes in each particle.
		:param momentum:                w parameter, indicates how much the last particle velocity will influence the next one.
		:param c_pbest:                 c1 parameter, indicates how much of the particle best position will influence in the convergence.
		:param c_gbest:                 c2 parameter, indicates how fast the particles will converge to the swarm best position.
		:param benchmark:               The function that PSO will optimizes. Default value = 'Ackley'. Possible values = ['Ackley', 'Alpine', 'Schwefel', 'Happy Cat', 'Brown', 'Exponential'].
		:param stop_criterion:          Number of times without updating g_best.
		'''

		self.n_particles = n_particles
		self.particle_dimension = particle_dimension
		self.momentum = momentum
		self.c_pbest = c_pbest
		self.c_gbest = c_gbest
		self.benchmark_name = benchmark
		self.benchmark_domain = get_domain(benchmark)
		self.benchmark_function = get_function(benchmark)
		self.stop_criterion = stop_criterion
		self.g_best_last_updated = 0                            # number of iterations without updating g_best
		self.total_iterations = 0                              # number total of iterations until the algorithm stops

		# initialization
		self.particles = np.random.uniform(self.benchmark_domain[0],self.benchmark_domain[1], [self.n_particles, self.particle_dimension])
		self.velocity = np.zeros([self.n_particles, self.particle_dimension])
		self.p_best = self.particles
		self.p_best_fitness = self.calculate_fitness()
		self.g_best = self.p_best[np.argmin(self.p_best_fitness)]
		self.g_best_fitness = self.p_best_fitness[np.argmin(self.p_best_fitness)]

	def run_with_reboot(self, print_solution=False, stay_domain=True, n_reboot=20):
		'''
		Run PSO with random reboot. It is used to avoid be stuck in a local minimum.

		:param print_solution:      if true, each iteration will be print
		:param stay_domain:         if true, particles are not allowed to be beyond the function domain
		:param n_reboot:            number of reboots
		'''

		for i in range(n_reboot):
			self.run(print_solution=print_solution, stay_domain=stay_domain, reboot_message=', reboot = ' +str(i))
			self.g_best_last_updated = 0
			self.particles = np.random.uniform(self.benchmark_domain[0], self.benchmark_domain[1],
			                                   [self.n_particles, self.particle_dimension])
			self.velocity = np.zeros([self.n_particles, self.particle_dimension])
			self.p_best = self.particles
			self.p_best_fitness = self.calculate_fitness()

	def run(self, print_solution=False, stay_domain=True, reboot_message=''):
		'''
			Find best optimization.

			:param print_solution:      if true, each iteration will be print
			:param stay_domain:         if true, particles are not allowed to be beyond the function domain
		'''

		while (self.g_best_last_updated < self.stop_criterion) and (self.total_iterations < 1000):

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
				plt.scatter(self.particles[:, 0], self.particles[:, 1])
				plt.scatter(self.g_best[0], self.g_best[1], label= 'g_best fitness: ' + str(self.g_best_fitness))
				plt.scatter(get_optmial_solution(self.benchmark_name)[0], get_optmial_solution(self.benchmark_name)[1], label='optimal solution: ' + get_optmial_solution_text(self.benchmark_name))
				plt.title(self.benchmark_name + reboot_message)
				plt.legend()
				plt.pause(0.1)
				plt.savefig('../img/gif/momentum0/'+str(self.total_iterations))


			self.total_iterations += 1
			fitness = self.calculate_fitness()

			# --- updating p_best
			for i in range(len(self.particles)):

				if fitness[i] < self.p_best_fitness[i]:
					self.p_best[i] = self.particles[i]
					self.p_best_fitness[i] = fitness[i]

			# --- updating g_best
			if self.p_best_fitness[np.argmin(self.p_best_fitness)] < self.g_best_fitness:

				self.g_best_fitness = self.p_best_fitness[np.argmin(self.p_best_fitness)]
				self.g_best = self.p_best[np.argmin(self.p_best_fitness)]
				self.g_best_last_updated = 0
			else:
				self.g_best_last_updated += 1

			# --- update velocity
			for i in range(len(self.particles)):

				r1 = np.random.uniform(0, 1, self.particle_dimension)
				r2 = np.random.uniform(0, 1, self.particle_dimension)

				self.velocity[i] = self.momentum * self.velocity[i] + self.c_pbest * r1 * (self.p_best[i] - self.particles[i]) + self.c_gbest * r2 * (self.g_best - self.particles[i])

			# --- update particle position
			self.particles += self.velocity

			# --- keep particles in the function domain
			if stay_domain:
				for i in range(len(self.particles)):

					self.particles[i][self.particles[i] < self.benchmark_domain[0]] = self.benchmark_domain[0]
					self.particles[i][self.particles[i] > self.benchmark_domain[1]] = self.benchmark_domain[1]

	def calculate_fitness(self):
		fitness = []
		for i in range(len(self.particles)):
			fitness.append(self.benchmark_function(self.particles[i]))

		return np.asarray(fitness)

class IDPSO:
	'''
	Improved Particle Swarm Optimization
	'''

	def __init__(self, n_particles=20, particle_dimension=10, w_initial=0.8, w_final=0.4, u=100, c_pbest=2, c_gbest=2, c_max=0.9, c_min=0.1, benchmark='Ackley', stop_criterion=100, max_total_iteration=1000):
		'''
		:param n_particles:             Number of particles.
		:param particle_dimension:      Number of attributes in each particle.
		:param w_initial:               momentum, initial value for momentum
		:param w_final:                 momentum, final value for momentum
		:param u:                 		adjustment factor
		:param c_pbest:                 c1 parameter, indicates how much of the particle best position will influence in the convergence.
		:param c_gbest:                 c2 parameter, indicates how fast the particles will converge to the swarm best position.
		:param benchmark:               The function that PSO will optimizes. Default value = 'Ackley'. Possible values = ['Ackley', 'Alpine', 'Schwefel', 'Happy Cat', 'Brown', 'Exponential'].
		:param stop_criterion:          Number of times without updating g_best.
		'''

		self.n_particles = n_particles
		self.particle_dimension = particle_dimension
		self.w_initial = w_initial			# initial momentum
		self.w_final = w_final				# final momentum
		self.u = u							# adjustment factor
		self.c_pbest = c_pbest
		self.c_gbest = c_gbest
		self.c_max = c_max					# maximum value for c(phi) -> c1 or c2
		self.c_min = c_min					# minimum value for c(phi) -> c1 or c2
		self.benchmark_name = benchmark
		self.benchmark_domain = get_domain(benchmark)
		self.benchmark_function = get_function(benchmark)
		self.stop_criterion = stop_criterion
		self.g_best_last_updated = 0                            # number of iterations without updating g_best
		self.total_iterations = 0                               # number total of iterations until the algorithm stops
		self.max_total_iteration = max_total_iteration			# max limit for total_iterations

		# initialization
		self.particles = np.random.uniform(self.benchmark_domain[0],self.benchmark_domain[1], [self.n_particles, self.particle_dimension])
		self.velocity = np.zeros([self.n_particles, self.particle_dimension])
		self.p_best = self.particles
		self.p_best_fitness = self.calculate_fitness()
		self.g_best = self.p_best[np.argmin(self.p_best_fitness)]
		self.g_best_fitness = self.p_best_fitness[np.argmin(self.p_best_fitness)]

	def run_with_reboot(self, print_solution=False, stay_domain=True, n_reboot=20):
		'''
		Run PSO with random reboot. It is used to avoid be stuck in a local minimum.
		:param print_solution:      if true, each iteration will be print
		:param stay_domain:         if true, particles are not allowed to be beyond the function domain
		:param n_reboot:            number of reboots
		'''

		for i in range(n_reboot):
			self.run(print_solution=print_solution, stay_domain=stay_domain, reboot_message=', reboot = ' +str(i))
			self.g_best_last_updated = 0
			self.particles = np.random.uniform(self.benchmark_domain[0], self.benchmark_domain[1],
			                                   [self.n_particles, self.particle_dimension])
			self.velocity = np.zeros([self.n_particles, self.particle_dimension])
			self.p_best = self.particles
			self.p_best_fitness = self.calculate_fitness()

	def run(self, print_solution=False, stay_domain=True, reboot_message=''):
		'''
			Find best optimization.
			:param print_solution:      if true, each iteration will be print
			:param stay_domain:         if true, particles are not allowed to be beyond the function domain
		'''

		#while (self.g_best_last_updated < self.stop_criterion) and (self.total_iterations < self.max_total_iteration):
		while (self.total_iterations < self.max_total_iteration):

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
				plt.scatter(self.particles[:, 0], self.particles[:, 1])
				plt.scatter(self.g_best[0], self.g_best[1], label= 'g_best fitness: ' + str(self.g_best_fitness))
				plt.scatter(get_optmial_solution(self.benchmark_name)[0], get_optmial_solution(self.benchmark_name)[1], label='optimal solution: ' + get_optmial_solution_text(self.benchmark_name))
				plt.title(self.benchmark_name + reboot_message)
				plt.legend()
				plt.pause(0.1)


			self.total_iterations += 1
			fitness = self.calculate_fitness()

			# --- updating p_best
			for i in range(len(self.particles)):

				if fitness[i] < self.p_best_fitness[i]:
					self.p_best[i] = self.particles[i]
					self.p_best_fitness[i] = fitness[i]

			# --- updating g_best
			if self.p_best_fitness[np.argmin(self.p_best_fitness)] < self.g_best_fitness:

				self.g_best_fitness = self.p_best_fitness[np.argmin(self.p_best_fitness)]
				self.g_best = self.p_best[np.argmin(self.p_best_fitness)]
				self.g_best_last_updated = 0
			else:
				self.g_best_last_updated += 1

			# --- update velocity
			for i in range(len(self.particles)):

				r1 = np.random.uniform(0, 1, self.particle_dimension)
				r2 = np.random.uniform(0, 1, self.particle_dimension)

				w, c1, c2 = self.calculate_parameters(i)

				self.velocity[i] = w * self.velocity[i] + c1 * r1 * (self.p_best[i] - self.particles[i]) + c2 * r2 * (self.g_best - self.particles[i])

				#signals = np.ones([len(self.velocity[i])])
				#signals[self.velocity[i] < 0] = -1
				#self.velocity[i][self.velocity[i] < 0.3] = 0.3

				#'''
				if self.benchmark_name == 'wide-resnet':
					print('ajeitar limite da velocidade pra wide-resner')
				else:
					domain_size = np.abs(self.benchmark_domain[1] - self.benchmark_domain[0])
					self.velocity[i][self.velocity[i] > (0.05 * domain_size)] = 0.05 * domain_size
					self.velocity[i][self.velocity[i] < (-0.05 * domain_size)] = -0.05 * domain_size
				#'''

				#print(self.velocity[i])
				#self.velocity[i] = self.velocity[i] * signals
				#self.velocity[i][self.velocity[i] < -0.3] = -0.3
				#self.velocity[i][self.velocity[i] > 0.3] = 0.3

				#print(self.velocity[i])
			# --- update particle position
			self.particles += self.velocity

			# --- keep particles in the function domain
			if stay_domain:
				for i in range(len(self.particles)):

					self.particles[i][self.particles[i] < self.benchmark_domain[0]] = self.benchmark_domain[0]
					self.particles[i][self.particles[i] > self.benchmark_domain[1]] = self.benchmark_domain[1]

	def calculate_parameters(self, particle_id):
		'''
		Calculate parameters from IDPSO for the i-th particle
		:param particle_id:		particle indices
		:return:				w, c1, c2
		'''

		division_const = 0.001

		# calculate phi
		phi = np.abs((np.linalg.norm(self.g_best - self.particles[particle_id]) + division_const) / (np.linalg.norm(self.p_best[particle_id] - self.particles[particle_id]) + division_const))

		dist_p = np.linalg.norm(self.p_best[particle_id] - self.particles[particle_id])
		dist_g = np.linalg.norm(self.g_best - self.particles[particle_id])
		#print([dist_g, dist_p, phi])
		#print(self.g_best)
		#print(self.particles[particle_id])
		#print(self.p_best[particle_id])
		# w, momentum
		first_term = self.w_initial - self.w_final
		exp_term = ((1 + np.log(phi)) * self.max_total_iteration) / self.u
		second_term = 1 + np.exp(phi * (self.total_iterations - exp_term))
		w = (first_term/second_term) + self.w_final

		# c1, c_pbest
		c1 = self.c_pbest / (phi + division_const)
		#'''
		if c1 < self.c_min:
			c1 = self.c_min
		if c1 > self.c_max:
			c1 = self.c_max
		#'''

		# c2, c_gbest
		c2 = self.c_gbest * phi
		#'''
		if c2 < self.c_min:
			c2 = self.c_min
		if c2 > self.c_max:
			c2 = self.c_max
		#'''

		#print([w, c1, c2, phi])
		return w, c1, c2


	def calculate_fitness(self):
		fitness = []
		for i in range(len(self.particles)):
			fitness.append(self.benchmark_function(self.particles[i]))

		return np.asarray(fitness)