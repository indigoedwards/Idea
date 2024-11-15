import os
import glob


def clearoutputs(output_filepath):
    
    files = glob.glob(f'{output_filepath}/*')
    for f in files:
        os.remove(f)
    
    os.makedirs(f"{output_filepath}/output/wavefunctions")
    os.makedirs(f"{output_filepath}/output/innerprods")
    os.makedirs(f"{output_filepath}/output/densities")
    f = open(f"{output_filepath}/energies.txt", "x")

