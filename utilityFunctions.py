import matplotlib.pyplot as plt
import matplotlib


def write_subjective_fitness(config_run, pop_one, pop_two, gen, run, sample_size):
    pop_one_file = open('results/' + str(config_run) + '/subjective/avg_pop_one_' + str(run) + '.csv', 'a')
    pop_two_file = open('results/' + str(config_run) + '/subjective/avg_pop_two_' + str(run) + '.csv', 'a')

    length = len(pop_one)
    mean = sum(pop_one) / length

    pop_one_file.write(str(gen) + ',')
    pop_one_file.writelines(str(mean / sample_size))
    pop_one_file.writelines('\n')
    pop_one_file.close()

    length = len(pop_two)
    mean = sum(pop_two) / length

    pop_two_file.write(str(gen) + ',')
    pop_two_file.write(str(mean / sample_size))
    pop_two_file.writelines('\n')
    pop_two_file.close()

    for i in range(len(pop_one)):
        pop_one_file = open('results/' + str(config_run) + '/subjective/pop_one_' + str(run) + '.csv', 'a')
        pop_two_file = open('results/' + str(config_run) + '/subjective/pop_two_' + str(run) + '.csv', 'a')

        pop_one_file.write(str(gen) + ',')
        pop_one_file.writelines(str(pop_one[i] / sample_size))
        pop_one_file.writelines('\n')
        pop_one_file.close()

        pop_two_file.write(str(gen) + ',')
        pop_two_file.write(str(pop_two[i] / sample_size))
        pop_two_file.writelines('\n')
        pop_two_file.close()


def write_sample_size(config_run, gen, run, sample_size_pop_one, sample_size_pop_two):
    pop_one_file = open('results/' + str(config_run) + '/sample_size/avg_pop_one_' + str(run) + '.csv', 'a')
    pop_two_file = open('results/' + str(config_run) + '/sample_size/avg_pop_two_' + str(run) + '.csv', 'a')

    length = len(sample_size_pop_one)
    mean = sum(sample_size_pop_one) / length

    pop_one_file.write(str(gen) + ',')
    pop_one_file.writelines(str(mean))
    pop_one_file.writelines('\n')
    pop_one_file.close()

    length = len(sample_size_pop_two)
    mean = sum(sample_size_pop_two) / length

    pop_two_file.write(str(gen) + ',')
    pop_two_file.write(str(mean))
    pop_two_file.writelines('\n')
    pop_two_file.close()

    for i in range(len(sample_size_pop_one)):
        pop_one_file = open('results/' + str(config_run) + '/sample_size/pop_one_' + str(run) + '.csv', 'a')
        pop_two_file = open('results/' + str(config_run) + '/sample_size/pop_two_' + str(run) + '.csv', 'a')

        pop_one_file.write(str(gen) + ',')
        pop_one_file.writelines(str(sample_size_pop_one[i]))
        pop_one_file.writelines('\n')
        pop_one_file.close()

        pop_two_file.write(str(gen) + ',')
        pop_two_file.write(str(sample_size_pop_two[i]))
        pop_two_file.writelines('\n')
        pop_two_file.close()


def write_objective_fitness(config_run, pop_one, pop_two, gen, run):
    pop_one_file = open('results/' + str(config_run) + '/objective/avg_pop_one_' + str(run) + '.csv', 'a')
    pop_two_file = open('results/' + str(config_run) + '/objective/avg_pop_two_' + str(run) + '.csv', 'a')

    length = len(pop_one)
    mean = sum(pop_one) / length

    pop_one_file.write(str(gen) + ',')
    pop_one_file.writelines(str(mean))
    pop_one_file.writelines('\n')
    pop_one_file.close()

    length = len(pop_two)
    mean = sum(pop_two) / length

    pop_two_file.write(str(gen) + ',')
    pop_two_file.write(str(mean))
    pop_two_file.writelines('\n')
    pop_two_file.close()

    for i in range(len(pop_one)):
        pop_one_file = open('results/' + str(config_run) + '/objective/pop_one_' + str(run) + '.csv', 'a')
        pop_two_file = open('results/' + str(config_run) + '/objective/pop_two_' + str(run) + '.csv', 'a')

        pop_one_file.write(str(gen) + ',')
        pop_one_file.writelines(str(pop_one[i]))
        # pop_one_file.writelines(str(mean))
        pop_one_file.writelines('\n')
        pop_one_file.close()

        pop_two_file.write(str(gen) + ',')
        pop_two_file.write(str(pop_two[i]))
        # pop_two_file.write(str(mean))
        pop_two_file.writelines('\n')
        pop_two_file.close()


