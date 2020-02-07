from Individual import Individual
import numpy as np

class Population():
    def __init__(self, pop_size, param_limits):
        """

        Parameters
        -------------

        pop_size: int
            size of the population
        param_limits: dict
            Dictionary with the upper and lower value of the model parameters
        """

        self._population = [Individual() for _ in range(pop_size)]

    def get_population(self):
        return self._population

    def _run_fitness_computation(self):
        """
        Computes the score of each individual, to prepare for next generation
        """
        
        return []

    def crossover(self):
        """
        Perform the crossover between the fittest elements
        """
        pass 

a = Population(5, {})

print(a.get_population())