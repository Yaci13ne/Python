<<<<<<< HEAD
'''

'''

from tp1_problem import *

def Lire_Systeme(T, B,N):
    Read_matrix(T, N)
    print("Enter the values of the vector B:")
    for i in range(N):
      B[i] = int(input("B[%d] = " % (i)))


def afficher_Systeme(T, B,N):
    print("The system is:")
    for i in range(N):
        for j in range(N):
            print(T[i][j], end=" ")
        print("| %d" % (B[i]))



def Algo_descente(T, N,B):
    if TriangulaireInf_Matrice(T, N)== False:
        print("la matrice n'est pas triangulaire inferieure")
        return None
    
    X= [0 for i in range(N)] 
    X[0]= B[0]/T[0][0]
    for i in range(1,N):
        somme=0
        for j in range(0,i):
            somme+= T[i][j]*X[j]
        X[i]=float((B[i]-somme)/T[i][i])
    return X

def Algo_descente_rec(T, N, B, i, X=None):
    if TriangulaireInf_Matrice(T, N) == False:
        print("La matrice n'est pas triangulaire inférieure")
        return None

    if X is None:
        X = [0 for _ in range(N)]

    if i == 0:
        X[i] = B[i] / T[i][i]
    else:
        X = Algo_descente_rec(T, N, B, i - 1, X)
        calc_descent(T, N, B, i, X)

    return X

def calc_descent(T,B,X):
        somme=0
        for j in range(0,i):
            somme+= T[i][j]*X[j]
        X[i]=float((B[i]-somme)/T[i][i])   


def Algo_remontee(T, N,B): 
    if TriangulaireSup_Matrice(T, N)== False:
        print("la matrice n'est pas triangulaire superieure")
        return None
    X= [0 for i in range(N)] 
    X[N-1]= B[N-1]/T[N-1][N-1]
    for i in range(N-2,-1,-1):
        somme=0
        for j in range(i+1,N):
            somme+= T[i][j]*X[j]
        X[i]=float((B[i]-somme)/T[i][i])
    return X

def Algo_remontee_rec(T, N, B, i, X=None):
    if TriangulaireSup_Matrice(T, N) == False:
        print("La matrice n'est pas triangulaire supérieure")
        return None

    if X is None:
        X = [0 for _ in range(N)]

    if i == N - 1: 
        X[i] = B[i] / T[i][i]
        return X
    else:
        X = Algo_remontee_rec(T, N, B, i + 1, X)  
        calc_remontee(T, N, B, i, X)
        return X  

def calc_remontee(T,N,B,i,X):
     somme = 0

     for j in range(i + 1, N):
            somme += T[i][j] * X[j]
     X[i] = (B[i] - somme) / T[i][i]
     return X
    
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



if __name__ == "__main__":

 N = int(input("Enter the size of the matrix: "))
 T = [[0 for i in range(N)] for j in range(N)]
 B = [0 for i in range(N)]
 X= [0 for i in range(N)]

 
 while True:
     print("\n------ MATRIX OPERATIONS MENU ------")
     print("1- Lire system.")
     print("2- afficher system.")
     print("3- methode de remontee.")
     print("4- methode de descente.")
     print("5- methode cramer.")
     operation = int(input("Choose a number: "))
     if operation == 1:
         Lire_Systeme(T,B,N)
     if operation ==2:
         afficher_Systeme(T,B,N)
     if operation ==3:
         while True:
             print("1- remontee iterative. ")
             print("2- remontee recursive. ")
             operationrem = int(input("Choose a number: "))
             if operationrem == 1:
                 X = Algo_remontee(T,N,B)
             if operationrem == 2:
                 X = Algo_remontee_rec(T,N,B,0)
 
             print("la solution est: ")
             for i in range(N):
                 print("x[%d] = %f" % (i, X[i]))
 
             answer = input("autre fois (Y/N): ")
             if answer.strip().lower() in ["n", "no"]:
                 break
 
     if operation  == 4:
         while True:
             print("1- descent iterative. ")
             print("2- descent recursive. ")
             operationdesc = int(input("Choose a number: "))
             if operationdesc == 1:
                 Algo_descente(T,N,B)
             if operationdesc == 2:
                 Algo_descente_rec(T,N,B)  
 
             print("la solution est: ")
             for i in range(N):
                 print("x[%d] = %f" % (i, X[i]))
             answer = input("autre fois (Y/N): ")
             if answer.strip().lower() in ["n", "no"]:
                 break  
     if operation == 5:
         while True:
             print("1- Cramer iterative. ")
             print("2- Cramer recursive. ")
             operationcram = int(input("Choose a number: "))
             if operationcram == 1:
                 X = method_cramer(T,N,B)
             if operationcram == 2:
                 X = method_cramer_rec(T,N,B,0)  
 
             print("la solution est: ")
             for i in range(N):
                 print("x[%d] = %f" % (i, X[i]))
             answer = input("autre fois (Y/N): ")
             if answer.strip().lower() in ["n", "no"]:
                 break  
     Global_answer = input("Continue? (Y/N): ")
     if Global_answer.strip().lower() in ["n", "no"]:
         break             
     
 
   



























