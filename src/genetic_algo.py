import numpy as np 
from .Population import Population

class Genetic():
    def __init__(self, pop_size, param_limits, config_dict):
        """

        Parameters
        -------------
        fitness_func: function
            Function to evaluate the fitness of a individual from the population
        pop_size: int
            size of the population
        param_limits: dict
            Dictionary with the upper and lower value of the model 
        config_dict: dict 
            Dictionary with some configuration Parameters:
                - offspring ratio - % of population that is going to reproduce
                - mutate_prob  - probability of an individual mutating, when created (the zeroth generation cannot mutate)
                - processes -  the number of processes that will be used to run the fitness functions 
                - keep_alive - should the processes stay alive after calculating all of the fitness for a given generation? (ideally set to True)
        """

        self._population = Population( pop_size = pop_size,
                                       param_limits =  param_limits,
                                       **config_dict
                                       ) 
        self._completed_fit = False
        self._config_dict = config_dict

    def fit(self, X, Y, max_iterations):
        """
        Run the genetic algorithm to find the best parameters for the orbit
        """
        for k in range(max_iterations):
            self._population.crossover(X, Y, **self._config_dict)

            if k % 100 == 0:
                print(f"Here we are: {k}")
        self._completed_fit = True 


    def get_optimal_params(self):
        """
            Returns the best value for our problem

            Taken and the median of the entire final population +84th percentile -16th percentile

            I.e. build a 68% confidence interval around the fitted value

        Returns
        --------
            Dictionary with sets inside (median value, median - 16th percentile, 84th percentile - median)
        """
        if not self._completed_fit:
            raise Exception("Genetic algorithm fit is yet to train;")
        
        param_dict = self._population.get_population_parameters()

        output = {}

        for parameter, values in param_dict.items():
            percentiles = np.percentile(values, [25, 50, 75])

            print(percentiles[0], percentiles[2])
            output[parameter] =  (percentiles[1], percentiles[1] - percentiles[0], percentiles[2] - percentiles[1] )

        return output
