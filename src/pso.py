import numpy as np
from benchmark import get_domain, get_function

class PSO:
	'''
	Particle Swarm Optimization
	'''

	def __init__(self, n_particles=100, particle_dimension=10, momentum=0.2, c_pbest=0.8, c_gbest=0.2, benchmark='Ackley', stop_criterion=100):
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
		self.total_itereations = 0                              # number total of iterations until the algorithm stops

		# initialization
		self.particles = np.random.uniform(self.benchmark_domain[0],self.benchmark_domain[1], [self.n_particles, self.particle_dimension])
		self.velocity = np.zeros([self.n_particles, self.particle_dimension])
		self.p_best = self.particles
		self.p_best_fitness = self.calculate_fitness()
		self.g_best = self.p_best[np.argmin(self.p_best_fitness)]
		self.g_best_fitness = self.p_best_fitness[np.argmin(self.p_best_fitness)]


	def run(self):
		'''
			Find best optmization
		'''

		while self.g_best_last_updated < self.stop_criterion:

			self.total_itereations += 1
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



	def calculate_fitness(self):
		fitness = []
		for i in range(len(self.particles)):
			fitness.append(self.benchmark_function(self.particles[i]))

		return np.asarray(fitness)