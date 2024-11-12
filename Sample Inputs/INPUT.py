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


starting-separation = 10


#============PLOT POTENTIAL SETTINGS=============

#============ASSEMBLE SETTINGS===================
#WELL MOVING SETTINGS
#distances are given from centre (0)
distance_step = 0.1 #req if assemble
inner_prod_tolerance = 0.1 #req if assemble
excitations_above_double = 5 #NEW req if assemble
#OUTPUT SETTINGS
enable_gif_generation = True # assume false
gif_observables = ["density","wavefunction","energy","exch-energy","kin-energy"] #req if gif ^
generate_innerproduct_gif = True #NEW assume false, requires save_states=True
graph_final_state = True # assume false
final_state_graphs = ["density","wavefunction","exch-energy","kin-energy"] # req if ^
#FINDING EXCITATION SETTINGS
enable_finding_double = True
known_double_excitation = 7 #only needed if enable_finding_double=False

#================FIND SETTINGS===================
excitation_limit = 15 # req if enable finding double 
peakfinder_sensitivity = 20 # req if enable finding double
#OUTPUT SETTINGS

#==========GENERAL OUTPUTS====================== # assume false
output_observables = True     
output_energy = True
save_states = True
save_final_energy_graph = True
               



