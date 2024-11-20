from assemble import assemble
from testpotential import potential
from clearoutputs import clearoutputs
import iDEA as idea
from find import finddoubleexcitation
from gifs import gif_innerproducts, gif_densities, gif_wavefunctions, energy_graph
from title import printtitle
import numpy as np
import sys
import matplotlib.pyplot as plt
from testinputs import xgrid,doubleexcitation,initial_distance,sensitivity,limit,abovedouble,innerprod_tolerence,distance_step,maxdivisions,outputpath,job

clearoutputs(outputpath)
printtitle()

if job == "assemble":
    excitation, numaccepted, numrejected, numtotal = assemble(xgrid,doubleexcitation,initial_distance,sensitivity,limit,abovedouble,innerprod_tolerence,distance_step,maxdivisions,outputpath)
    print(f"Final excitation number: {excitation}")
    print(f"Total states generated: {numtotal}")
    print(f"States accepted: {numaccepted}")
    print(f"States rejected: {numrejected}")
    gif_wavefunctions(outputpath)
    gif_densities(outputpath)
    gif_innerproducts(outputpath)
    energy_graph(outputpath)

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

