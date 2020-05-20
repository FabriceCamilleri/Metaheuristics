# Metaheuristics 
# Implementation of the Particle Swarm Optimization


Implementation choices: 

- Inertia weight PSO with 3 parameters: w, c1 and c2
- In case the velocity goes beyond the boundaries, it is set to the boundary value
- Stopping criterion: no improvement more than epsilon over the last N iterations
