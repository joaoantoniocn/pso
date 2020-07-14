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

		while (self.g_best_last_updated < self.stop_criterion) and (self.total_iterations < 5000):

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