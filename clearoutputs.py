import os
import glob
import shutil

def clearoutputs(output_filepath):

    shutil.rmtree(f"{output_filepath}/")
    
    os.makedirs(f"{output_filepath}/wavefunctions")
    os.makedirs(f"{output_filepath}/innerprods")
    os.makedirs(f"{output_filepath}/densities")
    os.makedirs(f"{output_filepath}/debugging")
    f = open(f"{output_filepath}/energies.txt", "x")

