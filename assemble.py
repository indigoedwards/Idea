import iDEA as idea
import numpy as np


#Assemble a double excitation state
#========================================
#INPUTS:
# potential, xgrid
#========================================
# GENERAL PLAN:
#
# find initial excitation
# generate state at starting distance
# generate state at next distance
# does an inner product exist for the interested state?
# if yes continue, if no generate state halfway between this state and last state
def finddoubleexcitation():
    return

def potential():
    return

def innerprod():
    return


def assemble(xgrid,doubleexcitation,initialdistance,sensitivity,limit,abovedouble,innerprod_tolerence,distance_step):

    #get initial system for finding double excitation
    v_int = idea.interactions.softened_interaction(xgrid)
    initialpotential = potential(initialdistance)
    initialsystem = idea.system.system(xgrid,initialpotential,v_int,electrons="uu")

    #if no initial excitation specified, find it for the initial distance.
    if doubleexcitation == 0:
        doubleexcitation = finddoubleexcitation(initialsystem,sensitivity,limit)
    initialexcitation = doubleexcitation + abovedouble
    
    #Generate state at first distance
    oldsystem = idea.system.system(xgrid,initialpotential,v_int,electrons="uu")
    oldstate = idea.methods.interacting.solve(oldsystem,k=initialexcitation,stopprint=True, allstates=True)
    distance = initialdistance + distance_step
    maxexcitation = initialexcitation
    n = 1

    while distance != 0:
        #Generate new states
        potential = potential(distance)
        newsystem = idea.system.system(xgrid,potential,v_int,electrons="uu")
        newstate = idea.methods.interacting.solve(newsystem,k=maxexcitation,stopprint=True,allstates=True)

        #compute inner product grid
        current_innerprodgrid = np.zeros((maxexcitation,maxexcitation))
        for oldstate_index in range(0,maxexcitation):
            for newstate_index in range(0,maxexcitation):
                current_innerprodgrid[oldstate_index][newstate_index] = innerprod(oldstate.allfull[...,oldstate_index],newstate.allfull[...,newstate_index],oldsystem,newsystem)
        
        #try to find the oldstate in the new system
        if np.max(current_innerprodgrid[doubleexcitation]) > 1-innerprod_tolerence:
            #innerprod found
            doubleexcitation = np.argmax(current_innerprodgrid[doubleexcitation])
            #ADD innerprodgrid to main
            #ADD energy to main
            #SAVE state if needed idk
            if n != 1:
                if (np.mod(distance,distance_step/(2**(n-1)))) != 0:
                    distance = distance + distance_step/(2**(n-1))
                else:
                    distance = distance + distance_step
                    n = 1
            else:
                distance = distance + distance_step
                n = 1
        else:
            #innerprod not found
            #check state between
            distance = distance - distance_step/(2**n)
            n = n + 1

        


    
        



    return 