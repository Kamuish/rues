
import numpy as np 
import random

def pop_random(lst):
    idx = random.randrange(0, len(lst))
    return lst.pop(idx)

def stochastic_uni_sampling(population, offspring_number):
    fitness_sum = np.sum([ind.score for ind in population])

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
                break
    
    # create random pairs out of the chosen elements
    chosen_pairs = []
    for k in range(offspring_number):
        chosen_pairs.append([pop_random(chosen_elements), pop_random(chosen_elements)])
    
    return chosen_pairs