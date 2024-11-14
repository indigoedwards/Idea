import numpy as np
import matplotlib.pyplot as plt
import iDEA as idea

#save observable numbers & graphs

def save_observables(state,system,excitation,newdistance,olddistance,outputpath,stateid,innerprodgrid):

    #make wavefunction plot
    plt.imshow(state.allfull[...,excitation][...,0,...,0], cmap="seismic", vmax=0.75, vmin=-0.75)
    plt.xlabel("x, position of electron 1 (Bohrs)")
    plt.ylabel("x', poisition of electron 2 (Bohrs)")
    plt.title(f"Distance from origin = {newdistance}")
    plt.gca().invert_yaxis()
    plt.savefig(f"{outputpath}/wavefunctions/Wavefuntion-ID{str(stateid).zfill(4)}")
    plt.close()

    #make density plot
    state.full = state.allfull[...,excitation]
    plt.plot(system.x, idea.observables.density(system, state=state), "m-", label="Charge Density")
    plt.plot(system.x, system.v_ext, "g--", label="Potential")
    plt.xlabel("x (Bohrs)")
    plt.ylabel("v_ext / charge density")
    plt.title(f"Distance from origin = {newdistance}")
    plt.legend()
    plt.savefig(f"{outputpath}/densities/Density-ID{str(stateid).zfill(4)}")
    plt.close()

    #make inner prod grid
    if innerprodgrid != 0:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        im = ax.imshow(innerprodgrid,cmap="Purples",vmin=0,vmax=1)
        plt.ylabel(f"Excitation of state at distance={round(olddistance,2)}")
        plt.xlabel(f"Excitation of state at distance={round(newdistance,2)}")
        for (j,i),label in np.ndenumerate(innerprodgrid):
            ax.text(i,j,round(label,2),ha="center", va="center")
        fig.colorbar(im,label="Inner product",boundaries=np.linspace(0, 1, 11))
        plt.savefig(f"{outputpath}/innerprods/innerprod-ID{str(stateid-1).zfill(4)}")
        plt.close()
    
    #save energy
    with open(f"{outputpath}/energies.txt","a") as file:
        file.write(f"{str(newdistance)},{str(state.allenergy[excitation])}\n")
    

    return