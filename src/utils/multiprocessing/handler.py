
from multiprocessing import Queue
import numpy as np 
from multiprocessing import Process 
from .worker import worker


def multiproc_handler(population, **kwargs):
    
    blocks = np.array_split(population, kwargs['processes'])
    number_blocks = len(blocks)
    tasks_queue  = Queue() 
    results_queue = Queue()

    [tasks_queue.put(i) for i in blocks]  # populate the task queue with all of the blocks

    for k in range(kwargs['processes']): # create all of the processes
        process = Process(target=worker, args = (tasks_queue, results_queue), kwargs=kwargs)
        process.start()
        
    number_responses = 0
    
    outputs_complete = {}
    while number_responses != number_blocks:  # wait until all of the workers put all of the information in their output queue
        output = results_queue.get()   # blocking call
        outputs_complete = {**outputs_complete, **output}
        number_responses += 1


    return outputs_complete

