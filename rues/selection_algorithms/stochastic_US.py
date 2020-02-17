
import numpy as np 
from .create_random_pairs import create_rand_pairs

def stochastic_uni_sampling(population, offspring_number, **kwargs):
    """
        TODO: the iteration through the pointer list can be done more efficiently
        There is no need to start from the beginning of the population for each pointer
        However, there seems to be no significant delay associated with this process.
    """
    if kwargs['crossover_type'] == 'blend': # blend crossover only gives one child from two parents (half of the 'normal') algorithm
        offspring_number *= 2

    fitness_sum = np.sum([ind.score for ind in population])

    # create pointer array to sample population
    pointer_distance = fitness_sum / (offspring_number)
    start = np.random.uniform(0, pointer_distance, size = 1)[0]
    pointers = [start + pointer_distance*i for i in range(offspring_number )]

    chosen_elements = []
    for p in pointers:
        part_sum = 0
    
        for index, individual in enumerate(population):
            part_sum += individual.score 
            if  p < part_sum:
                chosen_elements.append(individual)
                individual.parent = True 
                break  # avoid parsing through the list after finding the parent
    

    return create_rand_pairs(chosen_elements)