# Python3 program to create target string, starting from 
# random string using Genetic Algorithm 

# https://en.wikipedia.org/wiki/Wolf,_goat_and_cabbage_problem
# A farmer with a wolf, a goat, and a cabbage must cross a river by boat.
# The boat can carry only the farmer and a single item. 
# If left unattended together, the wolf would eat the goat, 
# or the goat would eat the cabbage. 
# How can they cross the river without anything being eaten?

#Take the goat over -> (3)
#Return empty-handed -> (1)
#Take the wolf or cabbage over -> (2) or (4)
#Return with the goat -> (3)
#Take whichever wasn't taken in step 3 over -> (2) or (4)
#Return empty-handed -> (1)
#Take the goat over -> (3)
# 3123413
# 3143213

import random 
from simulator import Simulator

# Number of individuals in each generation 
POPULATION_SIZE = 100_000

# Valid genes 
GENES = '01234'

MAX_STEPS = 8

class Individual(object): 
	''' 
	Class representing individual in population 
	'''
	def __init__(self, chromosome): 
		self.chromosome = chromosome 
		self.fitness = 0

	@classmethod
	def mutated_genes(self): 
		''' 
		create random genes for mutation 
		'''
		global GENES 
		gene = random.choice(GENES) 
		return gene 

	@classmethod
	def create_gnome(self): 
		''' 
		create chromosome or string of genes 
		'''
		global MAX_STEPS 
		return [self.mutated_genes() for _ in range(MAX_STEPS)] 

	def mate(self, par2):
		''' 
		Perform mating and produce new offspring 
		'''

		# chromosome for offspring 
		child_chromosome = [] 
		for gp1, gp2 in zip(self.chromosome, par2.chromosome):	 

			# random probability 
			prob = random.random() 

			# if prob is less than 0.45, insert gene 
			# from parent 1 
			if prob < 0.45: 
				child_chromosome.append(gp1) 

			# if prob is between 0.45 and 0.90, insert 
			# gene from parent 2 
			elif prob < 0.90: 
				child_chromosome.append(gp2) 

			# otherwise insert random gene(mutate), 
			# for maintaining diversity 
			else: 
				child_chromosome.append(self.mutated_genes()) 

		# create new Individual(offspring) using 
		# generated chromosome for offspring 
		return Individual(child_chromosome) 

# Driver code 
def main(): 
	global POPULATION_SIZE 

	sim = Simulator()
	
	#current generation 
	generation = 1

	found = False
	population = [] 

	# create initial population 
	for _ in range(POPULATION_SIZE): 
		gnome = Individual.create_gnome() 
		individual = Individual(gnome)
		individual.fitness = sim.simulate(individual.chromosome)
		population.append(individual)

	while not found:

		# sort the population in increasing order of fitness score 
		population = sorted(population, key = lambda x:x.fitness) 

		# if the individual having lowest fitness score ie. 
		# 0 then we know that we have reached to the target 
		# and break the loop 
		if population[0].fitness <= 7: 
			found = True
			sim.print(population[0].chromosome)
			break

		# Otherwise generate new offsprings for new generation 
		new_generation = [] 

		# Perform Elitism, that mean 10% of fittest population 
		# goes to the next generation 
		s = int((10*POPULATION_SIZE)/100)
		new_generation.extend(population[:s]) 

		# From 50% of fittest population, Individuals 
		# will mate to produce offspring 
		s = int((90*POPULATION_SIZE)/100)
		for _ in range(s): 
			parent1 = random.choice(population[:50]) 
			parent2 = random.choice(population[:50]) 
			child = parent1.mate(parent2) 
			new_generation.append(child) 

		population = new_generation 

		for individual in population:
			individual.fitness = sim.simulate(individual.chromosome)

		print("Generation: {}\tString: {}\tFitness: {}". 
			format(generation, 
			"".join(population[0].chromosome), 
			population[0].fitness)
		) 

		generation += 1

	
	print("Generation: {}\tString: {}\tFitness: {}".
		format(generation, 
		"".join(population[0].chromosome), 
		population[0].fitness)) 

if __name__ == '__main__': 
	main() 
