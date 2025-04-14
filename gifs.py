import iDEA as idea
import glob
import contextlib
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np




def gif_wavefunctions(outputpath):
    #create gifs from saved plots
    fp_in = f"{outputpath}/wavefunctions/*.png"
    fp_out = f"{outputpath}/wavefunctions.gif"
    with contextlib.ExitStack() as stack:
        # lazily load images
        imgs = (stack.enter_context(Image.open(f))
                for f in sorted(glob.glob(fp_in)))
        # extract  first image from iterator
        img = next(imgs)
        # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
        img.save(fp=fp_out, format='GIF', append_images=imgs,
                save_all=True, duration=400, loop=0)
    return
        
def gif_densities(outputpath):
    #create gifs from saved plots
    fp_in = f"{outputpath}/densities/*.png"
    fp_out = f"{outputpath}/densities.gif"
    with contextlib.ExitStack() as stack:
        # lazily load images
        imgs = (stack.enter_context(Image.open(f))
                for f in sorted(glob.glob(fp_in)))
        # extract  first image from iterator
        img = next(imgs)
        # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
        img.save(fp=fp_out, format='GIF', append_images=imgs,
                save_all=True, duration=400, loop=0)
    return

def gif_innerproducts(outputpath):
    #create gifs from saved plots
    fp_in = f"{outputpath}/innerprods/*.png"
    fp_out = f"{outputpath}/innerproduct.gif"
    with contextlib.ExitStack() as stack:
        # lazily load images
        imgs = (stack.enter_context(Image.open(f))
                for f in sorted(glob.glob(fp_in)))
        # extract  first image from iterator
        img = next(imgs)
        # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
        img.save(fp=fp_out, format='GIF', append_images=imgs,
                save_all=True, duration=400, loop=0)
    return

def energy_graph(outputpath):
        data = []
        with open(f"{outputpath}/energies.txt","r") as file:
                arr = [line.strip().split(",") for line in file.readlines()]
                data.append(np.array(arr,dtype=np.float64))
        data = data[0]

        data = data.transpose()

        plt.plot(data[1],data[3])
        plt.gca().invert_xaxis()
        plt.xlabel("Distance from origin (Bohrs)")
        plt.ylabel("Energy of double excitation (Hartrees)")
        plt.savefig(f"{outputpath}/energies.png")
        return
