import random
import utilityFunctions
from deap import base
from deap import creator
from deap import tools
import individual
from os import listdir
from os.path import isfile, join
import configparser

only_files = [f for f in listdir("configurations") if isfile(join("configurations", f))]


def get_best(population):
    objective_fitness_list = list(map(toolbox.get_objective_fitness, population))
    objective_fitness_list = sorted(objective_fitness_list)
    return objective_fitness_list[-1]


for a_file in only_files:
    if a_file != 'testing_file.ini':
        config = configparser.ConfigParser()
        config.sections()
        config.read("configurations/" + a_file)

        NUM_SPECIES = int(config["DEFAULT"]["NUM_SPECIES"])
        SPECIES_SIZE = int(config["DEFAULT"]["SPECIES_SIZE"])
        IND_SIZE = int(config["DEFAULT"]["IND_SIZE"])
        SAMPLE_SIZE = int(config["DEFAULT"]["SAMPLE_SIZE"])
        NUM_DIMENSIONS = int(config["DEFAULT"]["NUM_DIMENSIONS"])
        TIMES_RUN = int(config["DEFAULT"]["TIMES_RUN"])
        MUTATION_RATE = float(config["DEFAULT"]["MUTATION_RATE"])
        BIT_FLIP_PROBABILITY = float(config["DEFAULT"]["BIT_FLIP_PROBABILITY"])
        ALGORITHM = int(config["DEFAULT"]["ALGORITHM"])

        # Activators for meta mutation
        # mutate sample size
        MUTATE_SS_BOOL = int(config["META_EVOLUTION"]["MUTATE_SS_BOOL"])
        META_SAMPLE_SIZE_PROBABILITY = float(config["META_EVOLUTION"]["META_SAMPLE_SIZE_PROBABILITY"])
        META_SAMPLE_SIZE_MEAN = float(config["META_EVOLUTION"]["META_SAMPLE_SIZE_MEAN"])
        META_SAMPLE_SIZE_SD = float(config["META_EVOLUTION"]["META_SAMPLE_SIZE_SD"])

        # mutate mutation rate
        MUTATE_MR_BOOL = int(config["META_EVOLUTION"]["MUTATE_MR_BOOL"])
        META_MUTATION_PROBABILITY = float(config["META_EVOLUTION"]["META_MUTATION_PROBABILITY"])
        META_MUTATION_MEAN = float(config["META_EVOLUTION"]["META_MUTATION_MEAN"])
        META_MUTATION_SD = float(config["META_EVOLUTION"]["META_MUTATION_SD"])

        # mutate bit flip rate
        MUTATE_BF_BOOL = int(config["META_EVOLUTION"]["MUTATE_BF_BOOL"])
        META_BIT_FLIP_PROBABILITY = float(config["META_EVOLUTION"]["META_BIT_FLIP_PROBABILITY"])
        META_BIT_FLIP_MEAN = float(config["META_EVOLUTION"]["META_BIT_FLIP_MEAN"])
        META_BIT_FLIP_SD = float(config["META_EVOLUTION"]["META_BIT_FLIP_SD"])

        creator.create("FitnessMax", base.Fitness, weights=(1.0,))

        toolbox = base.Toolbox()


        def create_individual():
            return individual.Individual(mutation_rate=MUTATION_RATE, sample_size=SAMPLE_SIZE,
                                         num_dimensions=NUM_DIMENSIONS, ind_size=IND_SIZE,
                                         bit_flip_probability=BIT_FLIP_PROBABILITY,
                                         sample_size_mutation_probability=META_SAMPLE_SIZE_PROBABILITY,
                                         mutation_rate_mutation_probability=META_MUTATION_PROBABILITY,
                                         bit_flip_mutation_probability=META_BIT_FLIP_PROBABILITY,
                                         mutation_rate_mu=META_MUTATION_MEAN, mutation_rate_sigma=META_MUTATION_SD,
                                         sample_size_mu=META_SAMPLE_SIZE_MEAN, sample_size_sigma=META_SAMPLE_SIZE_SD,
                                         bit_flip_mu=META_BIT_FLIP_MEAN, bit_flip_sigma=META_BIT_FLIP_SD)


        def calculate_meta_mutation_chance(an_individual):
            return sum(an_individual),


        def calculate_fitness(an_individual):
            if NUM_DIMENSIONS == 1:
                total = 0
                for bit in an_individual.bits:
                    if bit:
                        total += 1
                return total
            else:
                total = 0
                for bit in an_individual:
                    if bit:
                        total += 1
                return total


        # Runs algorithm one where
        # each member of the population is compared
        # against the other in only a single dimension
        def algorithm_one(an_individual, pop):
            if NUM_DIMENSIONS != 1 or IND_SIZE != 100:
                exit("Algorithm requires 1 dimensions with an individual size of 100")

            if pop == 1:
                competition = random.sample(population_two, k=an_individual.sample_size)
            else:
                competition = random.sample(population_one, k=an_individual.sample_size)

            # Compute the subjective fitness using algorithm one
            total = 0
            for competitor in competition:
                if calculate_fitness(an_individual) > calculate_fitness(competitor):
                    total += 1
            return total + 0.0001,


        # Runs algorithm two where
        # each member of the population is compared
        # based on the dimension that is the most different.
        def algorithm_two(an_individual, pop):
            if NUM_DIMENSIONS != 10 or IND_SIZE != 10:
                exit("Algorithm requires 10 dimensions with an individual size of 10")

            if pop == 1:
                competition = random.sample(population_two, k=an_individual.sample_size)
            else:
                competition = random.sample(population_one, k=an_individual.sample_size)

            # Compute the subjective fitness using algorithm two
            total = 0

            for competitor in competition:
                greatest_difference_index = 0
                greatest_difference = 0
                for dimension in range(len(competitor.bits)):
                    difference = abs(
                        calculate_fitness(an_individual.bits[dimension]) - calculate_fitness(
                            competitor.bits[dimension]))
                    if difference > greatest_difference:
                        greatest_difference_index = dimension
                        greatest_difference = difference
                if calculate_fitness(an_individual.bits[greatest_difference_index]) > calculate_fitness(
                        competitor.bits[greatest_difference_index]):
                    total += 1

            return total + 0.0001,


        # Runs algorithm three where
        # each member of the population is compared
        # based on the dimension that is closest
        # in similarity.
        def algorithm_three(an_individual, pop):
            if NUM_DIMENSIONS != 10 or IND_SIZE != 10:
                exit("Algorithm requires 10 dimensions with an individual size of 10")

            if pop == 1:
                competition = random.sample(population_two, k=an_individual.sample_size)
            else:
                competition = random.sample(population_one, k=an_individual.sample_size)

            # Compute the subjective fitness using algorithm three
            total = 0

            for competitor in competition:
                smallest_difference_index = 0
                smallest_difference = 100
                for dimension in range(len(competitor.bits)):
                    difference = abs(
                        calculate_fitness(an_individual.bits[dimension]) - calculate_fitness(
                            competitor.bits[dimension]))
                    if difference < smallest_difference:
                        smallest_difference_index = dimension
                        smallest_difference = difference
                if calculate_fitness(an_individual.bits[smallest_difference_index]) > calculate_fitness(
                        competitor.bits[smallest_difference_index]):
                    total += 1

            return total,


        # Returns the objective fitness of the individual.
        def get_objective_fitness(an_individual):
            if NUM_DIMENSIONS == 1:
                return sum(an_individual[0]),
            else:
                total = 0
                for dimension in an_individual.bits:
                    total += sum(dimension)
                return total


        # Returns the objective fitness of the individual for printing to file.
        def get_objective_fitness_no_comma(an_individual):
            if NUM_DIMENSIONS == 1:
                return sum(an_individual.bits)
            else:
                total = 0
                for dimension in an_individual.bits:
                    total += sum(dimension)
                return total


        def get_mutation_rate(an_individual):
            return an_individual.mutation_rate


        def get_bit_flip(an_individual):
            return an_individual.bit_flip_probability

        def get_sample_size(an_individual):
            return an_individual.sample_size


        # toolbox.register("bit", individual.Individual.generate_bits, NUM_DIMENSIONS, IND_SIZE)
        toolbox.register("individual", create_individual)
        toolbox.register("species", tools.initRepeat, list, toolbox.individual, SPECIES_SIZE)
        toolbox.register("mutate", individual.Individual.mutate_bit_flip)
        toolbox.register("meta_mutate", individual.Individual.meta_mutate)
        toolbox.register("meta_meta_mutate", individual.Individual.meta_mutate_meta_mutation_parameters)
        toolbox.register("select", tools.selTournament, tournsize=5)
        toolbox.register("get_best", tools.selBest, k=1)
        # toolbox.register("evaluate", getObjectiveFitness)
        if ALGORITHM == 1:
            toolbox.register("evaluate", algorithm_one)
        elif ALGORITHM == 2:
            toolbox.register("evaluate", algorithm_two)
        elif ALGORITHM == 3:
            toolbox.register("evaluate", algorithm_three)
        else:
            exit("Algorithm not defined")

        toolbox.register("get_objective_fitness", get_objective_fitness_no_comma)
        toolbox.register("get_mutation_rate", get_mutation_rate)
        toolbox.register("get_bit_flip", get_bit_flip)
        toolbox.register("get_sample_size", get_sample_size)


        def main(runs=1):
            for run in range(runs):
                best_of_pop_one = []
                best_of_pop_two = []
                number_of_generations = 2000
                global population_one
                global population_two
                global SAMPLE_SIZE

                # Create two species containing 25 members each
                species = [toolbox.species() for _ in range(NUM_SPECIES)]

                population_one = species[0]
                population_two = species[1]

                # Evaluate the first population
                fitnesses = list(map(toolbox.evaluate, population_one, [random.randint(1, 1) for _ in range(100)]))
                for ind, fit in zip(population_one, fitnesses):
                    ind.fitness = fit

                # Evaluate the second population
                fitnesses = list(map(toolbox.evaluate, population_two, [random.randint(2, 2) for _ in range(100)]))
                for ind, fit in zip(population_two, fitnesses):
                    ind.fitness = fit

                # Variable keeping track of the number of generations
                g = 0

                # Begin the evolution
                while g < number_of_generations:
                    # Select the next generation individuals
                    offspring_one = toolbox.select(population_one, len(population_one))
                    # Select the next generation individuals
                    offspring_two = toolbox.select(population_two, len(population_two))
                    # Clone the selected individuals
                    offspring_one = list(map(toolbox.clone, offspring_one))
                    offspring_two = list(map(toolbox.clone, offspring_two))

                    # Apply crossover and mutation on the offspring
                    for child1, child2 in zip(offspring_one[::2], offspring_one[1::2]):
                        # toolbox.mate(child1, child2)
                        if child1.fitness > child2.fitness:
                            child2 = child1
                        else:
                            child1 = child2
                        child1.fitness = 0
                        child2.fitness = 0

                    for child1, child2 in zip(offspring_two[::2], offspring_two[1::2]):
                        # toolbox.mate(child1, child2)
                        if child1.fitness > child2.fitness:
                            child2 = child1
                        else:
                            child1 = child2
                        child1.fitness = 0
                        child2.fitness = 0

                    for mutant in offspring_one:
                        if random.random() < MUTATION_RATE:
                            toolbox.mutate(mutant)
                            mutant.fitness = 0

                    for mutant in offspring_two:
                        if random.random() < MUTATION_RATE:
                            toolbox.mutate(mutant)
                            mutant.fitness = 0

                    # Evaluate the first population
                    fitnesses = list(map(toolbox.evaluate, offspring_one, [random.randint(1, 1) for _ in range(100)]))
                    # fitnesses = list(map(toolbox.evaluate, offspring_one))
                    for ind, fit in zip(offspring_one, fitnesses):
                        ind.fitness = fit

                    # Evaluate the second population
                    fitnesses = list(map(toolbox.evaluate, offspring_two, [random.randint(2, 2) for _ in range(100)]))
                    # fitnesses = list(map(toolbox.evaluate, offspring_two))
                    for ind, fit in zip(offspring_two, fitnesses):
                        ind.fitness = fit

                    population_one[:] = offspring_one
                    population_two[:] = offspring_two

                    # Gather all the fitnesses in one list and print the stats
                    fits_one = [ind.fitness[0] for ind in population_one]
                    fits_two = [ind.fitness[0] for ind in population_two]

                    objective_fitness_one = list(map(toolbox.get_objective_fitness, population_one))
                    objective_fitness_two = list(map(toolbox.get_objective_fitness, population_two))
                    mutation_rate_one = list(map(toolbox.get_mutation_rate, population_one))
                    mutation_rate_two = list(map(toolbox.get_mutation_rate, population_two))
                    bit_flip_one = list(map(toolbox.get_bit_flip, population_one))
                    bit_flip_two = list(map(toolbox.get_bit_flip, population_two))
                    #
                    utilityFunctions.write_objective_fitness(a_file.replace('.ini', ''), objective_fitness_one,
                                                             objective_fitness_two, g, run)
                    utilityFunctions.write_mutation_rate(a_file.replace('.ini', ''), mutation_rate_one,
                                                         mutation_rate_two, g, run)
                    utilityFunctions.write_bit_flip_rate(a_file.replace('.ini', ''), bit_flip_one,
                                                         bit_flip_two, g, run)

                    if MUTATE_SS_BOOL:
                        sample_size_one = list(map(toolbox.get_sample_size, population_one))
                        sample_size_two = list(map(toolbox.get_sample_size, population_two))
                        utilityFunctions.write_sample_size(a_file.replace('.ini', ''), g, run, sample_size_one, sample_size_two)
                    else:
                        utilityFunctions.write_subjective_fitness(a_file.replace('.ini', ''), fits_one, fits_two, g,
                                                                  run,
                                                                  SAMPLE_SIZE)

                    # meta mutate

                    if g % 25 == 0:
                        for mutant in population_one:
                            toolbox.meta_mutate(mutant, MUTATE_SS_BOOL, MUTATE_MR_BOOL, MUTATE_BF_BOOL)

                        for mutant in population_two:
                            toolbox.meta_mutate(mutant, MUTATE_SS_BOOL, MUTATE_MR_BOOL, MUTATE_BF_BOOL)

                    if g % 50 == 0:
                        for mutant in population_one:
                            toolbox.meta_meta_mutate(mutant)

                        for mutant in population_two:
                            toolbox.meta_meta_mutate(mutant)

                    g = g + 1

                    best_of_pop_one.append(get_best(population_one))
                    best_of_pop_two.append(get_best(population_two))

                utilityFunctions.create_ciao_graphs(best_of_pop_one, best_of_pop_two, a_file.replace('.ini', ''),
                                                    run)


        main(TIMES_RUN)
        utilityFunctions.print_objective_fitness(a_file.replace('.ini', ''), TIMES_RUN, IND_SIZE, NUM_DIMENSIONS)

        if not MUTATE_SS_BOOL:
            utilityFunctions.print_subjective_fitness(a_file.replace('.ini', ''), TIMES_RUN)
