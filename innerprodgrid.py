import numpy as np
import iDEA as idea

#Find the inner product of two states for a given system
#INPUTS:    state1,state2, states being checked
#           system1,system2, systems of states being checked
#RETURN:    inner product of states

def innerproduct(state1,state2,system1,system2):    
    return abs(np.sum(state1.full*state2.full)*system1.dx*system2.dx)


#Generate the innerproduct grid for two states
def innerprodgrid(state1,state2,system1,system2,maxexcitation):
    grid = np.zeros((maxexcitation,maxexcitation))
    for i in range(0,maxexcitation):
        for j in range(0,maxexcitation):
            grid[i][j] = innerproduct(state1.allfull[...,i],state2.allfull[...,j],system1,system2)
    
    return grid 