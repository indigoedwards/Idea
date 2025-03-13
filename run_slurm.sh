#!/bin/sh
#SBATCH --job-name=gaussian1_ud-indigo-Idea               # Job name
#SBATCH --output=./log-orbitaltest-ud.txt           # Standard out and error log
#SBATCH --mail-type=ALL                   # Specify when to mail (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=jcre500@york.ac.uk         # NB change uid to your username if wanting to send mail

#need ONE of the following two lines:
#SBATCH --partition=week         # priority queue for class work
#SBATCH --account=pet-double-2024           # specify your project account if NOT doing class work
#SBATCH --mem=32G

#customise these according to job size and time required:
#SBATCH --ntasks=40                         # Run 4 tasks...
#SBATCH --cpus-per-task=1                  # ...with each task using 1 core
#SBATCH --time=24:00:00                    # Time limit hrs:min:sec
#SBATCH --exclusive
#actual executable info now:

#tell user what is going on:
echo My working directory is `pwd`
echo Running job on host:
echo -e '\t'`hostname` at `date`
echo -e '\t'using $SLURM_NTASKS cores
echo


source ~/scratch/.venv/bin/activate
export PYTHONUNBUFFERED=TRUE
OMP_NUM_TREADS=13 python3 -u main.py
deactivate

echo
echo Job completed at `date`

