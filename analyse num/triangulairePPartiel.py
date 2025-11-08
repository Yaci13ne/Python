from tp1_problem import *
from tp2_problem import *
from fct_elimination import fct_elimination
def Algo_trianPartiel(T, N, B):
    for k in range(N - 1):
        p = abs(T[k][k])
        l = k
        for i in range(k + 1, N):
            if abs(T[i][k]) > p:
                p = abs(T[i][k])
                l = i

        if l != k:
            T[k], T[l] = T[l], T[k]
            B[k], B[l] = B[l], B[k]
            print(f"Échange des lignes {k} et {l}:")
            for i in range(N):
                print(T[i], " | ", B[i])
            print("\n")

        pivot = T[k][k]
        if pivot == 0:
            print("Erreur : pivot nul après permutation")
            return None

        fct_elimination(T, N, B, k, pivot)
