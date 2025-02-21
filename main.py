from assemble import assemble
import plotext
from potential import potential
from clearoutputs import clearoutputs
import iDEA as idea
from find import finddoubleexcitation
from gifs import gif_innerproducts, gif_densities, gif_wavefunctions, energy_graph
from potential import create_potential_gif
from title import printtitle
import numpy as np
import sys
import matplotlib.pyplot as plt
from inputs import xgrid,potential_name,debugging,find_startpoint,doubleexcitation,initial_distance,sensitivity,limit,abovedouble,innerprod_tolerence,distance_step,maxdivisions,electronconfig,outputpath,job

outputpath = clearoutputs(outputpath)
print(printtitle(),flush=True)
print("-----------------------------------------------------------------------------------",flush=True)

if job == "assemble":
    excitation, numaccepted, numrejected, numtotal = assemble(xgrid,potential_name,debugging,find_startpoint,doubleexcitation,initial_distance,sensitivity,limit,abovedouble,innerprod_tolerence,distance_step,maxdivisions,electronconfig,outputpath)
    print(f"Final excitation number: {excitation}",flush=True)
    print(f"Total states generated: {numtotal}",flush=True)
    print(f"States accepted: {numaccepted}",flush=True)
    print(f"States rejected: {numrejected}",flush=True)
    gif_wavefunctions(outputpath)
    gif_densities(outputpath)
    gif_innerproducts(outputpath)
    energy_graph(outputpath)

elif job == "find":
    v_int = idea.interactions.softened_interaction(xgrid)
    system = idea.system.System(xgrid,potential(xgrid,initial_distance,potential_name),v_int,electrons=electronconfig)
    print(f"Double excitation found at excitation {finddoubleexcitation(system,sensitivity,limit,find_startpoint,outputpath)}",flush=True)

elif job == "plotpotential":
    v_int = idea.interactions.softened_interaction(xgrid)
    system = idea.system.System(xgrid,potential(xgrid,initial_distance,potential_name),v_int,electrons=electronconfig)
    plt.plot(system.x, system.v_ext, "g--", label="Potential")
    plt.xlabel("x (Bohrs)")
    plt.ylabel("v_ext (Hartrees)")
    plt.legend()
    plt.savefig(f"{outputpath}/potentialplot.png")
    plt.close()
    plotext.plot(system.x, system.v_ext)
    plotext.show()
    create_potential_gif(xgrid,initial_distance,potential_name,outputpath)
    print("Finished plotting potential :D",flush=True)