=======
from tp1_problem import *

def Lire_Systeme(T, B,N):
    Read_matrix(T, N)
    print("Enter the values of the vector B:")
    for i in range(N):
      B[i] = int(input("B[%d] = " % (i)))


def afficher_Systeme(T, B,N):
    print("The system is:")
    for i in range(N):
        for j in range(N):
            print(T[i][j], end=" ")
        print("| %d" % (B[i]))



def Algo_descente(T, N,B):
    if TriangulaireInf_Matrice(T, N)== False:
        print("la matrice n'est pas triangulaire inferieure")
        return None
    
    X= [0 for i in range(N)] 
    X[0]= B[0]/T[0][0]
    for i in range(1,N):
        somme=0
        for j in range(0,i):
            somme+= T[i][j]*X[j]
        X[i]=int((B[i]-somme)/T[i][i])
    return X

def Algo_descente_rec(T, N,B,i):
    if TriangulaireInf_Matrice(T, N)== False:
        print("la matrice n'est pas triangulaire inferieure")
        return None
    X= [0 for i in range(N)] 
    if i==0:
        X[0]= B[0]/T[0][0]
        return X
    else:
        X=Algo_descente_rec(T,N,B,i-1)
        calc_descent(T,B,X)
    return X

def calc_descent(T,B,X):
        somme=0
        for j in range(0,i):
            somme+= T[i][j]*X[j]
        X[i]=int((B[i]-somme)/T[i][i])



def Algo_remontee(T, N,B): 
    if TriangulaireSup_Matrice(T, N)== False:
        print("la matrice n'est pas triangulaire superieure")
        return None
    X= [0 for i in range(N)] 
    X[N-1]= B[N-1]/T[N-1][N-1]
    for i in range(N-2,-1,-1):
        somme=0
        for j in range(i+1,N):
            somme+= T[i][j]*X[j]
        X[i]=int((B[i]-somme)/T[i][i])
    return X

#def calc_remontee(T,N,B):
    
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




N = int(input("Enter the size of the matrix: "))
T = [[0 for i in range(N)] for j in range(N)]
B = [0 for i in range(N)]
X= [0 for i in range(N)]


while True:
    print("\n------ MATRIX OPERATIONS MENU ------")
    print("1- Lire system.")
    print("2- afficher system.")
    print("3- methode de remontee.")
    print("4- methode de descente.")
    print("5- methode cramer.")
    operation = int(input("Choose a number: "))
    if operation == 1:
        Lire_Systeme(T,B,N)
    if operation ==2:
        afficher_Systeme(T,B,N)
    if operation ==3:
        while True:
            print("1- remontee iterative. ")
            print("2- remontee recursive. ")
            operationrem = int(input("Choose a number: "))
            if operationrem == 1:
                Algo_remontee(T,N,B)
            if operationrem == 2:
                Algo_remontee_rec(T,N,B)
            answer = input("autre fois (Y/N): ")
            if answer.strip().lower() in ["n", "no"]:
                break

    if operation  == 4:
        while True:
            print("1- descent iterative. ")
            print("2- descent recursive. ")
            operationdesc = int(input("Choose a number: "))
            if operationdesc == 1:
                Algo_descente(T,N,B)
            if operationdesc == 2:
                Algo_descente_rec(T,N,B)  

            answer = input("autre fois (Y/N): ")
            if answer.strip().lower() in ["n", "no"]:
                break  
    if operation == 5:
        while True:
            print("1- Cramer iterative. ")
            print("2- Cramer recursive. ")
            operationcram = int(input("Choose a number: "))
            if operationcram == 1:
                method_cramer(T,N,B)
            if operationcram == 2:
                method_cramer_rec(T,N,B)  
            answer = input("autre fois (Y/N): ")
            if answer.strip().lower() in ["n", "no"]:
                break  
    Global_answer = input("Continue? (Y/N): ")
    if Global_answer.strip().lower() in ["n", "no"]:
        break             
    

   



























'''
B = [4,-2,1]
T = [[3,2,5],[0,1,-3],[0,0,1]]
X= [[0 for i in range(3)] for j in range(3)]
X =Algo_remontee(T,3,B)

print("x = ",X,"t")

B = [4,-2,1]
T = [[-2,0,0],[-1,3,0],[4,1,3]]
X= [[0 for i in range(3)] for j in range(3)]
X =Algo_descente(T,3,B)
print("x = ",X,"t")

B = [-4,6,-1,-15]
T = [[2,0,0,0],[-1,2,0,0],[4,-1,3,0],[1,3,-3,2]]
X= [[0 for i in range(4)] for j in range(4)]
X =Algo_descente(T,4,B)
print("x = ",X,"t")
'''
>>>>>>> 84859807c659802f5fb906ef0c51e814dbe570c0
