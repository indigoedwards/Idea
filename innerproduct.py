import numpy as np
import iDEA as idea

#Find the inner product of two states for a given system
#INPUTS:    state1,state2, states being checked
#           system1,system2, systems of states being checked
#RETURN:    inner product of states

def innerproduct(state1,state2,system1,system2):
    if (type(state1) != idea.state.ManyBodyState):
        raise Exception("State 1 is not a valid ManyBodyState")
    if (type(state2) != idea.state.ManyBodyState): 
        raise Exception("State 2 is not a valid ManyBodyState")
    if (type(system1) != idea.system.System):
        raise Exception("System1 is not valid")
    if (type(system2) != idea.system.System):
        raise Exception("System2 is not valid")
    
    return abs(np.sum(state1.full*state2.full)*system1.dx*system2.dx)