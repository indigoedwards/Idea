#!/usr/bin/bash

source ~/venv/bin/activate
script_return=$(OMP_NUM_THREADS=13 python3 -u main.py)
echo "$script_return" > ../log.txt
