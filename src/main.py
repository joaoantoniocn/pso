from pso import PSO
import numpy as np

modelo = PSO()
modelo.run()

print('iterations: ' + str(modelo.total_itereations))
print('fitness: ' + str(modelo.g_best_fitness))
