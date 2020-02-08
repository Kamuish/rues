
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
        initial_configuration = None 

    fitness_function = kwargs['fit_func']

    calculated_fitness = {}

    while True:
        try:
            population = in_queue.get(timeout=1)
        except Queue.Empty:
            return
        except Exception as e:
            print("Oh, another error: ", e)
            return 

        for individual in population:
            ID = individual.ID
            parameters = individual.parameters
            fit_level = fitness_function(parameters = parameters,
                                        initial_config = configuration_init,
                                        **initial_configuration)
            calculated_fitness[ID] = fit_level
            
        out_queue.put(calculated_fitness)