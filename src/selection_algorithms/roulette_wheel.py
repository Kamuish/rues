
import numpy as  np 
from .create_random_pairs import create_rand_pairs
def roulette_wheel(population, offspring_number, **kwargs):
    """
    Roulette wheel selection

    """

    fitness_sum = np.sum([ind.score for ind in population])
    chosen_elemts = []
    for k in range(offspring_number):
        random_number = np.random.uniform(0,fitness_sum, size=1)[0]
        partial_sum = 0
        found_two_parents = False 

        for individ in population:
            partial_sum += individ.score  
            if random_number < partial_sum:
                individ.parent = True
                if numb == 0:
                    chosen_elemts.append(individ)
                else:
                    chosen_elemts.append(individ.ID)
                    found_two_parents = True
                break

    return create_rand_pairs(chosen_elements)


