import numpy as np 
from .Population import Population
from rues.utils import sorted_population
import corner 
import matplotlib.pyplot as plt 

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
        print(self._population.print_current_gen())
        """
        
        for k in range(max_iterations):
            self._population.crossover(X, Y, **self._config_dict)

            if k % 100 == 0:
                print(f"Generation number: {k}")

        
        self._population.calculate_fitness(X,Y, kill_workers = True) # calculate fitness for last population
        self._completed_fit = True 


    def get_sorted_population(self):
        """
        Returns the entire sorted (from lowest to highest) population (by fitness). 
        Returns
        --------
            Dictionary with sets inside (median value, median - 16th percentile, 84th percentile - median)
        """
        if not self._completed_fit:
            raise Exception("Genetic algorithm fit is yet to train;")
        
        return sorted_population(self._population.get_population(), 'score')

    def get_optimal_params(self):
        """
            Returns the parameters of the individual with the highest fitness level
        """
        return sorted_population(self._population.get_population(), 'score')[-1].parameters

    def create_corner(self):
        if not self._completed_fit:
            raise Exception("Genetic algorithm fit is yet to train;")
        
        param_dict = self._population.get_population_parameters()

        output = {}

        fits = [i.score for i in self._population.get_population()]

        nsamples = self._population.size
        param_numb = len(param_dict.keys())
        all_values = []
        for parameter, values in param_dict.items():
            percentiles = np.percentile(values, [25, 50, 75])
            all_values.append(np.broadcast_to(np.asarray(values),(1,nsamples)))

            output[parameter] =  (percentiles[1], percentiles[1] - percentiles[0], percentiles[2] - percentiles[1] )
        
        corners = np.vstack(all_values).T

        figure = corner.corner(corners,
                        labels = list(param_dict.keys()),
                       quantiles=[],
                       show_titles=False, title_kwargs={"fontsize": 12})
        
        axes = np.array(figure.axes).reshape((len(param_dict), len(param_dict)))

        best_params = self.get_optimal_params()
        # Loop over the diagonal
        for i, key in enumerate(param_dict.keys()):
            ax = axes[i, i]
            ax.axvline(best_params[key], color="r", linestyle = '--')

        plt.show()
        return output
