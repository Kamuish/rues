


def worker(population, **kwargs):
    """ 
    Parameters
    ------------
    
    population: dict
        Dictionary -> keys are the IDs and values the parameters

    """
    try:
        initial_configuration = kwargs['initial_setup']
        configuration_init = initial_configuration(**kwargs)
    except KeyError as e:
        initial_configuration = None 

    fitness_function = kwargs['fit_func']

    calculated_fitness = {}
    for ID, parameters in population.items():
        fit_level = fitness_function(parameters = parameters,
                                    initial_config = configuration_init,
                                    **initial_configuration)
        calculated_fitness[ID] = fit_level