# Idea (Indigo's double excitation assembler)
![alt text](https://indigoedwards.org/otherimages/idealogo.png)
----------------------------
A python program for all your one dimentional double excitation needs :D

Idea is mainly based on iDEA https://github.com/iDEA-org/iDEA

[![Example](https://img.youtube.com/vi/5gbLfAoBN3Q/0.jpg)](https://youtu.be/5gbLfAoBN3Q)

Above is a video showing the data that results from a gaussian input potential.

-----------------------------
<h1>Requirements</h1>

* iDEA (indigo version): https://github.com/indigoedwards/iDEA-indigo
* numpy
* matplotlib
* plotext
* and all requirements of the above

------------------------------
<h1>Quickstart</h1>
Download Idea by cloning this repository

Make sure you have the correct requirements installed

Set output filepath in inputs.py

Run either using the bash files for normal console running or slurm running
By default these use 13 cores.
:D

![alt text](https://indigoedwards.org/otherimages/DOUBLEEXCITATION.png)

----------------------------
<h1>Functionality</h1>
Idea has three main functions: Potential plotting, finding a double excitation (when far apart), and assembling a double excitation state by moving electrons togehter.
Idea is completely flexable for these tasks, it will take any potential as inputs and (might) still work! wow!!!1!

The main task is assembling. This begins by finding the excitation number of the lowest energy double excitation when the electrons are far apart (low interacting limit). The potentials are then moved together (the movement of potentials can be seen in the gif generated by the plot potential task), at each distance step, the inner products of every excitation at the last distance and the excitations at the new distance are calculated, producing the inner product grids. If there is an inner product found over the tolerance set in the input file, the state is accepted and the program moves on to the next distance. If a high enough inner product is not found, the distance step is halved and the process repeats until the max divisions is hit. Once an accepted state is found at a distance of 0, the program ends with the double excitation being found.
If you have any questions please dont hesitate to get in contact with me! indigo.edwards@york.ac.uk.

---------------------------
<h1>Inputs</h1>
Inputs are taken from the inputs.py file. Input descriptions are below

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
