
from src.Individual import Individual
import numpy as np 


def k_point_crossover(parent_1, parent_2, k = 1):
    """
        Does the k_point crossover operator over the two parents, allowing to create the new individual

        By default does the 1 crossover point
    Parameters
    ------------
    parent_1:
        one of the parents
    parent_2:   
        another parent
    k:
        number of crossover points
    """

    params_1 = parent_1.parameters
    params_2 = parent_2.parameters

    children_params = {a: None for a in params_1.keys()}


    
    flag = 1

    param_map = {1: params_1, -1: params_2}

    current_pointer = 0
    number_params = len(params_1)

    if k >= number_params:
        raise ValueError("Crossover points equal to number of parameters")
    switching_points = np.sort(np.random.randint(1, len(params_1) - 1, size = k))


    for param_index, key in enumerate(params_1.keys()):
        children_params[key] = param_map[flag][key]
    
        if param_index == switching_points[current_pointer] - 1:
            flag *= -1    # switches between both parents 
            current_pointer = current_pointer +  1 if current_pointer < k -1 else current_pointer # updates the pointer


    return children_params