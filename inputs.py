import numpy as np
from potential import *
#------------------------------------------------
#================================================
#=====INDIGO'S DOUBLE EXCITATION ASSEMBLER=======
#====================Idea========================
#===============PARAMETER FILE===================
#================================================
#------------------------------------------------


xgrid = np.linspace(-20,20,300)
potential_name = "gaussian3"
debugging = True #If true, outputs inner product grids for every state generated, even if rejected.
doubleexcitation = 29 #set if you know initial excitation, otherwise set to 0.
find_startpoint = 5 #If doubleexcitation=0, only excitations above this value will be searched. If doubleexcitation is known, set to 0.
initial_distance = 10 #initial distance of the wells from 0.
sensitivity = 10 #sensitivity of peak finder
limit = 50 #excitation number limit of the double excitation finder
abovedouble = 5 #number of excitations above the double excitation that will be generated during assembly
innerprod_tolerence = 0.1 #Tolerence for accepting states, e.g. tol=0.1 will accept states that has an inner product >0.9
distance_step = 0.25 #default distance steps
maxdivisions = 10 #max number of step divisions before the assembler gives up
electronconfig = "uu" #spin configuration of the electrons
outputpath = "../output"
job = "plotpotential" #"assemble" #"find" #"plotpotential"