def write_mutation_rate(config_run, pop_one, pop_two, gen, run):
    pop_one_file = open('results/' + str(config_run) + '/mutation_rate/avg_pop_one_' + str(run) + '.csv', 'a')
    pop_two_file = open('results/' + str(config_run) + '/mutation_rate/avg_pop_two_' + str(run) + '.csv', 'a')

    length = len(pop_one)
    mean = sum(pop_one) / length

    pop_one_file.write(str(gen) + ',')
    pop_one_file.writelines(str(mean))
    pop_one_file.writelines('\n')
    pop_one_file.close()

    length = len(pop_two)
    mean = sum(pop_two) / length

    pop_two_file.write(str(gen) + ',')
    pop_two_file.write(str(mean))
    pop_two_file.writelines('\n')
    pop_two_file.close()

    for i in range(len(pop_one)):
        pop_one_file = open('results/' + str(config_run) + '/mutation_rate/pop_one_' + str(run) + '.csv', 'a')
        pop_two_file = open('results/' + str(config_run) + '/mutation_rate/pop_two_' + str(run) + '.csv', 'a')

        pop_one_file.write(str(gen) + ',')
        pop_one_file.writelines(str(pop_one[i]))
        # pop_one_file.writelines(str(mean))
        pop_one_file.writelines('\n')
        pop_one_file.close()

        pop_two_file.write(str(gen) + ',')
        pop_two_file.write(str(pop_two[i]))
        # pop_two_file.write(str(mean))
        pop_two_file.writelines('\n')
        pop_two_file.close()


def write_bit_flip_rate(config_run, pop_one, pop_two, gen, run):
    pop_one_file = open('results/' + str(config_run) + '/bit_flip/avg_pop_one_' + str(run) + '.csv', 'a')
    pop_two_file = open('results/' + str(config_run) + '/bit_flip/avg_pop_two_' + str(run) + '.csv', 'a')

    length = len(pop_one)
    mean = sum(pop_one) / length

    pop_one_file.write(str(gen) + ',')
    pop_one_file.writelines(str(mean))
    pop_one_file.writelines('\n')
    pop_one_file.close()

    length = len(pop_two)
    mean = sum(pop_two) / length

    pop_two_file.write(str(gen) + ',')
    pop_two_file.write(str(mean))
    pop_two_file.writelines('\n')
    pop_two_file.close()

    for i in range(len(pop_one)):
        pop_one_file = open('results/' + str(config_run) + '/mutation_rate/pop_one_' + str(run) + '.csv', 'a')
        pop_two_file = open('results/' + str(config_run) + '/mutation_rate/pop_two_' + str(run) + '.csv', 'a')

        pop_one_file.write(str(gen) + ',')
        pop_one_file.writelines(str(pop_one[i]))
        # pop_one_file.writelines(str(mean))
        pop_one_file.writelines('\n')
        pop_one_file.close()

        pop_two_file.write(str(gen) + ',')
        pop_two_file.write(str(pop_two[i]))
        # pop_two_file.write(str(mean))
        pop_two_file.writelines('\n')
        pop_two_file.close()


def print_objective_fitness(config_run, runs, ind_size, num_dimensions):
    for run in range(runs):
        file_one = open('results/' + str(config_run) + '/objective/avg_pop_one_' + str(run) + '.csv')
        file_two = open('results/' + str(config_run) + '/objective/avg_pop_two_' + str(run) + '.csv')

        fileOneContents = file_one.readlines()
        fileTwoContents = file_two.readlines()

        file_one.close()
        file_two.close()

        x1 = []
        x2 = []
        y1 = []
        y2 = []

        for i in range(len(fileOneContents)):
            line = fileOneContents[i].replace('\n', '').split(',')
            x1.append(int(line[0]))
            y1.append(float((line[1])))

        for i in range(len(fileTwoContents)):
            line = fileTwoContents[i].replace('\n', '').split(',')
            x2.append(int(line[0]))
            y2.append(float((line[1])))

        axes = plt.gca()
        axes.set_xlim([0, 2000])
        axes.set_xlabel("Generation")
        axes.set_ylim([0, ind_size * num_dimensions])
        axes.set_ylabel("Objective Fitness")
        # axes.set_title("Algorithm 3")
        plt.scatter(x1, y1, s=2, c='blue', alpha=1, label="Population 1")
        plt.scatter(x2, y2, s=2, c='orange', alpha=1, label="Population 2")
        plt.legend(loc="lower right")
        plt.savefig("results/" + str(config_run) + "/graphs/run_" + str(run + 1) + "_objective")
        # plt.show()
        plt.clf()
        plt.cla()
        plt.close()


