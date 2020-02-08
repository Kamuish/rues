import numpy as np 
from .create_random_pairs import create_rand_pairs

def tournament_selection(population, offspring_number, **kwargs):
    tournament_size = kwargs['tourn_size']

    selected_elements = []

    for numb in range(2*offspring_number):
        chosen_elements = np.random.choice(population, tournament_size)
        fits = [i.score for i in chosen_elements]
        selected_elements.append(chosen_elements[fits.index(max(fits))])
    
    return create_rand_pairs(selected_elements)