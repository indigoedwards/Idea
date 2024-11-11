import numpy as np
import matplotlib.pyplot as plt

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

read_potential_file()