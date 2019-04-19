import numpy as np
from constants import Constant


class Genetic:

    def __init__(self):
        self.fitness = None
        pass

    def calcFitness(self, inputs, population):
        self.fitness = np.sum(population * inputs, axis=1)
        return self.fitness


