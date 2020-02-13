from numpy import argsort, asarray

def sorted_population(population, sort_type):

    values_inds = [getattr(i, sort_type) for i in population]

    indexes = argsort(values_inds)

    return list([population[index] for index in indexes])
