from functions import *
import numpy as np
import matplotlib as plt
import time
import random


# definition of a class for Particle
class Particle:
    def __init__(self, problem):
        self.problem=problem
        self.position = np.random.uniform(low=self.problem.bounds[0], high=self.problem.bounds[1], size=self.problem.dim)
        self.velocity = np.random.uniform(low=-(self.problem.bounds[1]-self.problem.bounds[0]) \
                                        , high=(self.problem.bounds[1]-self.problem.bounds[0]), size=self.problem.dim)
        self.best_part_pos = self.position.copy()
        self.fitness = self.problem.fitness(self.position)
        self.best_fitness = self.fitness.copy()

    def moveParticule (self, swarm):
        #print (self.position)
        r1 = random.random()    # randomizations
        r2 = random.random()
     
        
        self.velocity =  ( swarm.w * self.velocity)   + \
            ( swarm.c1 * r1 * (self.best_part_pos - self.position) ) + \
            ( swarm.c2 * r2 * (swarm.best_swarm_position - self.position) )
        '''
        self.velocity =  swarm.w * ( self.velocity   + \
            ( swarm.c1 * r1 * (self.best_part_pos - self.position) ) + \
            ( swarm.c2 * r2 * (swarm.best_swarm_position - self.position) ) )
            
        #print ('ok')
        '''
        
        self.velocity=np.minimum(self.velocity, self.problem.bounds[1])
        self.velocity=np.maximum(self.velocity, self.problem.bounds[0])
        
        self.position = self.position + self.velocity
        
        #print (self.position)
        self.fitness = self.problem.fitness(self.position)
        #print(self.fitness)
        if self.fitness < self.best_fitness:
            self.best_fitness = self.fitness
            self.best_part_pos = self.position
            
    
    
            
            
# definition of a class for Swarm
class Swarm:

    def __init__(self, problem, numOfParticule=5, w=0.7, c1=1.4, c2=1.4):
        self.w=w
        self.c1=c1
        self.c2=c2
        self.problem=problem
        self.swarm_list = [Particle(problem) for i in range(numOfParticule)]
        self.best_swarm_position = self.swarm_list[0].position
        self.best_swarm_fitness = self.swarm_list[0].fitness
        for particule in self.swarm_list:
            if particule.fitness < self.best_swarm_fitness:
                self.best_swarm_position = particule.position
                self.best_swarm_fitness = particule.fitness
        

        
    def moveSwarm(self):
        for particule in self.swarm_list:
            particule.moveParticule(self) # update the position of particle
            if particule.fitness < self.best_swarm_fitness:  # check the position if it's best for swarm
                self.best_swarm_position = particule.position
                self.best_swarm_fitness = particule.fitness

# definition of a class for Optimize
class Optimize:
        def __init__(self,swarm, numOfEpochs=0, epsilon=0, N=100 ):
            self.epsilon=epsilon
            self.N=N
            self.swarm=swarm
            
        
        def run(self):
            ts=time.time()
            progress = []
            previousMin=self.swarm.best_swarm_fitness
            progress.append(previousMin)
            carryOn = True
            i = 0
            while carryOn: 
                self.swarm.moveSwarm()
                progress.append(self.swarm.best_swarm_fitness)
                # print('Run: {0} | Best fitness: {1}'.format(i, swarm.best_swarm_fitness))
                if previousMin > self.swarm.best_swarm_fitness:
                    previousMin=self.swarm.best_swarm_fitness
                if i>= self.N :
                    if (progress[- self.N] - progress[-1]) <= self.epsilon:
                        carryOn = False
                i += 1
            return progress, self.swarm.problem.nbFitness, time.time()-ts
        