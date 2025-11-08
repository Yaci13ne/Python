from fct_elimination import fct_elimination
from tp1_problem import *


def Algo_pivot_total(T,N,B):
    for k in range (0,N):
        p = T[k][k]
        l = k

        for i in range (k,N):
            if(T[i][k]>p):
                p = T[i][k]
                l = i

        if(l!=k):
            for j in range (k,N ):
                temp = T[k][j]
                T[k][j] = T[l][j]
                T[l][j]= temp

        fct_elimination(T,N,B,k,p)


if __name__ == "__main__":
    T = [
        [1, 3, 3],
        [2, 2, 5],
        [3, 2, 6]
    ]
    B = [-2, 7, 12]

    Algo_pivot_total(T, 3, B)
    X = Algo_remontee(T, 3, B)
    print("La solution est :")
    for i in range(3):
        print(f"x{i + 1} = {X[i]}")



            


                