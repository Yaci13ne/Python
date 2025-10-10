import random
def Read_matrix (T,N): 
        print("Enter the values of the matrix")
        for i in range (0,N) : 
                for j in range  (0,N) : 
                    print("T[%d][%d]= "%(i,j),end=' ') 
                    T[i][j]= int(input())


def Disp_matrix (T,N):
       for i in range(0,N) :
              print()
              for j in range (0,N):
                    print(T[i] [j],end=" ")
              print()      

def initial_matrix():

       N = random.randint(2,4)
       
       T =[[0 for j in range(0,N)] for i in range(0,N)]   

       for i in range (0,N) : 
                for j in range  (0,N) : 
                   T[i][j]= random.randint(0,10)     
       print("This is the matrix : ")
       Disp_matrix(T,N)
       return T

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
        
def Prod_Matrices(T, T2, N):
    prod = [[0 for j in range(N)] for i in range(N)]
    
    for i in range(N):
        for j in range(N):
            for k in range(N):
                prod[i][j] +=  T[i][k] * T2[k][j]
    print()
    print("Produit des matrices:")
    Disp_matrix(prod, N)

def Transp_Matrice(T,N) :
     transp =[[0 for i in range(N)]for j in range (N)]
     for i in range(0,N):
          for j in range(N):
               transp[i][j] = T[j][i]
     Disp_matrix(transp,N)
               
def TriangulaireSup_Matrice(T,N) : 
     flag =0 
     for i in range (0,N):
          for j in range (0,N):
               if j<i and T[i][j]!=0 :
                    flag = 1
                    print("the matrice isnt triangulaire sup ")
                    break
          if flag==1 : break
     
     if flag == 0 :
      print ("the matrice is triangulair sup")
  
def TriangulaireInf_Matrice(T,N) : 
     flag =0 
     for i in range (0,N):
          for j in range (0,N):
               if j>i and T[i][j]!=0 :
                    flag = 1
                    print("the matrice isnt triangulaire inf ")
                    break
          if flag==1 : break
     
     if flag == 0 :
      print ("the matrice is triangulair inf")
def Diagonal (T,N) :
     flag =0 
     for i in range (0,N):
          for j in range (0,N):
               if i!=j and T[i][j]!=0 :
                    flag = 1
                    print("the matrice isnt Diagonal")
                    break
          if flag==1 : break
     if flag == 0 :
      print ("the matrice is Diagonal")    

def Symmetric (T,N):
     for i in range (0,N):
          for j in range (0,N):
               if T[i][j]!=T[j][i] : 
                    flag = 1
                    print("the matrice isnt Symmetric")
                    break                        
          if flag==1 : break
     if flag == 0 :
      print ("the matrice is Symmetric  ")  




print("1 - Use an initial random matrix ")
print("2 - Create your own one ")
choose = int(input("Choose the number please: "))

if choose==1:
     T = initial_matrix()
     N = len(T)
     print("1 - calculate its transpose")
     print("2- test if it is triangularly superior")
     print("3- test if it is triangularly inferior")
     print("4- test if it is diagonal")
     print("5- test if it is Symmetric")
     print("6- See its identity matrix")
     operation1 = int(input("Choose the number please:  "))
     if operation1==1:
            Transp_Matrice(T,N)
     if operation1==2:
            TriangulaireSup_Matrice(T,N)
     if operation1==3:
            TriangulaireInf_Matrice(T,N)
     if operation1==4:
            Diagonal(T,N)
     if operation1==5:
            Symmetric(T,N)
     if operation1==6:
            Mat_identite(N)

if choose==2:
     
     while True :
        N= int(input("Enter N the size of the matrix: "))
        if N>=0:
          break

     T =[[0 for j in range(0,N)] for i in range(0,N)]   
     T2 =[[0 for j in range(0,N)] for i in range(0,N)] 
     Read_matrix(T,N)

     while True :
      print("1 - Display it.")
      print("2 - See its identity matrix")        
      print("3 - Add second matrix and Calculate the Sum between the two")        
      print("4 - Add second matrix and Calculate the product between the two ")          
      print("5- test if it is triangularly superior")
      print("6- test if it is triangularly inferior")
      print("7- test if it is diagonal")
      print("8- test if it is Symmetric")
      operation2 = int(input("Choose the number please:  "))
   
      if operation2==1:
            Disp_matrix(T,N)
      if operation2==2:
            Mat_identite(N)
      if operation2==3:
            Read_matrix(T2,N)
            Sum_Matrices(T,T2,N)
      if operation2==4:
            Read_matrix(T2,N)
            Prod_Matrices(T,T2,N)    
      if operation2==5:
            TriangulaireSup_Matrice(T,N)
      if operation2==6:
            TriangulaireInf_Matrice(T,N)   
      if operation2== 7:
            Diagonal(T,N)   
      if operation2== 8:
           Symmetric(T,N)

      answer = input("Continue ?(Y/N)")
      if answer == 'N' :
           break                    
                                        
          








