
import numpy as np
from potential import *
#------------------------------------------------
#================================================
#=====INDIGO'S DOUBLE EXCITATION ASSEMBLER=======
#====================Idea========================
#===============PARAMETER FILE===================
#================================================
#------------------------------------------------


xgrid = np.linspace(-20,20,301)
potential_name = "symgaussian"
debugging = True #If true, outputs inner product grids for every state generated, even if rejected.
doubleexcitation = 5 #set if you know initial excitation, otherwise set to -1.
find_startpoint = 0 #If doubleexcitation=0, only excitations above this value will be searched. If doubleexcitation is known, set to 0.
initial_distance = 5 #initial distance of the wells from 0.
sensitivity = 5 #sensitivity of peak finder
limit = 50 #excitation number limit of the double excitation finder
abovedouble = 5 #number of excitations above the double excitation that will be generated during assembly
innerprod_tolerence = 0.5 #Tolerence for accepting states, e.g. tol=0.1 will accept states that has an inner product >0.9
distance_step = 0.25 #default distance steps
maxdivisions = 30 #max number of step divisions before the assembler gives up
electronconfig = "ud" #spin configuration of the electrons
outputpath = "../symgaussian-ud-e5"
job = "assemble" #"assemble" #"find" #"plotpotential"

non_interacting = True
hartree_fock = True
natural = True
orbital_max_excitation = 20
naturaltol = 5
