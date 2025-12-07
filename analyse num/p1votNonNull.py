from tp1_problem import *
from tp2_problem import *
from fct_elimination import fct_elimination


def Algo_trianNonNull(T, N, B):
    for k in range(N - 1):
        pivot = T[k][k]
        if pivot == 0:
            print("Erreur : pivot nul")
            return None
        fct_elimination(T, N, B, k, pivot)
        
def Algo_trianNonNull_rec(T, B, N, k):
    if k >= N - 1:
        return
    pivot = T[k][k]
    if pivot == 0:
        print("Erreur : pivot nul")
        return
    fct_elimination(T, N, B, k, pivot)
    Algo_trianNonNull_rec(T, B, N, k + 1)
    

if __name__ == "__main__":
    T = [[10, 5, 5,0], [2,5,7,4], [4,4,1,4], [-2,-2,1,-3]]
    B = [25, 1, 12, -10]

    Algo_trianNonNull(T, 4, B)
    X = Algo_remontee(T, 4, B)
    print("La solution est :")
    print(X)
