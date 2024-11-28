#------------------------------------------------
#================================================
#=====INDIGO'S DOUBLE EXCITATION ASSEMBLER=======
#====================Idea========================
#===============POTENTIAL FILE===================
#================================================
#------------------------------------------------
import numpy as np

def potential(x,d,potential_name):

    if potential_name == "triangular":
        potential1 = np.zeros(300)
        potential2 = np.zeros(300)
        for xindex in range(0,len(x)):
            if x[xindex]<=-d-2:
                potential1[xindex] = 0
            if -d-2<x[xindex]<=-d:
                potential1[xindex] = -2*(x[xindex]+d)-4
            if -d<x[xindex]<=-d+2:
                potential1[xindex] = 2*(x[xindex]+d)-4
            if -d+2<x[xindex]:
                potential1[xindex] = 0
        for xindex in range(0,len(x)):
            if x[xindex]<=d-2:
                potential2[xindex] = 0
            if d-2<x[xindex]<=d:
                potential2[xindex] = -2*(x[xindex]-d)-4.001
            if d<x[xindex]<=d+2:
                potential2[xindex] = 2*(x[xindex]-d)-4.001
            if d+2<x[xindex]:
                potential2[xindex] = 0

        return potential1 + potential2
    
    if potential_name == "gaussian1":
        return (-4*np.exp(-((x-d)**2)/10) - 4.005*np.exp(-((x+d)**2)/10))



