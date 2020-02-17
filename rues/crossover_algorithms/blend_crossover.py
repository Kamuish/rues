
from rues.Individual import Individual
import numpy as np 


def blend_crossover(parent_list, generation,value_limits,  **kwargs):
    """
        Does the alpha_point crossover operator over the two parents, allowing to create the new individual

    Parameters
    ------------
    parent_1:
        one of the parents
    parent_2:   
        another parent
    **kwargs:
        configuration dictionary. Needs to have the alpha_value attribute defined, to set the number of crossover spots
    """
    try:
        alpha = kwargs['alpha_value']
    except KeyError:
        raise KeyError("alpha_value is not defined for the blended crossover algorithm.")

    parent_1 = parent_list[0]
    parent_2 = parent_list[1]
    
    params_1 = parent_1.parameters
    params_2 = parent_2.parameters

    children_1_params = {a: None for a in params_1.keys()}
    
    for param_name in children_1_params.keys():
        parent_1_p = params_1[param_name]
        parent_2_p = params_2[param_name] 
        if parent_2_p >= parent_1_p:  # find the upper and lower parameter limit
            big = parent_2_p
            small = parent_1_p
        else:
            big = parent_1_p
            small = parent_2_p

        lower_limit = max(small - alpha*(big - small), value_limits[param_name][0]) # avoid sampling out of bounds
        upper_limit = min(big + alpha*(big - small), value_limits[param_name][1]) # avoid sampling out of bounds

        children_1_params[param_name] = np.random.uniform(lower_limit, upper_limit, size = 1)[0]
    
    child_1 = Individual(param_values = children_1_params,
                        gen_date = generation)
    
    
    return [child_1]