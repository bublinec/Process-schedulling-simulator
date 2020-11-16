Notes
-------------------

# Miscellanea

- time budget: 10 hours
  - most of the time spent on understanding the concepts
  - writing the report
- the goal is to implement the scheduling algorithms and see how they compare for different tests
- work alone, unless someone asks me 
- report: 
  - name, ID, group + 
  - discussion of your findings for the “interesting” seed
values outlined earlier (i.e., what was the relative performance of the four algorithms,
whether it deviated from your expectations, and what you believe is the cause of the
deviation based on the internal state of the simulator). Feel free to also include any
feedback you may have on the assessed exercise

- sane defaults provided in code, can adjust them using cmd arguments or directly code

- there is a parent class simulator, with methods like run, print output etc. [Scheduler Des]
- I create 4 children classes, each will override the scheduler and dispatcher function with one of the scheduling algorithms

Main file:
- uses argparse, logging, sys
- set defaults for simulation
- parse arguments which modify the defaults
- print defaults
- instantiate an array of simulators object
  - create object for each children algorithm class 