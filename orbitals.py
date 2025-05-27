import iDEA as idea
import numpy as np
import pickle
from innerprodgrid import innerproduct
from potential import potential
import matplotlib.pyplot as plt
import scipy as sp
import datetime


#from single particle wavefunctions, calculate the basis sets either by hartree product or slater determinant.
def calculate_basis(state,single_states_a,single_states_b,electron_config,system):
    basis_set = np.zeros((len(single_states_a),len(single_states_b),len(system.x),len(system.x)),dtype=np.float32)
    coefficients = np.zeros((len(single_states_a),len(single_states_a)),dtype=np.float32)
    completeness = 0
    if electron_config == "uu":
        for i in range(0,len(single_states_a)):
            for j in range(i,len(single_states_b)):
                basis_set[i][j] = (1/np.sqrt(2))*(np.outer(single_states_a[i],single_states_b[j])-np.outer(single_states_b[j],single_states_a[i]))
                coefficients[i][j] = innerproduct(state.full[:,0,:,0],basis_set[i][j],system,system)
                completeness = completeness + (coefficients[i][j])**2
    elif electron_config == "dd":
        for i in range(0,len(single_states_a)):
            for j in range(i,len(single_states_b)):
                basis_set[i][j] = (1/np.sqrt(2))*(np.outer(single_states_a[i],single_states_b[j])-np.outer(single_states_b[j],single_states_a[i]))
                coefficients[i][j] = innerproduct(state.full[:,1,:,1],basis_set[i][j],system,system)
                completeness = completeness + (coefficients[i][j])**2
    elif electron_config == "ud":
        for i in range(0,len(single_states_a)):
            for j in range(0,len(single_states_b)):
                basis_set[i][j] = (1/np.sqrt(2))*(np.outer(single_states_a[i],single_states_b[j]) + np.outer(single_states_b[j],single_states_a[i]))
                coefficients[i][j] = innerproduct(state.full[:,0,:,1],basis_set[i][j],system,system)
                completeness = completeness + (coefficients[i][j])**2
    elif electron_config == "du":
        for i in range(0,len(single_states_a)):
            for j in range(0,len(single_states_b)):
                basis_set[i][j] = np.outer(single_states_a[i],single_states_b[j])
                coefficients[i][j] = innerproduct(state.full[:,1,:,0],basis_set[i][j],system,system)
                completeness = completeness + (coefficients[i][j])**2

    return basis_set, coefficients, completeness

#get the basis set and coeffcients 
def orbitals(state,system,stateid,distance,electron_config,orbital_max_excitation,outputpath,potential_name,xgrid):
    orbital_max_excitation = int(orbital_max_excitation)
    hf_completeness = 0
    print(f"{datetime.datetime.now()}: Generating Orbital Basis Sets")
    

    #create single particle orbitals for a hartree-fock system
    max_excitation = 10

    #xgrid = np.linspace(-20,20,300)
    v_int = idea.interactions.softened_interaction(xgrid)
    v_ext_what = potential(xgrid,distance,potential_name)
    v_ext = (-4*np.exp(-((xgrid-distance)**2)/10) - 4.005*np.exp(-((xgrid+distance)**2)/10)) #gaussian1
    #print(np.sum(v_ext-v_ext_what))

    #this bodge works
    testsystem = idea.system.System(xgrid,v_ext,v_int,electrons=electron_config)
    teststate = idea.methods.hartree_fock.solve(testsystem,k=0,restricted=True,tol=1e-2)

    #doesnt????
    #testsystem = idea.system.System(xgrid,v_ext_what,v_int,electrons=electron_config)
    #teststate = idea.methods.hartree_fock.solve(testsystem,k=0)

    #what the actual fuck im so confused

    single_states_a = np.zeros((max_excitation+1,300),dtype=np.float32)
    single_states_b = np.zeros((max_excitation+1,300),dtype=np.float32)
    for i in range(0,max_excitation+1):
        if electron_config[0] == "u":
            single_states_a[i] = teststate.up.orbitals[:,i]
        if electron_config[0] == "d":
            single_states_a[i] = teststate.down.orbitals[:,i]
        if electron_config[1] == "u":
            single_states_b[i] = teststate.up.orbitals[:,i]
        if electron_config[1] == "d":
            single_states_b[i] = teststate.down.orbitals[:,i]

    #make sure inputted state is normalised
    state.full = state.full*(1/np.sqrt((np.sum(np.square(state.full))*system.dx*system.dx)))

    #make sure orbitals are normalised
    for i in range(0,len(single_states_a)):
        single_states_a[i] = single_states_a[i]*(1/np.sqrt((np.sum(np.square(single_states_a[i]))*system.dx)))
        single_states_b[i] = single_states_b[i]*(1/np.sqrt((np.sum(np.square(single_states_b[i]))*system.dx)))

    #calculate basis set & coefficients
    basis_set, coefficients, hf_completeness = calculate_basis(state,single_states_a,single_states_b,electron_config,system)
    
    #save coefficients & basis functions
    file = open(f"{outputpath}/orbitals/hartree-fock/coeffs-ID{str(stateid-1).zfill(4)}.pkl","wb")
    pickle.dump(coefficients,file)
    file.close()
    file = open(f"{outputpath}/orbitals/hartree-fock/single_orbitals_a-ID{str(stateid-1).zfill(4)}.pkl","wb")
    pickle.dump(single_states_a,file)
    file.close()
    file = open(f"{outputpath}/orbitals/hartree-fock/single_orbitals_b-ID{str(stateid-1).zfill(4)}.pkl","wb")
    pickle.dump(single_states_a,file)
    file.close()
    file = open(f"{outputpath}/orbitals/hartree-fock/basis-ID{str(stateid-1).zfill(4)}.pkl","wb")
    pickle.dump(basis_set,file)
    file.close()

    #plot single particle orbitals for both particles
    for i in range(0,len(single_states_a)):
        plt.plot(single_states_a[i]+(2*i),label=f"excitation: {i}")
        plt.legend()
        plt.xlabel("Position (Bohrs)")
        plt.title(f"hartree-fock orbitals, distance={distance}")
    plt.plot(system.x,system.v_ext,"g--",label="potential")
    plt.savefig(f"{outputpath}/orbitals/hartree-fock/plot_single_orbitals_a_ID{str(stateid-1).zfill(4)}.png")
    plt.close()

    for i in range(0,len(single_states_b)):
        plt.plot(system.x,single_states_b[i]+(2*i),label=f"excitation: {i}")
        plt.legend()
        plt.xlabel("Position (Bohrs)")
        plt.title(f"hartree-fock orbitals, distance={distance}")
    plt.plot(system.x,system.v_ext,"g--",label="potential")
    plt.savefig(f"{outputpath}/orbitals/hartree-fock/plot_single_orbitals_a_ID{str(stateid-1).zfill(4)}.png")
    plt.close()

    return hf_completeness
