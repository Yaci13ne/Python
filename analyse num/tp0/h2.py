<<<<<<< HEAD
def Lire_Tableau(t,n): 
    for i in range (0,N): 
            print("T[%d]= "%(i),end="")
            T[i]=int(input())


def Afficher_Tableau(t,n): 
     for i in range (0,N): 
          print("T[%d]=%d"%(i,T[i]))
def Lire_Matrice(t,n,m): 
     for i in range(0,n):
        for j in range(0,m):
            print("t[%d][%d]="%(i,j),end="") 
            t[i][j]=int(input())
def Afficher_Matrice(t,n,m): 
     for i in range(0,n):
        print()
        for j in range(0,m):
            print(t[i][j],end=" ") 
     print()


N=int(input("Entrez la taille du Tableau: "))
T=[0 for i in range (0,N)]
print("Entrez les éléments du Tableau: ")
Lire_Tableau(T,N)
print("Afficher les éléments du Tableau élément par élément: ")
Afficher_Tableau(T,N)
N=int(input("Entrez le nombre de lignes de la matrice: "))
M=int(input("Entrez le nombre de colonnes de la matrice: "))
A=[[0 for j in range(0,M)] for i in range(0,N)]
B=[[0 for j in range(0,M)] for i in range(0,N)]
C=[[0 for j in range(0,M)] for i in range(0,N)]
print("Introduisez les éléments de la matrice A:")
Lire_Matrice(A,N,M)
print("Afficher la Matrice A:")
=======
def Lire_Tableau(t,n): 
    for i in range (0,N): 
            print("T[%d]= "%(i),end="")
            T[i]=int(input())


def Afficher_Tableau(t,n): 
     for i in range (0,N): 
          print("T[%d]=%d"%(i,T[i]))
def Lire_Matrice(t,n,m): 
     for i in range(0,n):
        for j in range(0,m):
            print("t[%d][%d]="%(i,j),end="") 
            t[i][j]=int(input())
def Afficher_Matrice(t,n,m): 
     for i in range(0,n):
        print()
        for j in range(0,m):
            print(t[i][j],end=" ") 
     print()


N=int(input("Entrez la taille du Tableau: "))
T=[0 for i in range (0,N)]
print("Entrez les éléments du Tableau: ")
Lire_Tableau(T,N)
print("Afficher les éléments du Tableau élément par élément: ")
Afficher_Tableau(T,N)
N=int(input("Entrez le nombre de lignes de la matrice: "))
M=int(input("Entrez le nombre de colonnes de la matrice: "))
A=[[0 for j in range(0,M)] for i in range(0,N)]
B=[[0 for j in range(0,M)] for i in range(0,N)]
C=[[0 for j in range(0,M)] for i in range(0,N)]
print("Introduisez les éléments de la matrice A:")
Lire_Matrice(A,N,M)
print("Afficher la Matrice A:")
>>>>>>> 84859807c659802f5fb906ef0c51e814dbe570c0
Afficher_Matrice(B,N,M)