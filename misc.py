

#Writing to output file
def writetooutput(message,output_filename):
    with open(output_filename,"a") as file:
        file.write(f"{message}\n")