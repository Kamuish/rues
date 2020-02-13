
import numpy as np 

def uniform_mutator(individual, value_ranges):
    """
    Draws a random sample within the possible value ranges. 
    Each parameter has an 50% chance of being selected for mutation.
    If it is selected, a new draw is made in the value range of the given parameter

    """

    parameters = individual.parameters


    for key in parameters.keys():
        if np.random.randint(0,2) :
            parameters[key] = np.random.uniform(*value_ranges[key], size = 1)[0]

    return parameters