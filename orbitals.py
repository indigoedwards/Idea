import iDEA as idea
import numpy as np
import pickle
from innerprodgrid import innerproduct
import matplotlib.pyplot as plt
import scipy as sp
import datetime

#find number of nodes in a single particle wavefunction
def nodes(state,tol,dx):
    stateabs = abs(state)
    statesecond = 10*np.gradient(np.gradient(stateabs,dx),dx)
    big = max(statesecond)
    baseline = statesecond[10]*10
    idxs = []
    c = 0
    print(sp.signal.find_peaks(statesecond)[0])
    while big>tol:
        print(big)
        idx = list(statesecond).index(big)
        left = check_left(idx,statesecond,baseline)
        right = check_right(idx,statesecond,baseline)
        statesecond[left:right]=baseline
        c+=1
        idxs.append(idx)
        big = max(statesecond)
    return c#len(sp.signal.find_peaks(statesecond,threshold=0.005)[0])
    
def check_left(idx,arr,baseline):
    go = True
    while go:
        if arr[idx] > baseline and idx>0:
            idx-=1
        else:
            go = False
    return idx
    
def check_right(idx,arr,baseline):
    go = True
    while go:
        if arr[idx] > baseline and idx<len(arr):
            idx+=1
        else:
            go = False
    return idx

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
                basis_set[i][j] = np.outer(single_states_a[i],single_states_b[j])
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
def orbitals(non_interacting,hartree_fock,natural,state,system,stateid,distance,electron_config,orbital_max_excitation,naturaltol,outputpath):
    orbital_max_excitation = int(orbital_max_excitation)
    ni_completeness = 0
    hf_completeness = 0
    n_completeness = 0
    print(f"{datetime.datetime.now()}: Generating Orbital Basis Sets")
    if non_interacting == True:

        #initialise systems for both electrons
        system_a = idea.system.System(system.x,system.v_ext,system.v_int,electrons=electron_config[0])
        system_b = idea.system.System(system.x,system.v_ext,system.v_int,electrons=electron_config[1])

        #generate single particle states for both electrons
        single_states_a = np.zeros((orbital_max_excitation+1,300),dtype=np.float32)
        single_states_b = np.zeros((orbital_max_excitation+1,300),dtype=np.float32)
        for i in range(0,orbital_max_excitation+1):
            single_states_a[i] = idea.methods.interacting.solve(system_a,k=i,stopprint=True).space
            single_states_b[i] = idea.methods.interacting.solve(system_b,k=i,stopprint=True).space

        #make sure inputted state is normalised
        state.full = state.full*(1/np.sqrt((np.sum(np.square(state.full))*system.dx*system.dx)))

        #calculate basis set & coefficients
        basis_set, coefficients, ni_completeness = calculate_basis(state,single_states_a,single_states_b,electron_config,system)
        
        #save coefficients & basis functions
        file = open(f"{outputpath}/orbitals/non-interacting/coeffs-ID{str(stateid-1).zfill(4)}.pkl","wb")
        pickle.dump(coefficients,file)
        file.close()
        file = open(f"{outputpath}/orbitals/non-interacting/single_orbitals_a-ID{str(stateid-1).zfill(4)}.pkl","wb")
        pickle.dump(single_states_a,file)
        file.close()
        file = open(f"{outputpath}/orbitals/non-interacting/single_orbitals_b-ID{str(stateid-1).zfill(4)}.pkl","wb")
        pickle.dump(single_states_a,file)
        file.close()
        file = open(f"{outputpath}/orbitals/non-interacting/basis-ID{str(stateid-1).zfill(4)}.pkl","wb")
        pickle.dump(basis_set,file)
        file.close()

        #plot single particle orbitals for both particles
        for i in range(0,len(single_states_a)):
            plt.plot(system.x,single_states_a[i]+(2*i),label=f"excitation: {i}")
            plt.legend()
            plt.xlabel("Position (Bohrs)")
            plt.title(f"Non-interacting orbitals, distance={distance}")
        plt.plot(system.v_ext,"g--",label="potential")
        plt.savefig(f"{outputpath}/orbitals/non-interacting/plot_single_orbitals_a_ID{str(stateid-1).zfill(4)}.png")
        plt.close()

        for i in range(0,len(single_states_b)):
            plt.plot(system.x,single_states_b[i]+(2*i),label=f"excitation: {i}")
            plt.legend()
            plt.xlabel("Position (Bohrs)")
            plt.title(f"Non-interacting orbitals, distance={distance}")
        plt.plot(system.v_ext,"g--",label="potential")
        plt.savefig(f"{outputpath}/orbitals/non-interacting/plot_single_orbitals_a_ID{str(stateid-1).zfill(4)}.png")
        plt.close()

    if hartree_fock == True:

        #create single particle orbitals for a hartree-fock system
        max_excitation = 10
        teststate = idea.methods.hartree_fock.solve(system,k=0,silent=True)
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
        plt.plot(system.v_ext,"g--",label="potential")
        plt.savefig(f"{outputpath}/orbitals/hartree-fock/plot_single_orbitals_a_ID{str(stateid-1).zfill(4)}.png")
        plt.close()

        for i in range(0,len(single_states_b)):
            plt.plot(system.x,single_states_b[i]+(2*i),label=f"excitation: {i}")
            plt.legend()
            plt.xlabel("Position (Bohrs)")
            plt.title(f"hartree-fock orbitals, distance={distance}")
        plt.plot(system.v_ext,"g--",label="potential")
        plt.savefig(f"{outputpath}/orbitals/hartree-fock/plot_single_orbitals_a_ID{str(stateid-1).zfill(4)}.png")
        plt.close()

    if natural == True:
        #create density matrix
        density_a = 2*np.einsum('azby,czby->ac',state.full,state.full*system.dx)

        #solve eigenproblem
        coeffs, orbital = sp.linalg.eigh(density_a*system.dx)

        #pick all that have eigenvalues >0.00000001
        single = []
        coeffs_accept = []
        for i in range(0,len(system.x)):
            if coeffs[i]>naturaltol:
                single.append(orbital[:,i])
                coeffs_accept.append(coeffs[i])

        #normalise single particle wavefunctions
        for i in range(0,len(single)):
            single[i] = single[i]*(1/np.sqrt((np.sum(np.square(single[i]))*system.dx)))

        #get single particle wavefunctions into the correct order
        single_sorted = np.zeros((len(single),len(system.x)))
        single_nodes = []
        for i in range(0,len(single)):
            single_nodes.append(nodes(single[i],naturaltol,system.x[0]-system.x[1]))
        argsort_nodes = np.argsort(single_nodes)
        for i in range(0,len(single)):
            single_sorted[i] = single[argsort_nodes[i]]

        single_states_a = single_sorted
        single_states_b = single_sorted

        #make sure inputted state is normalised
        state.full = state.full*(1/np.sqrt((np.sum(np.square(state.full))*system.dx*system.dx)))

        #calculate basis set & coefficients
        basis_set, coefficients, n_completeness = calculate_basis(state,single_states_a,single_states_b,electron_config,system)
        
        #save coefficients & basis functions
        file = open(f"{outputpath}/orbitals/natural/coeffs-ID{str(stateid-1).zfill(4)}.pkl","wb")
        pickle.dump(coefficients,file)
        file.close()
        file = open(f"{outputpath}/orbitals/natural/single_orbitals_a-ID{str(stateid-1).zfill(4)}.pkl","wb")
        pickle.dump(single_states_a,file)
        file.close()
        file = open(f"{outputpath}/orbitals/natural/single_orbitals_b-ID{str(stateid-1).zfill(4)}.pkl","wb")
        pickle.dump(single_states_a,file)
        file.close()
        file = open(f"{outputpath}/orbitals/natural/basis-ID{str(stateid-1).zfill(4)}.pkl","wb")
        pickle.dump(basis_set,file)
        file.close()

        #plot single particle orbitals for both particles
        for i in range(0,len(single_states_a)):
            plt.plot(system.x,single_states_a[i]+(2*i),label=f"excitation: {i}")
            plt.legend()
            plt.xlabel("Position (Bohrs)")
            plt.title(f"natural orbitals, distance={distance}")
        plt.plot(system.v_ext,"g--",label="potential")
        plt.savefig(f"{outputpath}/orbitals/natural/plot_single_orbitals_a_ID{str(stateid-1).zfill(4)}.png")
        plt.close()

        for i in range(0,len(single_states_b)):
            plt.plot(system.x,single_states_b[i]+(2*i),label=f"excitation: {i}")
            plt.legend()
            plt.xlabel("Position (Bohrs)")
            plt.title(f"natural orbitals, distance={distance}")
        plt.plot(system.v_ext,"g--",label="potential")
        plt.savefig(f"{outputpath}/orbitals/natural/plot_single_orbitals_a_ID{str(stateid-1).zfill(4)}.png")
        plt.close()

    return ni_completeness, hf_completeness, n_completeness
