import numpy as np
import matplotlib.pyplot as plt
from settings import Settings
import os

DIGITS = ["0","1","2","3","4","5","6","7","8","9"]
OPS = ["(",")",".","*","+","/","-","^"]
FUNCS = ["arcsinh","arccosh","arctanh",
         "arctan","arcsin","arccos",
         "sinh","cosh","tanh",
         "exp","log","sin","cos","tan"]
NPFUNCS = ["np.arcsinh","np.arccosh","np.arctanh",
         "np.arctan","np.arcsin","np.arccos",
         "np.sinh","np.cosh","np.tanh",
         "np.exp","np.log","np.sin","np.cos","np.tan"]
VARS = ["sep","x"]

ALLOWED_JOBS = ["assemble", "find", "plot-potential"]

def read_potential_file():
    with open("potential.txt","r") as file:
        equ = file.read().replace(" ","")
    test_equ = equ
    for func in FUNCS:
        test_equ = test_equ.replace(func,"")
    for var in VARS:
        test_equ = test_equ.replace(var,"")
    for op in OPS:
        test_equ = test_equ.replace(op,"")
    for dig in DIGITS:
        test_equ = test_equ.replace(dig,"")

    if test_equ == "":
        for i in range(len(FUNCS)):
            equ = equ.replace(FUNCS[i],NPFUNCS[i])
        equ = equ.replace("^","**")
        code = compile(equ,"<string>","eval")
        for name in code.co_names:
            if name not in FUNCS+VARS+["np"]:
                raise NameError(f"Use of {name} not allowed")
            
        x = np.linspace(-10,10,150)
        sep = 5
        ALLOWED = {"sep":sep,"x":x}
        potential = eval(code,{"__builtins__": {},"np":np},ALLOWED)
        plt.plot(x,potential)
        plt.show()

def read_param_file():
    with open("param.txt","r") as file:
        inputfile = [line.strip() for line in file.readlines()]
    inputs = []
    for line in inputfile:
        if line != "" and line[0] != "#":
            inputs.append(line)
    inputs = [line.split("#")[0].strip() for line in inputs]
    for i in range(len(PARAMETERS)):
        lines = [line for line in inputs if PARAMETERS[i] in line]
        PARAM_CHECKS[i](lines)

def job_checker(inputs):
    if len(inputs) == 0:
        raise Exception("no job specified")
    elif len(inputs) > 1:
        raise Exception("too many jobs specified, only one job may be specified")
    arg = inputs[0].split(":")[-1].strip()
    if arg not in ALLOWED_JOBS:
        raise Exception("not an allowed job")
    s.set_job(arg)

def xgrid_checker(inputs):
    if len(inputs) == 0:
        raise Exception("no xgrid parameters specified")
    elif len(inputs) < 3:
        raise Exception("missing xgrid parameters, requires xgrid-min, xgrid-max, xgrid-points")
    elif len(inputs) > 3:
        raise Exception("too many xgrid parameters")
    args = {}
    p = []
    for line in inputs:
        param = line.split(":")[0].strip()
        arg = line.split(":")[1].strip()
        if param == "xgrid-min" or param == "xgrid-max":
            try:
                arg = float(arg)
            except ValueError:
                raise Exception(f"{param} needs to be a float")
        elif param == "xgrid-points":
            try:
                arg = int(arg)
            except ValueError:
                raise Exception("xgrid-points needs to be an integer")
            if arg < 1:
                raise Exception("number of points must be greater than zero")
        args[param] = arg
        p.append(param)
    if len(list(set(p))) != 3:
        raise Exception("duplicate parameters specified, specified parameters must be xgrid-min, xgrid-max, xgrid-points")
    s.set_xgrid(args)

def path_checker(inputs):
    if len(inputs) == 0:
        raise Exception("no output path specified")
    elif len(inputs) > 3:
        raise Exception("too many output paths specified")
    
    print(inputs)
    print(os.getcwd())

PARAMETERS = ["job","xgrid","path"]
PARAM_CHECKS = [job_checker,xgrid_checker,path_checker]

s = Settings()

read_param_file()

print(s)