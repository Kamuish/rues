
import numpy as np 

def uniform_mutator(individual, value_ranges):
    """
    Draws a random sample within the possible value ranges. 
    Each parameter has an 50% chance of being selected for mutation.
    If it is selected, a new draw is made in the value range of the given parameter

    """

    parameters = individual.parameters

    child_params = parameters.copy() 


    for key in child_params.keys():
        if np.random.randint(0,2) :
            print(f"{key} going to mutate")
            child_params[key] = np.random.uniform(*value_ranges[key], size = 1)[0]

    individual.mutate_genes(child_params)