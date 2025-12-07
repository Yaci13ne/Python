from tp1_problem import *
from tp2_problem import *   


def Decomposition_LU(T,N):
    t=1
    U = T
    L = [[0 for _ in range(N)] for _ in range(N)]
    L= Mat_identite(N)
    for k in range(N):
        pivot = U[k][k]
        for i in range(k+1,N):
            q = U[i][k]
            U[i][k]= 0
            L[i][k] = q / pivot
            for j in range(k+1, N):
                U[i][j] = U[i][j] - U[k][j]*(q / pivot)
        print(f"\n etape k ={t}")
        print(f"U{t-1}=")  
        for row in U:
            print(row)
        print(f"L{t-1}=")
        for row in L:
            print(row)
        t+=1
                
    return L, U


def Decomposition_LU_rec(T, N, k=0, L=None):
    if L is None:
        L = Mat_identite(N)
    if k >= N - 1:
        return L, T
    calcul_decomposition_LU(T, N,L,k)
    return Decomposition_LU_rec(T, N, k + 1, L)

def calcul_decomposition_LU(T, N,L,k):
        pivot = T[k][k]
        for i in range(k + 1, N):
            q = T[i][k]
            L[i][k] = q / pivot
            for j in range(k, N):
                T[i][j] = T[i][j] - T[k][j] * (q / pivot)

if __name__ == "__main__":

    T = [[1,2,3],
         [1,1,2],
         [1,1,1]]
    B =[2,0,1]

    N = 3
    print("Décomposition LU itérative:")
    L, U = Decomposition_LU(T, N)
    print("Matrice L:")
    for row in L:
        print(row)
    print("Matrice U:")
    for row in U:
        print(row)
    
    X = Algo_descente(L,N,B)
    solution= Algo_remontee(U,N,X)
    for i in range (N):
        print("x[%d] = %f" % (i, solution[i]))

    
