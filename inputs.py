import numpy as np
#------------------------------------------------
#================================================
#=====INDIGO'S DOUBLE EXCITATION ASSEMBLER=======
#====================Idea========================
#===============PARAMETER FILE===================
#================================================
#------------------------------------------------


xgrid = np.linspace(-20,20,300)
doubleexcitation = 0
initial_distance = 10
sensitivity = 10
limit = 50
abovedouble = 5
innerprod_tolerence = 0.1
distance_step = 0.25
maxdivisions = 10
outputpath = "../output"
job = "assemble" #"find" #"plotpotential"
