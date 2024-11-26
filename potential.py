#------------------------------------------------
#================================================
#=====INDIGO'S DOUBLE EXCITATION ASSEMBLER=======
#====================Idea========================
#===============POTENTIAL FILE===================
#================================================
#------------------------------------------------
import numpy as np

def potential(d):
    x = np.linspace(-20,20,300)

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


