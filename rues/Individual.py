
import numpy as np 


class Individual():
    pop_tracker = 0

    def __init__(self, param_values, gen_date):
        """
            Individual class, part of the species that will fit our problem

            Parameters
            ------------
            param_values: dict
                If first_gen == True, then dict with each parameter as a key and the value is a list with upper and lower bound for that
                parameter. Else it is the parameter value for this individual
            
            first_gen: bool
                If true creates a random inidividual (for the creation of the first generation). Otherwise, the individual will
                be the result of crossover.
            
            mutate_prob: float 
                Probability of having mutations
        """
        self._generation_creation = gen_date
        self.ID = self.__class__.pop_tracker
        self.__class__.pop_tracker += 1
        self._param_vector = {}


        # if True then it will be used as one of the parents
        self.parent = False   
        self._score = None

        # create Individual with parameters random within the region space
        if gen_date == 0:
        
            for key, value in param_values.items():
                self._param_vector[key] = np.random.uniform(*value, size = 1)[0]
        else:
            self._param_vector = param_values


    def mutate_genes(self, new_params):
        self._param_vector = new_params

    @property
    def score(self):
        return self._score

    @property
    def creation_age(self):
        return self._generation_creation
        
    @property
    def parameters(self):
        return self._param_vector

    @score.setter
    def score(self, new_score):
        self._score = new_score

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        output_str = f"ID: {self.ID} {self._param_vector}"
        added_info = '' if self._score is None else f" - fitness: {self._score}" 
        return output_str + added_info


if __name__ == '__main__':
    a = Individual({'a':[0,2]}
    )
    print(a)

    a.score = 10
    print(a)