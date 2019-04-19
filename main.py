import numpy as np
from constants import Constant
from genetic import Genetic



inputs = np.array([4, -2, 3.5, 5, -11, -4.7])

length = len(inputs)

solution_count = Constant.SOLUTION_COUNT

population_size = (solution_count, length) #(8, 6)

best_outputs = []



if __name__ == "__main__":


    genetic = Genetic()


    #Make initial population 8 chromosomes and 6 genes
    init_population = np.random.uniform(-4, 4, size=population_size)
    print(init_population)

    for generation in range(Constant.GENERATION_COUNT):

        print("Generation : {}" . format(generation))

        fitness = genetic.calcFitness(inputs, init_population)
        print("fitness", fitness)

        best_outputs.append(np.max(fitness))
        print(best_outputs)

        
