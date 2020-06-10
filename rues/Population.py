from rues.Individual import Individual
from rues.selection_algorithms import roulette_wheel, stochastic_uni_sampling, tournament_selection
from rues.crossover_algorithms import k_point_crossover, blend_crossover
from rues.mutation_algorithms import uniform_mutator
from rues.reinsertion_algorithms import age_based_selection, fittest_individuals
from rues.utils import multiproc_handler

import numpy as np

class Population():
    def __init__(self, pop_size, param_limits, **kwargs):
        """

        Parameters
        -------------

        pop_size: int
            size of the population
        param_limits: dict
            Dictionary with the upper and lower value of the model parameters
        """

         # Different possibilities for selection, crossover and mutation algorithms to be used
        self._selection_mapping = { 
                            'roulette': roulette_wheel,
                            'tournament': tournament_selection,
                            'universal_sampling': stochastic_uni_sampling
        }

        self._mutation_mapping = {
                        'uniform': uniform_mutator
        }

        self._crossover_mapping = {
                'K_point': k_point_crossover,
                'blend': blend_crossover
        }


        self._value_limits = param_limits
        self.mutation_prob = kwargs['mutate_prob']
        self.generation = 0
        self._pop_size = pop_size
        self._population = [Individual(param_values =  param_limits, gen_date=0) for _ in range(pop_size)]

        self.number_offsprings = int(pop_size * kwargs['offspring_ratio']) # each set of 2 parents creates 2 childs

        self._parameters_to_fit = param_limits.keys()

        self._process_handler = multiproc_handler(**kwargs)
        
    def get_population(self):
        return self._population
      

    def crossover(self, X, Y, **kwargs):
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
                    uniform
            reinsertion_type:
                Algorithm for reinsertion 
                    - age
                    - fitness
            worker_params: dict
                Configuration dictionary; should have some values defines:
                    - fit_func: function to calculate fitness of individual
                    - init_setup: initial setup function, if needed, else None
                    - all other worker specific kwargs, for the fit_func and init_setup
        """

        if self.generation == 0:  # set the configuration arguments for the initial setup and fitness functions
            self._process_handler.set_configuration(kwargs['worker_params'])
            
        self.generation += 1
        selection_type = kwargs['selection_type']
        crossover =  kwargs['crossover_type']
        mutation = kwargs['mutation_type']

        self.calculate_fitness(X, Y, kill_workers = False)
        # select the parents
        selected_pairs = self._selection_mapping[selection_type](population = self._population,
                                                                offspring_number = self.number_offsprings,
                                                                **kwargs
                                                                )

        # Select the members to maintain to next generation and find individuals to be reinserted
        number_to_keep = self._pop_size - self.number_offsprings


        if number_to_keep != 0:
            if kwargs['reinsertion_type'] == 'age':
                if self.generation == 1:
                    new_gen = fittest_individuals(self._population, number_to_keep)
                else:
                    new_gen = age_based_selection(self._population, number_to_keep)

            elif kwargs['reinsertion_type'] == 'fit':
                new_gen = fittest_individuals(self._population, number_to_keep)
        else:
            new_gen = []

        # create the offspring and see if they will mutate
        for parent_pair in selected_pairs: 
            children = self._crossover_mapping[crossover](parent_list = parent_pair, 
                                                                        generation = self.generation,
                                                                        value_limits = self._value_limits,
                                                                        **kwargs) 
            for individual in children:   
                if np.random.random(size = 1)[0] < self.mutation_prob:  # trigger mutation with given probability ?
                    mutated_genes = self._mutation_mapping[mutation](individual, self._value_limits)

                    individual.mutate_genes(mutated_genes)
                new_gen.append(individual)
        self._population = new_gen

    def calculate_fitness(self, X, Y, kill_workers):
        self._process_handler.run_population(self._population, X, Y, kill_workers) # compute the fitness of current 

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
    @property
    def size(self):
        return self._pop_size
if __name__ == '__main__':
    a = Population(5, param_limits = {'a':[0,1], 'b':[2,3]})


    print(a.get_population_parameters())