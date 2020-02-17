
from rues.Individual import Individual
import numpy as np 


def k_point_crossover(parent_list, generation,  **kwargs):
    """
        Does the k_point crossover operator over the two parents, allowing to create the new individual

        By default does the 1 crossover point
    Parameters
    ------------
    parent_1:
        one of the parents
    parent_2:   
        another parent
    **kwargs:
        configuration dictionary. Needs to have the K_value attribute defined, to set the number of crossover spots
    """

    try:
        k = kwargs['K_value']
    except KeyError:
        raise KeyError("K_value is not defined for the k_point crossover algorithm.")

    parent_1 = parent_list[0]
    parent_2 = parent_list[1]
    
    params_1 = parent_1.parameters
    params_2 = parent_2.parameters

    children_1_params = {a: None for a in params_1.keys()}
    children_2_params = {a: None for a in params_1.keys()}

    flag = 1

    param_map = {1: params_1, -1: params_2}

    current_pointer = 0
    number_params = len(params_1)

    if k >= number_params:
        raise ValueError("Crossover points equal to number of parameters")

    switching_points = np.sort(np.random.randint(1, len(params_1) - 1, size = k))

    for param_index, key in enumerate(params_1.keys()):
        children_1_params[key] = param_map[flag][key]
        children_2_params[key] = param_map[-1*flag][key]

        if param_index == switching_points[current_pointer] - 1:
            flag *= -1    # switches between both parents 
            current_pointer = current_pointer +  1 if current_pointer < k -1 else current_pointer # updates the pointer

    child_1 = Individual(param_values = children_1_params,
                        gen_date = generation)

    child_2 = Individual(param_values = children_2_params,
                        gen_date = generation)     
      
    return [child_1, child_2]