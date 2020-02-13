import random

def pop_random(lst):
    idx = random.randrange(0, len(lst))
    return lst.pop(idx)

def create_rand_pairs(chosen_elements):
    # create random pairs out of the chosen elements
    chosen_pairs = []
    for k in range(int(len(chosen_elements)/2)): # list will always have an even number of elements
        chosen_pairs.append([pop_random(chosen_elements), pop_random(chosen_elements)])
    return chosen_pairs