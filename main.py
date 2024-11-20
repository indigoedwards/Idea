from assemble import assemble
from testpotential import potential
from clearoutputs import clearoutputs
import iDEA as idea
from find import finddoubleexcitation
from gifs import gif_innerproducts, gif_densities, gif_wavefunctions
import numpy as np
import sys
import matplotlib.pyplot as plt
from testinputs import xgrid,doubleexcitation,initial_distance,sensitivity,limit,abovedouble,innerprod_tolerence,distance_step,maxdivisions,outputpath,job

#clearoutputs(outputpath)

if job == "assemble":
    print(assemble(xgrid,doubleexcitation,initial_distance,sensitivity,limit,abovedouble,innerprod_tolerence,distance_step,maxdivisions,outputpath))
    gif_wavefunctions(outputpath)
    gif_densities(outputpath)
    gif_innerproducts(outputpath)

elif job == "find":
    v_int = idea.interactions.softened_interaction(xgrid)
    system = idea.system.System(xgrid,potential(initial_distance),v_int,electrons="uu")
    print(f"Double excitation found at excitation {finddoubleexcitation(system,sensitivity,limit)}")

elif job == "plotpotential":
    v_int = idea.interactions.softened_interaction(xgrid)
    system = idea.system.System(xgrid,potential(initial_distance),v_int,electrons="uu")
    plt.plot(system.x, system.v_ext, "g--", label="Potential")
    plt.xlabel("x (Bohrs)")
    plt.ylabel("v_ext (Hartrees)")
    plt.legend()
    plt.savefig(f"{outputpath}/potentialplot.png")
    plt.close()

