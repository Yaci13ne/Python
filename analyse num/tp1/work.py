def Read_matrix (T,N): 
        for i in range (0,N) : 
                for j in range  (0,N) : 
                    print("T[%d][%d]"%(i,j),end=' ') 
                    T[i][j]= int(input())


def Disp_matrix (T,N):
       for i in range(0,N) :
              print()
              for j in range (0,N):
                    print(T[i] [j],end=" ")
              print()      

def Mat_identite(N):
    id =[[0 for j in range(0,N)] for i in range(0,N)]
    for i in range(0,N):
        for j in range(0,N):
              if i == j :
                    id[i][j] = 1
    Disp_matrix(id,N)
              
                    
def Sum_Matrices(T,T2,N):
        sum =[[0 for j in range(0,N)] for i in range(0,N)]
        for i in range(0,N):
              for j in range(0,N):
                sum[i][j] = T[i][j] + T2[i][j]
        Disp_matrix(sum,N)
        return sum
        
def Prod_Matrices(T, T2, N):
    prod = [[0 for j in range(N)] for i in range(N)]
    
    for i in range(N):
        for j in range(N):
            for k in range(N):
                prod[i][j] =  prod[i][j] + T[i][k] * T2[k][j]
    print()
    print("Produit des matrices:")
    Disp_matrix(prod, N)
    return prod

def Transp_Matrice(T,N) :
     transp =[[0 for i in range(N)]for j in range (N)]
     for i in range(0,N):
          for j in range(N):
               transp[i][j] = T[j][i]
     Disp_matrix(transp,N)
               
def TriangulaireSup_Matrice(T,N) : 



N = 3
T =[[0 for j in range(0,N)] for i in range(0,N)]
T2 =[[0 for j in range(0,N)] for i in range(0,N)]

print("Read values of matrix T:")
Read_matrix (T,N)
print("Read values of matrix T2:")
Read_matrix (T2,N)
print("The display of matrix T:")
Disp_matrix(T,N)
print("identity matrix of T:")
Mat_identite(N)
Prod_Matrices(T,T2,N)  

print("transpose de matrix T:")

Transp_Matrice(T,N)

                       #function determinant recursion 