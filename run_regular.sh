 #!/usr/bin/bash

source ~/venv/bin/activate
OMP_NUM_THREADS=13 python3 -u main.py > log.txt
