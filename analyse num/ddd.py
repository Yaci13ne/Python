from tp1_problem import *
from tp2_problem import *

def fct_elimination(T, N, B, k, pivot):
    for i in range(k + 1, N):
        q = T[i][k]
        T[i][k] = 0
        B[i] = B[i] - (q / pivot) * B[k]
        for j in range(k + 1, N):
            T[i][j] = T[i][j] - (q / pivot) * T[k][j]
    print(f"Matrice après élimination de la colonne {k}:")
    for i in range(N):
        print(T[i], " | ", B[i])
    print("\n")


def Algo_trianNonNull(T, N, B):
    for k in range(N - 1):
        pivot = T[k][k]
        if pivot == 0:
            print("Erreur : pivot nul")
            return None
        fct_elimination(T, N, B, k, pivot)


def Algo_trianPartiel(T, N, B):
    for k in range(N - 1):
        # Recherche du plus grand pivot
        p = abs(T[k][k])
        l = k
        for i in range(k + 1, N):
            if abs(T[i][k]) > p:
                p = abs(T[i][k])
                l = i

        # Échange des lignes si nécessaire
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


if __name__ == "__main__":
    T = [
        [1, 6, 9],
        [2, 1, 2],
        [3, 6, 9]
    ]
    B = [1, 2, 3]

    Algo_trianPartiel(T, 3, B)
    X = Algo_remontee(T, 3, B)
    print("La solution est :")
    for i in range(3):
        print(f"x{i + 1} = {X[i]}")
