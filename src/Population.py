from Individual import Individual
from src.selection_algorithms import roulette_wheel, stochastic_uni_sampling, tournament_selection
from src.crossover_algorithms import k_point_crossover 
from src.mutation_algorithms import uniform_mutator
from src.reinsertion_algorithms import age_based_selection, fittest_individuals

import numpy as np

class Population():
    def __init__(self, pop_size, param_limits, offspring_ratio=0.5):
        """

        Parameters
        -------------

        pop_size: int
            size of the population
        param_limits: dict
            Dictionary with the upper and lower value of the model parameters
        """
        self.generation = 0
        self._pop_size = pop_size
        self._population = [Individual(param_values =  param_limits, gen_date=0) for _ in range(pop_size)]

        self.number_offsprings = int(pop_size * offspring_ratio) # each set of 2 parents creates 2 childs
        self._parameters_to_fit = param_limits.keys()


        # Different possibilities for selection, crossover and mutation algorithms to be used
        self._selection_mapping = { 
                            'roulette': roulette_wheel
                            'tournament': tournament_selection
                            'universal_sampling': stochastic_uni_sampling
        }

        self._mutation_mapping = {
                        'uniform': uniform_mutator
        }

        self._crossover_mapping = {
                'K_point': k_point_crossover
        }


    def get_population(self):
        return self._population
      
    def _run_fitness_computation(self, fitness_func):
        """
        Computes the score of each individual, to prepare for next generation

        Parameters
        ----------------
        fitness_func:
            function to calculate the score of each element

        """
        return []

    def crossover(self, **kwargs):
        """
        Perform the crossover between the fittest elements. IN order to facilitate the configuration of this function,
        everything is passed through the kwargs.

        In it, we need the following parameters:

            selection_type: str
                Model in use to find the individuals that will be selected:
                    roulette: roulette wheel selection 
                    tournament: tournament selection
                    uni_sample: stochastic universal sampling
            crossover_type: str
                ALgorithm to perform the crossover:
                    K_point: K point crossover algorithm. If one chooses this algorithm, also set the K_value to the desired number of switching points
            mutation_type
                Algorithm for the mutation 
            reinsertion_type:
                Algorithm for reinsertion 
                    - age
                    - fitness
        """
        self.generation += 1

        selection_type = kwargs['selection_type']
        crossover =  kwargs['crossover_type']
        mutation = kwargs['mutation_type']

        self._run_fitness_computation() 
        selected_pairs = self._selection_mapping[selection_type](population = self._population,
                                                                offspring_number = self.number_offsprings
                                                                **kwargs
                                                                )

        number_to_keep = self._pop_size - self.number_offsprings
        if kwargs['reinsertion_type'] == 'age':
            if self.generation == 1:
                new_gen = fittest_individuals(self._population, number_to_keep)
            else:
                new_gen = age_based_selection(self._population, number_to_keep)
        elif kwargs['reinsertion_type'] == 'fit';
            new_gen = fittest_individuals(self._population, number_to_keep)

        # implement interface for modelling the addition of the new offspring
        # e.g. steady state model (children replace the parent's place, if tey have higher fitness)
        # generational: change 
        for parent_pair in selected_pairs: 
            children_1, children_2 = self._crossover_mapping[crossover](parent_list = parent_pair, 
                                                                        **kwargs)

            new_generation.append(children_1)
            new_generation.append(children_2)

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

    def get_population_parameters(self):
        """
        Get the value, for each parameter, for each individual in the population

        Returns
        ----------
        Dictionary where the keys are the parameter's names and the values are lists, with the value of each element in the population
        """
        parameter_dict = {i : [] for i in self._parameters_to_fit}

        for individ in self._population:
            for param in self._parameters_to_fit:
                parameter_dict[param].append(individ.parameters[param])
        return parameter_dict


    @property
    def all_IDS(self):
        return list([i.ID for i in self._population])

if __name__ == '__main__':
    a = Population(5, param_limits = {'a':[0,1], 'b':[2,3]})


    print(a.get_population_parameters())