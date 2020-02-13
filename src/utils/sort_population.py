from numpy import argsort, asarray

def sorted_population(population, sort_type):

    values_inds = [i.getattr(sort_type) for i in population]

    indexes = argsort(values_inds)

    return asarray(population)[indexes]
