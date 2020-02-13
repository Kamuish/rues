
from rues.utils import sorted_population


def fittest_individuals(population, to_keep):
    
    sorted_pop =  sorted_population(population, 'score') # fittest individuals at the end
    return sorted_pop[-to_keep:]
