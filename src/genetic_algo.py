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
            Dictionary with the upper and lower value of the model parameters
        """
        self._population = Population(pop_size, param_limits) 
        self._completed_fit = False
        self._config_dict = config_dict
        
    def fit(self, X, Y):
        """
        Run the genetic algorithm to find the best parameters for the orbit
        """
        pass
        self._completed_fit = True 


    def get_optimal_params(self):
        """
            Returns the best value for our problem

            Taken and the median of the entire final population +84th percentile -16th percentile

            I.e. build a 68% confidence interval around the fitted value
        """
        if not self._completed_fit:
            raise Exception("Genetic algorithm fit is yet to be used;")
        pass 

        percentiles = np.sqrt(np.nanpercentile(vararr, [16, 50, 84])) / np.sqrt(norm)


