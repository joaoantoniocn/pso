import numpy as np

def get_domain(benchmark_name):

	domain = {
		'Ackley': [-32, 32],
		'Alpine': [0, 10],
		'Schwefel': [-500, 500],
		'Happy Cat': [-2, 2],
		'Brown': [-1, 4],
		'Exponential': [-1, 1]
	}

	return domain[benchmark_name]

def get_function(benchmark_name):
	functions = {
		'Ackley': ackley_function,
		'Alpine': alpine_function,
		'Schwefel': schwefel_function,
		'Happy Cat': happy_cat_function,
		'Brown': brown_function,
		'Exponential': exponential_function
	}

	return functions[benchmark_name]

def get_optmial_solution(benchmark_name):
	best_solution = {
		'Ackley': 'f(x∗)=0 at x∗=(0,…,0).',
		'Alpine': 'f(x∗)=0 located at x∗=(0,…,0).',
		'Schwefel': 'f(x∗)=0 at x∗=(420.9687,…,420.9687)',
		'Happy Cat': 'f(x∗)=0 located at x∗=(−1,…,−1).',
		'Brown': 'f(x∗)=0 located at x∗=0.',
		'Exponential': 'f(x∗)= at x∗=0.'
	}

	return best_solution[benchmark_name]


def ackley_function(x, a=20, b=0.2, c=2*np.pi):
	'''
		http://benchmarkfcns.xyz/benchmarkfcns/ackleyfcn.html
	'''

	part_1 = -a * np.exp(-b * np.sqrt(np.mean(np.power(x, 2))))
	part_2 = np.exp(np.mean(np.cos(c * x)))

	result = part_1 - part_2 + a + np.exp(1)

	return result


def alpine_function(x):
	'''
		http://benchmarkfcns.xyz/benchmarkfcns/alpinen1fcn.html
	'''

	return np.sum(np.abs((x * np.sin(x)) + 0.1 * x))

def schwefel_function(x):
	'''
		http://benchmarkfcns.xyz/benchmarkfcns/schwefelfcn.html
	'''

	return (418.9829 * len(x)) - np.sum(x * np.sin(np.sqrt(np.abs(x))))

def happy_cat_function(x, alpha=0.125):
	'''
		http://benchmarkfcns.xyz/benchmarkfcns/happycatfcn.html
	'''

	part_1 = np.power(np.power(np.sum(np.power(x, 2)) - len(x), 2), alpha)
	part_2 = (1/len(x)) * ((0.5 * np.sum(np.power(x, 2))) + np.sum(x))

	return part_1 + part_2 + 0.5

def brown_function(x):
	'''
		http://benchmarkfcns.xyz/benchmarkfcns/brownfcn.html
	'''

	result = 0
	for i in range(len(x)-1):
		x2 = np.power(x[i], 2)
		xi2 = np.power(x[i+1], 2)

		result += np.power(x2, xi2 + 1) + np.power(xi2, x2 + 1)

	return result

def exponential_function(x):
	'''
		http://benchmarkfcns.xyz/benchmarkfcns/exponentialfcn.html
	'''

	return -1 * np.exp(-0.5 * np.sum(np.power(x, 2)))