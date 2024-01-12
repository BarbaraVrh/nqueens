"""
HillClimbingSearch
"""
import time
#from random_restart import *
import pdb
import random
import numpy as np

class HillClimbingSearch():

    def __init__(self, problem, beam_width=1):
        # save the
        self.problem = problem
        self.beam_width = beam_width
        self.rounds = 0
        self.timeSpent = 0

    """
    Searches for a path from the start state to a goal state using the Problem given
    to the constructor
    """
    def search(self):
        return self.hillclimb(self.problem.initial)

    """
    Conducts Hill Climbing Search from a given start state.
    startState: the start state for the search
    """
    def hillclimb(self, startState):
        startTime = time.time()

        # create a node for the state;
        state = startState
        bestCost = self.problem.cost(state) #cost = how many queens attacking each other; min value initialzing
        
        better_move_found = True 
         
        while better_move_found:
         
            better_move_found = False

            neighbor_list = self.problem.actions(state) # neighbor node
            self.rounds += 1
            # find the lowest valued neighbor
            for n in neighbor_list:

                cost_of_n = self.problem.cost(n)

                if cost_of_n < bestCost:

                    bestCost = cost_of_n

                    best_cost_state = n

                    better_move_found = True
                 
            # update state to lowest valued neighbor      
            if better_move_found:
                state = best_cost_state
                print("current state: ", state, ", cost = ", bestCost)
                    
                 
        

        self.timeSpent = time.time() - startTime

        return state, bestCost
        
        
    def search2(self):
        return self.random_start(self.problem.initial)
    
    def shuffle(self, state):
        
        # generate a random permuation of the given state
        # new_state = np.random.permutation([1,2,3])
        new_state = np.random.permutation(state)
        
        return  new_state

    def search3(self):
        return self.local_beam_search(self.problem.initial)
        
        
    
    def random_start(self,startState,limit=10):
        state = startState
        count = 0
        
        while self.problem.cost(state) !=0  and count < limit:
            
            
            # pdb.set_trace()
            
            # state.shuffle(200)
            new_state = self.shuffle(startState) # REZA EDIT: shuffle the positions of the queens
            
            print(count, ") Running hillclimbing from random shuffling of the given initial state: ", new_state)
            
            
            state, cost =self.hillclimb(new_state)
            
            if (cost == 0):
                print("Solution found!")
                print("\n")
            else:
                print("Solution not found!")
                print("\n")
                
            count += 1
            
            
                        
        return state
    
    def local_beam_search(self, startState):
        startTime = time.time()

        # create a list of nodes for the initial states
        states = [startState]
        print("Local Beam Search start state: ", states)
        print("\n")

        # search for solution
        while True:
            successors = []

            # for each state in the beam
            for state in states:
                neighbor_list = self.problem.actions(state)
                self.rounds += 1

                # for each neighbor of the state
                for n in neighbor_list:
                    
                    # compute the cost of the neighbor
                    cost = self.problem.cost(n)
                    successors.append((n,cost))

             # sort the successors in ascending order of cost
            successors.sort(key=lambda x: x[1])
            #print("???: ", successors)
            #print("\n")

            # check if the best successor is better than the current state
            if successors[0][1] < self.problem.cost (states[0]):
                
                # update the states to be the best successors
                states = [x[0] for x in successors[:self.beam_width]]
                print("Best successor: ", states) 
                print("Current successor cost: ", self.problem.cost (states[0]))
                print("\n")
  
            else:
                #print("????")
                break

        self.timeSpent = time.time() - startTime
        print("Solution found!", states[0])
        return states[0]
