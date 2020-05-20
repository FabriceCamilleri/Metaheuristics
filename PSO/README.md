# Metaheuristics 
# Implementation of the Genetic Algorithm

Implementation of the Genetic algorithm to solve the TSP problem.

Implementation choices: 

- Parent selection for cross-over using: 
 - Selection by Ranking for N first individual
 then for the remaning selection: 
 - Roulette Wheel Selection 
 
- Random initialization of the population

- GA Stopping Criteria: no or marginal improvement for the last N solutions

- Insertion Strategies:  replace an entire population 

- Mutation: mutation can apply to all individual (according to the rate) except for the fittest individual.