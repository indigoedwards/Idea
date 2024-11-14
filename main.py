from assemble import assemble
import numpy as np

xgrid = np.linspace(-30,30,300)
doubleexcitation = 7
initial_distance = 8
sensitivity = 20
limit = 50
abovedouble = 5
innerprod_tolerence = 0.1
distance_step = 0.25
maxdivisions = 4
outputpath = "../output"



print(assemble(xgrid,doubleexcitation,initial_distance,sensitivity,limit,abovedouble,innerprod_tolerence,distance_step,maxdivisions,outputpath))
