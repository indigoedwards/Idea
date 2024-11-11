#------------------------------------------------
#================================================
#=====INDIGO'S DOUBLE EXCITATION ASSEMBLER=======
#====================Idea========================
#===============PARAMETER FILE===================
#================================================
#------------------------------------------------

#===================JOB==========================
job = "assemble" #"find" #"plotpotential"

#=============GENERAL SETTINGS===================
#X-GRID SETTINGS
xgrid_start = -30
xgrid_end = 30
xgrid_points = 300
#FILE DIRECTORIES
output_file = ""
save_state_directory = ""
save_graph_directory = ""

#============ASSEMBLE SETTINGS===================
#WELL MOVING SETTINGS
#distances are given from centre (0)
starting_distance = 20
distance_step = 0.1
inner_prod_tolerance = 0.1
#OUTPUT SETTINGS
enable_gif_generation = True
gif_observables = ["density","wavefunction","energy","exch-energy","kin-energy"]
graph_final_state = True
final_state_graphs = ["density","wavefunction","exch-energy","kin-energy"]      
#FINDING EXCITATION SETTINGS
enable_finding_double = True
known_double_excitation = 7 #only needed if enable_finding_double=False

#================FIND SETTINGS===================
excitation_limit = 15
peakfinder_sensitivity = 20
#OUTPUT SETTINGS

#==========GENERAL OUTPUTS======================
output_observables = True     
output_energy = True
save_states = True
save_final_energy_graph = True
               



