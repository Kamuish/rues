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

        self.generation = 0
        self._population = [Individual(param_values =  param_limits, gen_date=0) for _ in range(pop_size)]

    def get_population(self):
        return self._population

        
    def _run_fitness_computation(self):
        """
        Computes the score of each individual, to prepare for next generation
        """
        return []


    def crossover(self, fitness_func, parent_model='roulette', **kwargs):
        """
        Perform the crossover between the fittest elements

        Parameters
        -----------

        fitness_func:
            function to calculate the score of each element
        parent_model: str
            Model in use to find the individuals that will be selected:
                roulette: roulette wheel selection 
                tournament: tournament selection
                uni_sample: stochastic universal sampling
        """

        self.generation += 1

    def print_current_gen(self):
        """
        Print all of the individuals of the current generation
        """
        output_string = f"============= Gen: {self.generation} ================\n"

        for element in self._population:
            output_string += str(element) + "\n"
        return output_string

    def get_individual_by_ID(self, ID):
        """
            Return an Individual with the given ID

        Parameters
        --------------
        ID: int
            ID of the individual
        """
        try:
            return [i for i in self._population if i.ID == ID][0]
        except IndexError:
            raise IndexError("Trying to access individual with an ID that does not exist")


if __name__ == '__main__':
    a = Population(5, param_limits = {'a':[0,1]})

    print(a.get_individual_by_ID(6))