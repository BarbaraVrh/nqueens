import math
import time
#from random_restart import *
import sys
import random
from NQueensProblem_rr_lbs import *


class SimulatedAnnealing:

    def __init__(self, problem):
        # save the
        self.problem = problem
        self.rounds = 0
        self.timeSpent = 0

    def search4(self):
        return self.simulated_annealing(self.problem.initial)


    def exp_schedule(self, k=30, alpha=0.001, limit=20000):
        return lambda t: (k * math.exp(-alpha * t) if t < limit else 0)


    
    def simulated_annealing(self, state):
        
        startTime = time.time()
        
        schedule  = self.exp_schedule()
        
        current   = state
        
        
        
        for t in range(sys.maxsize):
            
            T = schedule(t)
            
            current_h = self.problem.cost(current)
            
            if T == 0 or current_h ==0:
                self.timeSpent = time.time() - startTime
                print("SA: ", t, ") cost of next state: ", current_h, " for final state ", current)
                return current
            
            neighbour = self.problem.randomnearstate(current)
            
            if not neighbour:
                self.timeSpent = time.time() - startTime
                return current
            
           
            new_h = self.problem.cost(neighbour)
            
            # ---------- REZA EDIT (05/09/23) ----------
            # delta_e = new_h - current_h
            #                      THIS IS MINIMIZATION PROBLEM, HENCE YOU WANT YOUR NEIGHBOR'S COST
            #                      TO BE LOWER THAN YOURS. HENCE YOU SHOULD CONSIDER DOING
            #                      delta_e = current_h - new_h
            delta_e = current_h - new_h
            # ---------- ENDS ----------
            
     
            # ---------- REZA EDIT (05/09/23) ----------
            # I WOULD EXPAND YOUR ABOVE CODE AS FOLLOWS. IT WILL LOOK ALMOST LIKE OUR PSEUDOCODE FROM CLASS LECTURE
            str_formatted = "[diff=%0.2f, T=%0.2f]"%(delta_e, T)
            if delta_e > 0:
                
                current    = neighbour
                print("SA: ", t, ")",     str_formatted,"     taking random state as temparature difference is +ve ")
                
            else:
                                
                
                random_toss = random.uniform(0.0, 1.0)
                
                if random_toss < math.exp(delta_e/T):
                    current = neighbour                    
                    print("SA: ", t, ")", str_formatted,"     taking random state. random_toss=", random_toss, " and exp(delta_e/T)=", math.exp(delta_e/T))
                else:
                    current = current
                    print("SA: ", t, ")", str_formatted,"     not taking random state. random_toss=", random_toss, " and exp(delta_e/T)=", math.exp(delta_e/T))
                    
                    
            # ---------- ENDS ----------
            
