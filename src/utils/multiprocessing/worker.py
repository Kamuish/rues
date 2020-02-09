
from multiprocessing import Queue

def worker(in_queue, out_queue, **kwargs):
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
        configuration_init = None 

    print(kwargs)
    fitness_function = kwargs['fit_func']

    calculated_fitness = {}

    while True:
        if not in_queue.empty():
            population = in_queue.get(timeout=1)
        else:
            return 

        for individual in population:
            ID = individual.ID
            parameters = individual.parameters
            fit_level = fitness_function(parameters = parameters,
                                        initial_config = configuration_init,
                                        **kwargs)
            calculated_fitness[ID] = fit_level
            
        out_queue.put(calculated_fitness)