import numpy as np
from constants import Constant
from genetic import Genetic
from matplotlib import pyplot



inputs = Constant.EQUATION_INPUTS

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

        parents = genetic.getMating(init_population, Constant.PARENT_MATING_COUNT)

        crossover = genetic.crossover(offspring_size=(population_size[0] - parents.shape[0], length))
        print("Crossover", crossover)

        mutation = genetic.mutation()
        print("Mutation", mutation)

        # Creating the init population based on the parents and offspring.
        init_population[0:parents.shape[0], :] = parents
        init_population[parents.shape[0]:, :] = mutation



    fitness = genetic.calcFitness(inputs, init_population)

    best_match_idx = np.where(fitness == np.max(fitness))

    print("Best solution : ", init_population[best_match_idx, :])
    print("Best solution fitness : ", fitness[best_match_idx])



    pyplot.plot(best_outputs)
    pyplot.xlabel("Iteration")
    pyplot.ylabel("Fitness")
    pyplot.show()



