
from multiprocessing import Queue

def worker(in_queue, out_queue, **kwargs):
    """ 
    Parameters
    ------------
    
    population: dict
        Dictionary -> keys are the IDs and values the parameters

    """

    try:  # allow to run a function before the 'fit_func' starts being used over all of the individuals of the population
        initial_configuration = kwargs['initial_setup']
        configuration_init = initial_configuration(**kwargs)
    except KeyError as e:
        configuration_init = None 

    fitness_function = kwargs['fit_func']

    calculated_fitness = {}   # dictionary to store fitness values; keys -> ID of the individual; values -> fit level

    while True:
        if not in_queue.empty() or kwargs['keep_alive']:  # still have elements in the input queue or worker is supposed to stya alive  
            population = in_queue.get()
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