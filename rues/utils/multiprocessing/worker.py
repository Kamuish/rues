
from multiprocessing import Queue

def worker(in_queue, out_queue, keep_alive, X,Y, **kwargs):
    """ 
    Parameters
    ------------
    
    population: dict
        Dictionary -> keys are the IDs and values the parameters

    """

    if kwargs['initial_setup'] is not None:  # allow to run a function before the 'fit_func' starts being used over all of the individuals of the population
        initial_configuration = kwargs['initial_setup']
        configuration_init = initial_configuration(X,Y, **kwargs)
    else:
        configuration_init = None 

    fitness_function = kwargs['fit_func']

    calculated_fitness = {}   # dictionary to store fitness values; keys -> ID of the individual; values -> fit level

    while True:
        if not in_queue.empty() or keep_alive:  # still have elements in the input queue or worker is supposed to stya alive  
            population = in_queue.get()

            if len(population) == 0:
                print('shutting down')
                return
        else:
            return 

        for individual in population:
            ID = individual.ID
            parameters = individual.parameters
            if individual.score is None:
                fit_level = fitness_function(ind_parameters = parameters,
                                        initial_config = configuration_init,
                                        data_x = X,
                                        data_y = Y,
                                        **kwargs)
            else:
                fit_level = individual.score
            calculated_fitness[ID] = fit_level
            
        out_queue.put(calculated_fitness)