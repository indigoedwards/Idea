import iDEA as idea
import numpy as np
import gc
from innerprodgrid import innerprodgrid
from find import finddoubleexcitation
from save_observables import save_observables
from testpotential import potential
from save_observables import save_innerprodgrid
import datetime
import sys




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


def assemble(xgrid,doubleexcitation,initial_distance,sensitivity,limit,abovedouble,innerprod_tolerence,distance_step,maxdivisions,outputpath):

    #get initial system for finding double excitation
    v_int = idea.interactions.softened_interaction(xgrid)
    initial_potential = potential(initial_distance)
    initial_system = idea.system.System(xgrid,initial_potential,v_int,electrons="uu")

    #if no initial excitation specified, find it for the initial distance.
    if doubleexcitation == 0:
        doubleexcitation = finddoubleexcitation(initial_system,sensitivity,limit)

    maxexcitation_gen = doubleexcitation + abovedouble
    
    #Generate state at first distance
    print(f"{datetime.datetime.now()}: Generating initial state at distance {initial_distance}, DE={doubleexcitation}")
    sys.stdout.flush()
    distance_old = initial_distance
    distance_new  = initial_distance - distance_step
    system_old = idea.system.System(xgrid,potential(distance_old),v_int,electrons="uu")
    state_old = idea.methods.interacting.solve(system_old, k=maxexcitation_gen, stopprint=True, allstates=True)
    state_id = 1
    save_observables(state_old,system_old,doubleexcitation,distance_old,distance_old,outputpath,state_id,0)
    n = 1

    #Begin moving closer
    print(f"{datetime.datetime.now()}: Starting Movement")
    sys.stdout.flush()
    while distance_old != 0:
        
        #generate new state
        print(f"{datetime.datetime.now()}: Generating state at distance {distance_new}")
        sys.stdout.flush()
        maxexcitation_gen = doubleexcitation + abovedouble
        system_new = idea.system.System(xgrid,potential(distance_new),v_int,electrons="uu")
        state_new = idea.methods.interacting.solve(system_new, k=maxexcitation_gen, stopprint=True, allstates=True)

        #compute inner product grid for these states
        innergrid_old_new = innerprodgrid(state_old,state_new,system_old,system_new,maxexcitation_gen)
        save_innerprodgrid(innergrid_old_new,distance_old,distance_new,outputpath)

        #get value and index of highest inner product for old state double excitation
        de_innerprod_value = np.max(innergrid_old_new[doubleexcitation])
        de_innerprod_index = np.argmax(innergrid_old_new[doubleexcitation])

        #check if there is an inner product above 1-tolerance
        if (de_innerprod_value > (1-innerprod_tolerence)):
            #state found
            #is the current distance a multiple of the step distance?
            if (round(distance_new/distance_step,2)).is_integer():
                print(f"{datetime.datetime.now()}: Double excitation state found at distance {distance_new}, Innerproduct {de_innerprod_value}, DE={de_innerprod_index}")
                sys.stdout.flush()
                state_id = state_id + 1
                doubleexcitation = de_innerprod_index
                save_observables(state_new,system_new,doubleexcitation,distance_new,distance_old,outputpath,state_id,innergrid_old_new)
                system_old = system_new
                state_old = state_new
                del state_new
                gc.collect()
                distance_old = distance_new
                distance_new = distance_new - distance_step
                n = 1
                
            else:
                print(f"{datetime.datetime.now()}: Double excitation state found at distance {distance_new}, Innerproduct {de_innerprod_value}, DE={de_innerprod_index}")
                sys.stdout.flush()
                state_id = state_id + 1
                doubleexcitation = de_innerprod_index
                save_observables(state_old,system_old,doubleexcitation,distance_new,distance_old,outputpath,state_id,innergrid_old_new)
                system_old = system_new
                state_old = state_new
                del state_new
                gc.collect()
                distance_old = distance_new
                distance_new = distance_new - (distance_step/(2**(n-1)))
                
                
        else:
            #state not found, check half distance
            print(f"{datetime.datetime.now()}: Double excitation state not found at distance {distance_new}, Innerproduct {de_innerprod_value}")
            sys.stdout.flush()
            del state_new
            gc.collect()
            distance_new = distance_old-(distance_step/(2**n))
            if n >= maxdivisions:
                raise Exception("Max number of deivisons reached. Stopping")
            n = n + 1

    idea.state.save_many_body_state(state_old.allfull[...,doubleexcitation],f"{outputpath}/doublestate")
    return doubleexcitation
    
