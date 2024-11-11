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
xgrid_maxrange = 30
xgrid_points = 300

#============ASSEMBLE SETTINGS===================
#WELL MOVING SETTINGS
#distances are given from centre (0)
starting_distance = 20
distance_step = 0.1
inner_prod_tolerance = 0.1

#================FIND SETTINGS===================
enable_finding_double = True
known_double_excitation = 7 #only needed if enable_finding_double=False
excitation_limit = 15
peakfinder_sensitivity = 20

#================OUTPUT SETTINGS=================
#OUTPUT SETTINGS
enable_gif_generation_density = True        
enable_gif_generation_wavefunction = True   
enable_gif_generation_energy = True         
enable_final_energy_graph = True            
save_all_states = True                      


