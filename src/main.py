from pso import PSO
from benchmark import get_optmial_solution
import numpy as np

benchmark = ['Ackley', 'Alpine', 'Schwefel', 'Happy Cat', 'Brown', 'Exponential']

for i in range(len(benchmark)):

	modelo = PSO(n_particles=100, particle_dimension=2, momentum=0.8, c_pbest=0.9, c_gbest=0.1, benchmark=benchmark[i], stop_criterion=20)
	modelo.run(print_solution=True, stay_domain=True)

	print('----------')
	print('benchmark: ' + benchmark[i])
	print('iterations: ' + str(modelo.total_itereations))
	print('fitness: ' + str(modelo.g_best_fitness))
	print('solution: ' +str(modelo.g_best))
	print('optimal solution: ' + get_optmial_solution(benchmark[i]))
	print('----------')