from pso import PSO
from abc_ import ABC
from benchmark import get_optmial_solution_text
import numpy as np

benchmark = ['Ackley', 'Alpine', 'Schwefel', 'Happy Cat', 'Brown', 'Exponential']
dimension=50
'''
for i in range(len(benchmark)):

	modelo = PSO(n_particles=100, particle_dimension=dimension, momentum=0.5, c_pbest=0.5, c_gbest=0.5, benchmark=benchmark[i], stop_criterion=20)
	modelo.run(print_solution=True, stay_domain=True)

	print('----------')
	print('benchmark: ' + benchmark[i])
	print('dimension: ' + str(dimension))
	print('iterations: ' + str(modelo.total_itereations))
	print('fitness: ' + str(modelo.g_best_fitness))
	print('solution: ' +str(modelo.g_best))
	print('optimal solution: ' + get_optmial_solution_text(benchmark[i]))
	print('----------')
'''
'''
for i in range(len(benchmark)):
	modelo = ABC(n_bees=200, problem_dimension=dimension, benchmark=benchmark[i], max_iterations=200, max_food_iteration=20)
	modelo.run(print_solution=True)

	print('----------')
	print('benchmark: ' + benchmark[i])
	print('dimension: ' + str(dimension))
	print('fitness: ' + str(modelo.best_fitness))
	print('solution: ' + str(modelo.best_source))
	print('optimal solution: ' + get_optmial_solution_text(benchmark[i]))
	print('----------')
'''