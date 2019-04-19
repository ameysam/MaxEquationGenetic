import numpy as np
from constants import Constant


class Genetic:

    def __init__(self):
        self.fitness = None
        self.parents = None
        self.offspring = None

    def calcFitness(self, inputs, population):
        self.fitness = np.sum(population * inputs, axis=1)
        return self.fitness

    def getMating(self, population, count):
        parents = np.empty((count, population.shape[1]))
        for i in range(count):
            max_fitness_idx = np.where(self.fitness == np.max(self.fitness))[0][0]
            parents[i, :] = population[max_fitness_idx, :]
            self.fitness[max_fitness_idx] = -99999999999

        self.parents = parents
        return parents

    def crossover(self, offspring_size):

        offspring = np.empty(offspring_size)
        crossover_point = np.uint8(offspring_size[1] / 2)

        for k in range(offspring_size[0]):
            parent1_idx = k % self.parents.shape[0]
            parent2_idx = (k + 1) % self.parents.shape[0]
            offspring[k, 0:crossover_point] = self.parents[parent1_idx, 0:crossover_point]
            offspring[k, crossover_point:] = self.parents[parent2_idx, crossover_point:]

        self.offspring = offspring
        return offspring



    def mutation(self):
        crossover = self.offspring

        for i in range(crossover.shape[0]):
            random_value = np.random.uniform(-1.0, 1.0, 1)
            crossover[i, Constant.PARENT_MATING_COUNT] = crossover[i, Constant.PARENT_MATING_COUNT] + random_value

        return crossover