def print_subjective_fitness(config_run, runs):
    for run in range(runs):
        file_one = open('results/' + str(config_run) + '/subjective/avg_pop_one_' + str(run) + '.csv')
        file_two = open('results/' + str(config_run) + '/subjective/avg_pop_two_' + str(run) + '.csv')

        fileOneContents = file_one.readlines()
        fileTwoContents = file_two.readlines()

        file_one.close()
        file_two.close()

        x1 = []
        x2 = []
        y1 = []
        y2 = []

        for i in range(len(fileOneContents)):
            line = fileOneContents[i].replace('\n', '').split(',')
            x1.append(int(line[0]))
            y1.append(float((line[1])))

        for i in range(len(fileTwoContents)):
            line = fileTwoContents[i].replace('\n', '').split(',')
            x2.append(int(line[0]))
            y2.append(float((line[1])))

        plt.subplot(211)
        axes = plt.gca()
        axes.set_xlim([0, 2000])
        axes.set_ylim([0, 1])
        axes.set_ylabel("Subjective Fitness")
        plt.scatter(x1, y1, s=2, c='blue', alpha=1)
        plt.subplot(212)
        axes = plt.gca()
        axes.set_xlim([0, 2000])
        axes.set_xlabel("Generation")
        axes.set_ylim([0, 1])
        axes.set_ylabel("Subjective Fitness")
        plt.scatter(x2, y2, s=2, c='orange', alpha=1)
        plt.savefig("results/" + str(config_run) + "/graphs/run_" + str(run + 1) + "_subjective")
        # plt.show()
        plt.clf()
        plt.cla()
        plt.close()


def create_ciao_graphs(population_one, population_two, config_run, run):
    x = 0
    x_values = []
    x2_values = []
    y = 0
    y_values = []
    y2_values = []
    z_values = []
    z2_values = []

    for ind_one in population_one:
        y = 0
        for ind_two in population_two:
            if x <= y:
                if ind_one >= ind_two:
                    x_values.append(x)
                    y_values.append(y)
                    z_values.append((ind_one - ind_two))
                elif ind_one <= ind_two:
                    x2_values.append(x)
                    y2_values.append(y)
                    z2_values.append((ind_two - ind_one))
            y += 1
        x += 1

    axes = plt.gca()
    axes.set_xlim([0, 2000])
    axes.set_xlabel("Population 1")
    axes.set_ylim([0, 2000])
    axes.set_ylabel("Population 2")
    axes.xaxis.tick_top()
    axes.xaxis.set_label_position('top')
    # Hide the right and bottom spines
    axes.spines['right'].set_visible(False)
    axes.spines['bottom'].set_visible(False)
    # axes.set_title("Algorithm 3")
    colormap = plt.cm.Greys  # or any other colormap
    normalize = matplotlib.colors.Normalize()
    plt.scatter(x_values, y_values, c=z_values, s=2, cmap=colormap, norm=normalize, marker='*')
    # plt.scatter(x_black_values, y_black_values, s=0.5, c='black', alpha=1, label="difference greater than 10")
    # plt.scatter(x_dark_grey_values, y_dark_grey_values, s=0.5, c='#A9A9A9', alpha=0.6,
    #             label="difference greater than 5")
    # plt.scatter(x_grey_values, y_grey_values, s=0.5, c='#DCDCDC', alpha=0.3, label="difference greater than 0")
    # plt.legend(loc="lower right")
    plt.savefig("results/" + str(config_run) + "/CIAO_graphs/run_" + str(run + 1))
    # plt.show()
    plt.clf()
    plt.cla()
    plt.close()

    axes = plt.gca()
    axes.set_xlim([0, 1000])
    axes.set_xlabel("Population 1")
    axes.set_ylim([0, 1000])
    axes.set_ylabel("Population 2")
    axes.xaxis.tick_top()
    axes.xaxis.set_label_position('top')
    # Hide the right and bottom spines
    axes.spines['right'].set_visible(False)
    axes.spines['bottom'].set_visible(False)
    # axes.set_title("Algorithm 3")
    colormap = plt.cm.Greys  # or any other colormap
    normalize = matplotlib.colors.Normalize()
    plt.scatter(x2_values, y2_values, c=z2_values, s=2, cmap=colormap, norm=normalize, marker='*')
    # plt.scatter(x_black_values, y_black_values, s=0.5, c='black', alpha=1, label="difference greater than 10")
    # plt.scatter(x_dark_grey_values, y_dark_grey_values, s=0.5, c='#A9A9A9', alpha=0.6,
    #             label="difference greater than 5")
    # plt.scatter(x_grey_values, y_grey_values, s=0.5, c='#DCDCDC', alpha=0.3, label="difference greater than 0")
    # plt.legend(loc="lower right")
    plt.savefig("results/" + str(config_run) + "/CIAO_graphs/run_opposite_" + str(run + 1))
    # plt.show()
    plt.clf()
    plt.cla()
    plt.close()