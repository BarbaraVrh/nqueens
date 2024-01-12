

from NQueensProblem_rr_lbs import *
from HillClimbingSearch_rr_lbs import *
from random import shuffle
from Simulated_Annealing import *
# create the problem model

#nqueens = NQueensProblem((1,7,4,7,0,3,4,2)) # 4 changes
#nqueens = NQueensProblem((1, 3, 0, 3)) # 
nqueens = NQueensProblem((15,13,13,3,12,5,4,1,10,1,2,8,11,9,8,4)) 



print("==============")
print("Hill Climbing")
myHCSearch = HillClimbingSearch(nqueens)
state = myHCSearch.search()
print("\nsolution: ", state)
print("Number of rounds:", myHCSearch.rounds)
print("Time Spent with Hill Climbing search:", myHCSearch.timeSpent)
print("\n")

print("==============")
print("Random Restart Search")
rrSearch = HillClimbingSearch(nqueens)
state = rrSearch.search2()
print("\nsolution: ", state)
print("Number of rounds:", rrSearch.rounds)
print("Time Spent with Random Restart Hill Climbing search:", rrSearch.timeSpent)
print("\n")

print("==============")
print("Local Beam Search")
lbsSearch = HillClimbingSearch(nqueens)
state = lbsSearch.search3()
print("\nNumber of rounds:", lbsSearch.rounds)
print("Time Spent with Local Beam search:", lbsSearch.timeSpent)
print("\n")


print("==============")
print("Simulated Annealing Search")
saSearch = SimulatedAnnealing(nqueens)
state = saSearch.search4()
print("\nsolution: ", state)
print("Time Spent with Simulated Annealing Search", saSearch.timeSpent)
print("\n")








