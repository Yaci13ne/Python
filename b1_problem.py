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


print("1 - Use an initial random matrix")
print("2 - Create your own matrix")
choose = int(input("Choose a number: "))

if choose == 1:
    T = initial_matrix()
    N = len(T)
    while True:

     print("1 - Calculate its transpose")
     print("2 - Test if it is upper triangular")
     print("3 - Test if it is lower triangular")
     print("4 - Test if it is diagonal")
     print("5 - Test if it is symmetric")
     print("6 - Display its identity matrix")
     operation1 = int(input("Choose a number: "))
     if operation1 == 1:
         Transp_Matrice(T, N)
     if operation1 == 2:
        TriangulaireSup_Matrice(T, N)
     if operation1 == 3:
        TriangulaireInf_Matrice(T, N)
     if operation1 == 4:
        Diagonal(T, N)
     if operation1 == 5:
        Symmetric(T, N)
     if operation1 == 6:
         Mat_identite(N)

     answer = input("Continue? (Y/N): ")
     if answer.upper() == 'N' or 'No':
            break 


if choose == 2:
    while True:
        N = int(input("Enter N (the size of the matrix): "))
        if N > 0:
            break

    T = [[0 for j in range(N)] for i in range(N)]   
    T2 = [[0 for j in range(N)] for i in range(N)] 
    Read_matrix(T, N)

    while True:
        print("1 - Display it")
        print("2 - Display its identity matrix")        
        print("3 - Add a second matrix and calculate their sum")        
        print("4 - Add a second matrix and calculate their product")          
        print("5 - Test if it is upper triangular")
        print("6 - Test if it is lower triangular")
        print("7 - Test if it is diagonal")
        print("8 - Test if it is symmetric")
        operation2 = int(input("Choose a number: "))
   
        if operation2 == 1:
            Disp_matrix(T, N)
        if operation2 == 2:
            Mat_identite(N)
        if operation2 == 3:
            Read_matrix(T2, N)
            Sum_Matrices(T, T2, N)
        if operation2 == 4:
            Read_matrix(T2, N)
            Prod_Matrices(T, T2, N)    
        if operation2 == 5:
            TriangulaireSup_Matrice(T, N)
        if operation2 == 6:
            TriangulaireInf_Matrice(T, N)   
        if operation2 == 7:
            Diagonal(T, N)   
        if operation2 == 8:
            Symmetric(T, N)

        answer = input("Continue? (Y/N): ")
        if answer.upper() == 'N' or 'No':
            break 
