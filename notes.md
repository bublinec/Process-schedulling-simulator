Notes
-------------------

# Miscellanea

- time budget: 10 hours
  - most of the time spent on understanding the concepts
  - writing the report
- the goal is to implement the scheduling algorithms and see how they compare for different tests
- work alone, unless someone asks me 
- report: 
  - name, ID, group
  + discussion of your findings for the “interesting” seed
values outlined earlier (i.e., what was the relative performance of the four algorithms,
whether it deviated from your expectations, and what you believe is the cause of the
deviation based on the internal state of the simulator). Feel free to also include any
feedback you may have on the assessed exercise

 AE2 report guideline : your report should not be more than 800 words in 11pt Arial font. The minimum is 500 words. 

- sane defaults provided in code, can adjust them using cmd arguments or directly in code
- there is a parent class simulator, with methods like run, print output etc. [Scheduler Des]
- I create 4 children classes, each will override the scheduler and dispatcher function with one of the scheduling algorithms

## OOP in Python
- self is equivalent of this
- python is not pure OOP language, all class methods need to have self as their first argument
- constructor is called __init__, attributes are also defined in the constructor
- we can also override parent methods
- create a child class passing it in parens
- python doesn't offer any protection of class variables, the convention is to indicate private attributes with _ / dunder __
- there is also a Enum object in python

## Discrete Event Simulation (DES)
- simulates operation of a system via series of discrete events ordered in time
- given a set of events ordered by time of occurrence from earliest to latest,
  the internal clock of simulator does not take on a continuum of values, but rather jumps from one event to the next
- the simulated system is considered to by in a constant state in between any pair of successive events
- while every event triggers a possible change in the system's state

- every time a new process arrives (thats an event) the scheduling algorithm (scheduler function) decides which process should be executed

Main file:
- uses argparse, logging, sys
- set defaults for simulation
- parse arguments which modify the defaults
- print defaults
- instantiate an array of simulators object
  - create object for each children algorithm class 

## Logging
- can be used as printing but also provides many other functionalities, such as creating a file with our loggs

## PRNG
- pseudo random generator
- values generated based on the seed
- we can set seed to get the same results


# Testing, observing

- Formulate hypothesis, explain why
- Try different:
  - seeds, quantum, number of processes 
- Include tables/graphs for each algorithm
- Try recommended seeds