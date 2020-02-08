
import numpy as np 
import random

def pop_random(lst):
    idx = random.randrange(0, len(lst))
    return lst.pop(idx)

def stochastic_uni_sampling(population, offspring_number):
    """
        TODO: the iteration through the pointer list can be done more efficiently
        There is no need to start from the beginning of the population for each pointer
        However, there seems to be no significant delay associated with this process.
    """
    fitness_sum = np.sum([ind.score for ind in population])

    # create pointer array to sample population
    pointer_distance = fitness_sum / (2 * offspring_number)
    start = np.random.uniform(0, pointer_distance, size = 1)[0]
    pointers = [start + pointer_distance*i for i in range(offspring_number*2 )]

    chosen_elements = []
    for p in pointers:
        part_sum = 0
    
        for index, individual in enumerate(population):
            part_sum += individual.score 
            if  p < part_sum:
                chosen_elements.append(individual)
                individual.parent = True 
                break  # avoid parsing through the list after finding the parent
    
    # create random pairs out of the chosen elements
    chosen_pairs = []
    for k in range(offspring_number): # list will always have an even number of elements
        chosen_pairs.append([pop_random(chosen_elements), pop_random(chosen_elements)])
    
    return chosen_pairs