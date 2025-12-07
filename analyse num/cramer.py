from tp1_problem import * 


def method_cramer(T,N,B):
    determinant = Determinant(T, N)
    if(determinant == 0):
        print(" no unique solution.")
        return None
    X = [0 for i in range(N)] 
    for i in range(N):
        T_tmp = [row[:] for row in T] 
        for j in range(N):
            T_tmp[j][i] = B[j] 
    
        det_tmp = Determinant(T_tmp, N)
        X[i] = det_tmp / determinant

    if X is not None:
      print("la solution est: ")
      for i in range(N):
           print("x[%d] = %f" % (i, X[i])) 
    return X  

def method_cramer_rec(T,N,B,i,X=None):
    determinant = Determinant(T, N)
    if(determinant == 0):
        print(" no unique solution.")
        return None   
    if X is None:
        X = [0 for _ in range(N)]
    if i == N:
        return X
    else:
        cramer_calcul(T,N,B,determinant,i,X)
        return method_cramer_rec(T, N, B, i + 1, X)    
    

def cramer_calcul(T,N,B,determinant,i,X):
    T_tmp = [row[:] for row in T] 
    for j in range(N):
         T_tmp[j][i] = B[j] 
         det_tmp = Determinant(T_tmp, N)
         X[i] = det_tmp / determinant


T = [[3,1,6],[2,1,3],[1,1,1]]
B =[2,7,4]
X= method_cramer_rec(T,3,B,0)
print(X)