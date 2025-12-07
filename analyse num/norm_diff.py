import math



def norme_diff(X1, X2):
    s = 0
    for a, b in zip(X1, X2):
        s += (a - b)**2
    return math.sqrt(s)
