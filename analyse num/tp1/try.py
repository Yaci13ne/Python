import random

def Read_matrix(T, N): 
    print("Enter the values of the matrix:")
    for i in range(N): 
        for j in range(N): 
            print("T[%d][%d] = " % (i, j), end=' ') 
            T[i][j] = int(input())

def Disp_matrix(T, N):
    for i in range(N):
        print()
        for j in range(N):
            print(T[i][j], end=" ")
        print()      

def initial_matrix():
    N = random.randint(2, 4)
    T = [[0 for j in range(N)] for i in range(N)]   

    for i in range(N): 
        for j in range(N): 
            T[i][j] = random.randint(0, 10)     

    print("This is the matrix:")
    Disp_matrix(T, N)
    return T

def Mat_identite(N):
    id = [[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                id[i][j] = 1
    print("Identity matrix:")
    Disp_matrix(id, N) 
    return id             
                    
def Sum_Matrices(T, T2, N):
    s = [[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            s[i][j] = T[i][j] + T2[i][j]
    print("Sum of the two matrices:")
    Disp_matrix(s, N)
        
def Prod_Matrices(T, T2, N):
    prod = [[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                prod[i][j] += T[i][k] * T2[k][j]
    print("\nProduct of the matrices:")
    Disp_matrix(prod, N)

def Transp_Matrice(T, N):
    transp = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            transp[i][j] = T[j][i]
    print("Transpose of the matrix:")
    Disp_matrix(transp, N)
               
def TriangulaireSup_Matrice(T, N): 
    flag = 0 
    for i in range(N):
        for j in range(N):
            if j < i and T[i][j] != 0:
                flag = 1
                print("The matrix is not upper triangular.")
                break
        if flag == 1:
            break
    if flag == 0:
        print("The matrix is upper triangular.")
  
def TriangulaireInf_Matrice(T, N): 
    flag = 0 
    for i in range(N):
        for j in range(N):
            if j > i and T[i][j] != 0:
                flag = 1
                print("The matrix is not lower triangular.")
                break
        if flag == 1:
            break
    if flag == 0:
        print("The matrix is lower triangular.")

def Diagonal(T, N):
    flag = 0 
    for i in range(N):
        for j in range(N):
            if i != j and T[i][j] != 0:
                flag = 1
                print("The matrix is not diagonal.")
                break
        if flag == 1:
            break
    if flag == 0:
        print("The matrix is diagonal.")    

def Symmetric(T, N):
    flag = 0
    for i in range(N):
        for j in range(N):
            if T[i][j] != T[j][i]:
                flag = 1
                print("The matrix is not symmetric.")
                break                        
        if flag == 1:
            break
    if flag == 0:
        print("The matrix is symmetric.")  
def Determinant(T, N):
    id = Mat_identite(N)
    if T == id:
        return 1

    if TriangulaireSup_Matrice(T, N) or TriangulaireInf_Matrice(T, N):
        det = 1
        i = 0
        while i < N:
            det *= T[i][i]
            i += 1
        return det

    if N == 1:
        return T[0][0]

    if N == 2:
        return T[0][0]*T[1][1] - T[0][1]*T[1][0]

    if N == 3:
        T1 = [[T[1][1], T[1][2]], [T[2][1], T[2][2]]]
        T2 = [[T[1][0], T[1][2]], [T[2][0], T[2][2]]]
        T3 = [[T[1][0], T[1][1]], [T[2][0], T[2][1]]]
        det = (
            T[0][0]*Determinant(T1, 2)
            - T[0][1]*Determinant(T2, 2)
            + T[0][2]*Determinant(T3, 2)
        )
        return det

def SwapRows(T,N,row1,row2):
    r1 = row1-1
    r2 = row2-1
    i=0
    while (i<N):
        T[r1][i],T[r2][i] = T[r2][i],T[r1][i]
        i+=1


def SwapColumn(T,N,col1,col2):
    c1 = col1 -1 
    c2 = col2 -1
    i = 0
    while (i<N):
        T[i][col1],T[i][col2] = T[i][col2],T[i][col1]
        i+=1
    
    
    
    
T = [[0 for j in range(3)] for i in range(3)] 
Read_matrix(T,3)
Disp_matrix(T,3)
SwapColumn(T,3,1,2)
Disp_matrix(T,3)
