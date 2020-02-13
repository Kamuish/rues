from numpy import argsort

def sorted_population(sort_type):

    values_inds = [i.getattr(sort_type) for i in self._population]

    indexes = argsort(values_inds)

    return self._population[indexes]
