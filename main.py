from assemble import assemble
import numpy as np
import sys

xgrid = np.linspace(-30,30,300)
doubleexcitation = 7
initial_distance = 6.25
sensitivity = 20
limit = 50
abovedouble = 5
innerprod_tolerence = 0.1
distance_step = 0.25
maxdivisions = 8
outputpath = "../output"

print("test")
sys.stdout.flush()

print(assemble(xgrid,doubleexcitation,initial_distance,sensitivity,limit,abovedouble,innerprod_tolerence,distance_step,maxdivisions,outputpath))
