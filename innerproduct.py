import numpy as np
import iDEA as idea

#Find the inner product of two states for a given system

def innerproduct(state1,state2,system):
    if (type(state1) != idea.state.ManyBodyState):
        raise Exception("State 1 is not a valid ManyBodyState")
    if (type(state2) != idea.state.ManyBodyState): 
        raise Exception("State 2 is not a valid ManyBodyState")
    if (type(system) != idea.system.System):
        raise Exception("System is not valid")
    
    return abs(np.sum(state1.full*state2.full)*system.dx**system.count)