# rues - real valued genetic algorithms in python 

## What is it ?

rues is a pure python concurrent implementation of real valued genetic algorithms (to be more precise, the fitness evaluation of each individual is concurrent). 

The modular interface easily allows the users to easily implement custom crossover, selection, mutation and reinsertion routines. Furthermore, the concurrency handler interface allows a
user to (if applicable) to initialiase a part of the fitness evaluation function before the score of the individuals is calculated

## How to install

rues is available in pypi, with:

    pip install rues

SO far it was only tested with python3.6+, but it should work on older versions, since it only makes use of non-deprecated features of numpy and matplotlib.


## How to use

Further documentation will eventually appear, but for now refer to the rues_example.py file, where the library is showcased