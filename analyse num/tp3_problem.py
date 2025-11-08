from tp1_problem import *
from tp2_problem import *



def Algo_trianNonNull(T, N, B):
    for k in range(N - 1):
        pivot = T[k][k]
        if pivot == 0:
            print("Error: pivot nul")
            return None
        fct_elimination(T,N,B,k,pivot)

        
def fct_elimination (T,N,B,k,pivot):
        for i in range(k + 1, N):
          q = T[i][k]
          T[i][k] = 0
          B[i] = B[i] - (q / pivot) * B[k]
          for j in range(k + 1, N):
                 T[i][j] = T[i][j] - (q / pivot) * T[k][j]
                 
        for i in range (0,4):
        print(f"k = {i} ,[Disp_matrix(T,N))




def Algo_trianPartiel(T,N,B):
    for k in range (N-1):
        p = T[k][k]
        l = k

        for i in range (k-1 , N-1):
            if(T[i][k]>p):
                p = T[i][k]
                l = i

        if (l!=k) :
            for j in range (k-1, N-1 ):
                temp = T[k][j]
                T[k][j] =T[l][j]
        fct_elimination(T,N,B,k,p)

        






if __name__ == "__main__":
    T = [[10, 5, 5, 0],
         [2, 5, 7, 4],
         [4, 4, 1, 4],
         [-2, -2, 1, -3]]
    B = [25, 1, 12, -10]

    Algo_trianNonNull(T, 4, B)
    X = Algo_remontee(T, 4, B) 
    print("La solution est :")
    print (X)
