
import numpy as  np 
from .create_random_pairs import create_rand_pairs

def roulette_wheel(population, offspring_number, **kwargs):
    """
    Roulette wheel selection

    """
    if kwargs['crossover_type'] == 'blend': # blend crossover only gives one child from two parents (half of the 'normal') algorithm
        offspring_number *= 2

    fitness_sum = np.sum([ind.score for ind in population])
    chosen_elemts = []
    for k in range(offspring_number):
        random_number = np.random.uniform(0,fitness_sum, size=1)[0]
        partial_sum = 0
        numb = 0
        for individ in population:
            partial_sum += individ.score  
            if random_number < partial_sum:
                individ.parent = True
                if numb == 0:
                    chosen_elemts.append([individ])
                    numb += 1
                else:
                    chosen_elemts[-1].append(individ)
                    break

    return chosen_elemts


