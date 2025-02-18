import os
import glob
import shutil

def clearoutputs(output_filepath):
    is_file_path = os.path.isdir(name)
    if is_file_path:
        print("file path already exists - generating new path")
        while is_file_path:
            output_filepath = output_filepath+"_new"
            is_file_path = os.path.isdir(name)
    
    os.makedirs(f"{output_filepath}")
    
    #shutil.rmtree(f"{output_filepath}/")
    
    os.makedirs(f"{output_filepath}/wavefunctions")
    os.makedirs(f"{output_filepath}/innerprods")
    os.makedirs(f"{output_filepath}/densities")
    os.makedirs(f"{output_filepath}/debugging")
    f = open(f"{output_filepath}/energies.txt", "x")
    
    print(f"working directory is now {output_filepath}")

