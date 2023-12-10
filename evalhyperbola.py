import math

a = None
b = None
c = None
l = {}

x = None
y = None
h = None
k = None
f1 = None
f2 = None
v1 = None
v2 = None
c1 = None
c2 = None


twos = "f1f2v1v2c1c2"
two_vars = [str(twos[x:x+2]) for x in range(0, len(twos), 2)]
one_vars = list("abcxyhkl")

vector_vars = two_vars + list("xyhk")
scalar_vars = list("abc")

given_vars = two_vars + one_vars


while True:
    inp = input("> ")
    if inp.startswith("eval"):
        [_, eq] = inp.split(" ", 1)
        print(eval(eq))
    elif inp.startswith("set"):
        [_, var, eq] = inp.split(" ", 2)
        
        if var.startswith("l[\""):
            pass
        elif var not in given_vars:
            print("invalid variable", var)
            continue

        globals()[var] = eval(eq)
    elif inp.lower() in ['exit', "close", "ex", "x"]:
        break 
    elif inp.startswith("pyh"):
        [_, var] = inp.split(" ", 1)

        if var not in list("abc"):
            print("invalid variable", var)
            continue

        match var:
            case 'a':
                a = math.sqrt(c ** 2 - b ** 2)
            case 'b':
                b = math.sqrt(c ** 2 - a ** 2)
            case 'c':
                c = math.sqrt(a ** 2 + b ** 2)
            case _:
                print("Reached Unreachable")
                continue
    elif inp.startswith("dst"):
        [_, p1, p2, dest] = inp.split(" ", 3)

        if p1 not in vector_vars:
            print(f"'{p1}' not inteded to be use as a Vector")
            continue

        if p2 not in vector_vars:
            print(f"'{p2}' not inteded to be use as a Vector")
            continue

        if p2 not in vector_vars:
            print(f"'{p2}' not inteded to be use as a Vector")
            continue

        p1 = globals()[p1]
        p2 = globals()[p2]

        dst = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

        globals()[dest] = dst
        print(f"Distance has been stored in {dest}")
    else:
       print(f"unknown {inp}") 
