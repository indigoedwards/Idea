# Idea (Indigo's double excitation assembler)
![alt text](https://frogchairminecraft.co.uk/w/images/6/65/Idea_logo.png)
----------------------------
A python program for all your one dimentional double excitation needs :D

Idea is mainly based on iDEA https://github.com/iDEA-org/iDEA

-----------------------------
<h1>Requirements</h1>

* iDEA (indigo version): https://github.com/indigoedwards/iDEA-indigo
* numpy
* matplotlib
* maybe some other stuff i dont remember idk it should be a requirement of iDEA :)

------------------------------
<h1>Quickstart</h1>
Download Idea by cloning this repository

Make sure you have the correct requirements installed

Set output filepath in inputs.py

Run using the following console command:

OMP_NUM_THREADS=13 python3 ./main.py & > ./log.txt
:D


----------------------------
<h1>Functionality</h1>
Idea has three main functions: Plotting a potential, finding a double excitation (when far apart), and assembling a double excitation state by moving electrons togehter.
Idea is completely flexable for these tasks, it will take any potential as inputs and (might) still work! wow!!!1!

----------------------------
<h1>Progress</h1>
UPDATE: Idea WORKS!!!!!
yayyyyyyyyy :D
----------------------------
<h1>Inputs</h1>
Please write inputs into a param.txt. There is a sample one provided! 

* xgrid(beginning,end,steps): beginning and end are x coordinates of the limits of the model (in Bohrs), number of steps are the number of points on that grid.
* initial distance is the initial distance of both wells from 0.
* sensitivity is the sensitivity of the initial double excitation peak finder.
* limit is the excitation number limit for finding the initial double excitation.
* excitations above double is the number of excitations above the double excitation number which will be solved for during the movement process
* innerproduct tolerance is the tolerance for which inner products will be accepted. A tolerance of 0.1 means that any inner products over 0.9 will be accepted.
* distance step is the maximum and initial length of the steps during the movement phase. This is decreased if an inner product within tolerance is not found.
* max divisions is the maximum number of step divisions that will occour before an error is raised.

Please write your potential into potential.txt in python format. A sample is also provided.
This program works for wells that initially start split in space. Potentials should also approach 0 on the edges of the xgrid. 
