
  
# https://www.sheffield.ac.uk/polopoly_fs/1.60188!/file/manual.pdf

# page 21

from rues.utils import sorted_population

def age_based_selection(population, to_keep):
    """
    Select only the younger individuals to contine to the next generation

    the n_keep new individuals will substitute the "old" elements

    """


    sort_pop = sorted_population(population, 'creation_age')   # the older elements will be at the end of the list 

    return sort_pop[0:to_keep]
