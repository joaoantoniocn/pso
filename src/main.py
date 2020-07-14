from pso import PSO
from abc_ import ABC
from benchmark import get_optmial_solution_text
import numpy as np
from tqdm import tqdm
from time import time

benchmark = ['Ackley', 'Alpine', 'Schwefel', 'Happy Cat', 'Brown', 'Exponential']
dimension= [10, 20, 50]

# --- run N times for a specific benchmark
n_times = 100
benchmark_i = 0
#'''
for j in range(2, len(benchmark)):
	for k in range(len(dimension)):
		fitness = []
		iterations = []
		begin = time()
		for i in tqdm(range(n_times)):
			modelo = PSO(n_particles=100, particle_dimension=dimension[k], momentum=0.6, c_pbest=0.4, c_gbest=0.6, benchmark=benchmark[j], stop_criterion=40)
			modelo.run(print_solution=False, stay_domain=True)

			fitness.append(modelo.g_best_fitness)
			iterations.append(modelo.total_iterations)
		end = time()
		fitness = np.asarray(fitness)
		iterations = np.asarray(iterations)
		print('benchmark ' + benchmark[j])
		print('dimension ' + str(dimension[k]))
		print('fitness min ' + str(np.min(fitness)))
		print('tempo ' + str(end-begin))
		print('-----')
#'''
#print('iterations mean ' + str(np.min(iterations)))
#print('iterations std ' + str(np.std(iterations)))

# --- run over every benchmark
'''
for i in range(len(benchmark)):

	modelo = PSO(n_particles=100, particle_dimension=dimension, momentum=0.6, c_pbest=0.4, c_gbest=0.6, benchmark=benchmark[i], stop_criterion=40)
	modelo.run(print_solution=False, stay_domain=True)

	print('----------')
	print('benchmark: ' + benchmark[i])
	print('dimension: ' + str(dimension))
	print('iterations: ' + str(modelo.total_iterations))
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
	print('fitness: ' + str(modelo.benchmark_function(modelo.best_source)))
	print('solution: ' + str(modelo.best_source))
	print('optimal solution: ' + get_optmial_solution_text(benchmark[i]))
	print('----------')
'''