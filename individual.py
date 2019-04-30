import random


class Individual:
    def __init__(self, mutation_rate, sample_size, num_dimensions, ind_size, bit_flip_probability,
                 sample_size_mutation_probability, mutation_rate_mutation_probability, bit_flip_mutation_probability,
                 sample_size_mu, sample_size_sigma,
                 mutation_rate_mu, mutation_rate_sigma,
                 bit_flip_mu, bit_flip_sigma):
        self.fitness = None
        self.mutation_rate = mutation_rate
        self.sample_size = sample_size
        self.bits = []
        self.num_dimensions = num_dimensions
        self.ind_size = ind_size
        self.bit_flip_probability = bit_flip_probability
        self.objective_fitness = 0
        self.sample_size_mutation_probability = sample_size_mutation_probability
        self.sample_size_mu = sample_size_mu
        self.sample_size_sigma = sample_size_sigma
        self.mutation_rate_mutation_probability = mutation_rate_mutation_probability
        self.mutation_rate_mu = mutation_rate_mu
        self.mutation_rate_sigma = mutation_rate_sigma
        self.mutation_rate_meta_sigma = random.random()
        self.bit_flip_mutation_probability = bit_flip_mutation_probability
        self.bit_flip_mu = bit_flip_mu
        self.bit_flip_sigma = bit_flip_sigma
        self.generate_bits()

    #
    # Initialise all bits to 0 inside a given size.
    #
    def generate_bits(self):
        if self.num_dimensions > 1:
            bits = []
            for dimension in range(self.num_dimensions):
                individual_inner = []
                for ind in range(self.ind_size):
                    individual_inner.append(random.randint(0, 0))
                bits.append(individual_inner)
            self.bits = bits
        else:
            bits = []
            for ind in range(self.ind_size):
                bits.append(random.randint(0, 0))
            self.bits = bits

    #
    # Mutates a bit with a given probability defined as self.mutation_rate
    #
    def mutate_bit_flip(self):
        if self.num_dimensions > 1:
            for dimension in range(len(self.bits)):
                for bit in range(len(self.bits[dimension])):
                    if random.random() < self.bit_flip_probability:
                        if self.bits[dimension][bit] == 0:
                            self.bits[dimension][bit] = 1
                        else:
                            self.bits[dimension][bit] = 0
        else:
            for bit in range(len(self.bits)):
                if random.random() < self.bit_flip_probability:
                    if self.bits[bit] == 0:
                        self.bits[bit] = 1
                    else:
                        self.bits[bit] = 0

    #
    # meta mutate function for selected features
    #
    def meta_mutate(self, mutate_ss_bool, mutate_mr_bool, mutate_bf_bool):
        # if enabled, mutate the number of individuals that are competed with according to a normal distribution.
        if mutate_ss_bool:
            if random.random() <= self.sample_size_mutation_probability:
                self.sample_size += random.gauss(self.sample_size_mu, self.sample_size_sigma)
                self.sample_size = self.sample_size.__round__()
                if self.sample_size < 1:
                    self.sample_size = 1
                elif self.sample_size > 25:
                    self.sample_size = 25
        # if enabled, mutate the mutation rate according to a normal distribution.
        if mutate_mr_bool:
            if random.random() <= self.mutation_rate_mutation_probability:
                self.mutation_rate += random.gauss(self.mutation_rate_mu, self.mutation_rate_sigma)
            if self.mutation_rate < 0:
                self.mutation_rate = 0
            elif self.mutation_rate > 1:
                self.mutation_rate = 1
        # if enabled, mutate the bit flip mutation probability according to a normal distribution.
        if mutate_bf_bool:
            if random.random() <= self.bit_flip_mutation_probability:
                self.bit_flip_probability += random.gauss(self.bit_flip_mu, self.bit_flip_sigma)
            if self.bit_flip_probability < 0:
                self.bit_flip_probability = 0
            elif self.bit_flip_probability > 1:
                self.bit_flip_probability = 1

    #
    # meta mutate function for selected features
    #
    def meta_mutate_meta_mutation_parameters(self):
        # if enabled, mutate the number of individuals that are competed with according to a normal distribution.

        self.sample_size_mutation_probability += random.gauss(0, 0.05)
        self.sample_size_sigma += random.gauss(0, 1)

        if self.sample_size_sigma < 0:
            self.sample_size_sigma = 0

        if self.sample_size_mutation_probability < 0:
            self.sample_size_mutation_probability = 0
        elif self.sample_size_mutation_probability > 1:
            self.sample_size_mutation_probability = 1

        self.mutation_rate_mutation_probability += random.gauss(0, 0.05)
        self.mutation_rate_sigma += random.gauss(0, 0.05)

        if self.mutation_rate_sigma < 0:
            self.mutation_rate_sigma = 0
        elif self.mutation_rate_sigma > 1:
            self.mutation_rate_sigma = 1

        if self.mutation_rate_mutation_probability < 0:
            self.mutation_rate_mutation_probability = 0
        elif self.mutation_rate_mutation_probability > 1:
            self.mutation_rate_mutation_probability = 1

