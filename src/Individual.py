
import numpy as np 


class Individual():
    pop_tracker = 0

    def __init__(self, param_values, first_gen = False, mutate_prob = 0.1):
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

        self.ID = self.__class__.pop_tracker
        self.__class__.pop_tracker += 1
        self._param_vector = {}
        self._mutate_prob = 0.1
        # create Individual with parameters random within the region space
        if first_gen:
            for key, value in param_values.items():
                self._param_vector[key] = np.random.uniform(*value, size = 1)[0]
        else:
            self._param_vector = param_values

    def __repr__(self):
        return f"ID: {self.ID} {self._param_vector}" 


if __name__ == '__main__':
    a = Individual({'a':[0,2]}
    )
    print(a)