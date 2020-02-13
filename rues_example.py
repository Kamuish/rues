from rues import  Genetic
import numpy as np
import matplotlib.pyplot as plt 

def fitness(data_x, data_y, ind_parameters, initial_config, **kwargs):
    """
        fitness function should have these arguments. 

        kwargs is the 'worker_params' dictionary on line 31
    """

    residuals = data_y - model(ind_parameters['amplitude'], ind_parameters['phase'], data_x)
    return 1/np.std(residuals)  # we want to maximize the fitness of an individual


def model(amplitude, phase, X):
    """
        Simple sinusoidal model
    """
    return amplitude * np.sin(X + phase)


def rues_example():
    configuration_dict = {
        'keep_alive': True,
        'offspring_ratio': 0.5,
        'mutate_prob': 0.01,
        'processes': 4,
        'crossover_type': 'blend',
        'alpha_value': 0.5,
        'mutation_type': 'uniform',
        'reinsertion_type': 'age',
        'selection_type': 'tournament',
        'tourn_size': 4,
        'worker_params': {'fit_func': fitness, 'initial_setup': None},
        
    }

    # create a population with 100 individuals, with two parameters to be fitted
    a = Genetic(100, {'amplitude':[0,6], 'phase':[0, np.pi*2]}, configuration_dict)

    x = np.linspace(0, 2*np.pi, 200)
    y_noise_free = model(4, np.pi/4, x)

    yerr = 0.5 * np.random.rand(200)
    y_noisy = y_noise_free + yerr * np.random.randn(200)
    
    plt.plot(x, y_noise_free, color = 'black', label = 'input w/ noise')
    plt.plot(x, y_noisy, color = 'blue', label = 'input with noise')

    a.fit(X = x, Y = y_noisy, max_iterations =  200)

    print("OPTIMAL PARAMETERS: ", a.get_optimal_params())
    print("True parameters: ", 4, np.pi/4)
    params = a.get_optimal_params()

    y_model = model(params['amplitude'][0], params['phase'][0], x)
    plt.plot(x, y_model, color = 'red', label = 'model')

    plt.figure()
    plt.plot(x, y_noisy-y_model, label = 'residuals')
    plt.show()


if __name__ == '__main__':
    rues_example()