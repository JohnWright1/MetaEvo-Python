import unittest
import individual
import configparser


class TestSum(unittest.TestCase):

    def setUp(self):
        config = configparser.ConfigParser()
        config.sections()
        config.read("configurations/testing_file.ini")

        NUM_SPECIES = int(config["DEFAULT"]["NUM_SPECIES"])
        SPECIES_SIZE = int(config["DEFAULT"]["SPECIES_SIZE"])
        IND_SIZE = int(config["DEFAULT"]["IND_SIZE"])
        self.SAMPLE_SIZE = int(config["DEFAULT"]["SAMPLE_SIZE"])
        NUM_DIMENSIONS = int(config["DEFAULT"]["NUM_DIMENSIONS"])
        TIMES_RUN = int(config["DEFAULT"]["TIMES_RUN"])
        self.MUTATION_RATE = float(config["DEFAULT"]["MUTATION_RATE"])
        self.BIT_FLIP_PROBABILITY = float(config["DEFAULT"]["BIT_FLIP_PROBABILITY"])
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

        self.my_individual = individual.Individual(mutation_rate=self.MUTATION_RATE, sample_size=self.SAMPLE_SIZE,
                                                   num_dimensions=NUM_DIMENSIONS, ind_size=IND_SIZE,
                                                   bit_flip_probability=self.BIT_FLIP_PROBABILITY,
                                                   sample_size_mutation_probability=META_SAMPLE_SIZE_PROBABILITY,
                                                   mutation_rate_mutation_probability=META_MUTATION_PROBABILITY,
                                                   bit_flip_mutation_probability=META_BIT_FLIP_PROBABILITY,
                                                   mutation_rate_mu=META_MUTATION_MEAN,
                                                   mutation_rate_sigma=META_MUTATION_SD,
                                                   sample_size_mu=META_SAMPLE_SIZE_MEAN,
                                                   sample_size_sigma=META_SAMPLE_SIZE_SD,
                                                   bit_flip_mu=META_BIT_FLIP_MEAN, bit_flip_sigma=META_BIT_FLIP_SD)

    def test_meta_mutation_on_sample_size(self):
        self.my_individual.meta_mutate(1, 0, 0)
        self.assertNotEqual(self.my_individual.sample_size, self.SAMPLE_SIZE,
                            'Test should result in a different sample size')
        # print(self.my_individual.sample_size)
        # print(self.SAMPLE_SIZE)

    def test_meta_mutation_on_mutation_rate(self):
        self.my_individual.meta_mutate(0, 1, 0)
        self.assertNotEqual(self.my_individual.mutation_rate, self.MUTATION_RATE)
        # print(self.my_individual.mutation_rate)
        # print(self.MUTATION_RATE)

    def test_meta_mutation_on_bit_flip_rate(self):
        self.my_individual.meta_mutate(0, 0, 1)
        self.assertNotEqual(self.my_individual.bit_flip_probability, self.BIT_FLIP_PROBABILITY)
        # print(self.my_individual.bit_flip_probability)
        # print(self.BIT_FLIP_PROBABILITY)

    def test_self_mutation_on_sample_size(self):
        print("Sample Size Before: " + str(self.my_individual.sample_size_sigma))
        print("Sample Mutation Rate Before: " + str(self.my_individual.sample_size_mutation_probability))
        print("Mutation Rate Before: " + str(self.my_individual.mutation_rate_sigma))
        print("Mutation Mutation Rate Before: " + str(self.my_individual.mutation_rate_mutation_probability))
        self.my_individual.meta_mutate_meta_mutation_parameters()
        print("Sample Size After: " + str(self.my_individual.sample_size_sigma))
        print("Sample Mutation Rate After: " + str(self.my_individual.sample_size_mutation_probability))
        print("Mutation Rate After: " + str(self.my_individual.mutation_rate_sigma))
        print("Mutation Mutation Rate After: " + str(self.my_individual.mutation_rate_mutation_probability))
        # self.assertNotEqual(self.my_individual.sample_size, self.SAMPLE_SIZE,
        #                     'Test should result in a different sample size')
        # print(self.my_individual.sample_size)
        # print(self.SAMPLE_SIZE)


if __name__ == '__main__':
    unittest.main()
