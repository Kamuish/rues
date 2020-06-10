
from multiprocessing import Queue
import numpy as np 
from multiprocessing import Process 
from .worker import worker


class multiproc_handler():
    def __init__(self, **kwargs):
        self.keep_alive = kwargs['keep_alive'] 
        self.nproc = kwargs['processes'] 

        self.tasks_queue = None
        self.results_queue = None

        self.processes  = [] 

    def set_configuration(self, config_dict):
        self.config_dict = config_dict

        
    def run_population(self, population, X,Y, kill_workers = False):
        """
        runs the fitness function over the input population. If the workers are set to be kept alive, then the background processes will be alive 
        until the code ends

        """

        kwargs = self.config_dict
        blocks = self.nproc*4 if len(population)/(self.nproc * 4 ) > 2 else self.nproc
        blocks = np.array_split(population, self.nproc)
        number_blocks = len(blocks)

        if self.keep_alive:
            if self.tasks_queue is None:  # create the always alive queues
                self.tasks_queue = Queue()
                self.results_queue = Queue()
                
            tasks_queue  = self.tasks_queue
            results_queue = self.results_queue 
        else:
            tasks_queue  = Queue() 
            results_queue = Queue()

        [tasks_queue.put(i) for i in blocks]  # populate the task queue with all of the blocks

        if not self.keep_alive or len(self.processes) == 0:  # either always creates the processes (if not keep_alive) or creates them for the first time
            for k in range(self.nproc): # create all of the processes
                process = Process(target=worker, args = (tasks_queue, results_queue, self.keep_alive, X, Y), kwargs=kwargs)
                process.start()

                if self.keep_alive:
                    self.processes.append(process)
                
        number_responses = 0
        outputs_complete = {}
        while number_responses != number_blocks:  # wait until all of the workers put all of the information in their output queue
            output = results_queue.get()   # blocking call
            outputs_complete = {**outputs_complete, **output} # merging to final dict
            number_responses += 1

        if kill_workers:
            [tasks_queue.put([]) for i in  range(len(self.processes))]  # populate the task queue with all of the blocks

        for individual in population:
            individual.score = outputs_complete[individual.ID]
        
        return outputs_complete
    

    def __del__(self):
        if self.keep_alive and self.tasks_queue is not None:
            self.tasks_queue.close()
            self.results_queue.close()

            [proc.terminate() for proc in self.processes]

