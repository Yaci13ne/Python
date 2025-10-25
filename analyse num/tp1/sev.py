N=int(input("Entrez le nombre de lignes de la matrice: "))
M=int(input("Entrez le nombre de colonnes de la matrice: "))
T=[[0 for j in range(0,M)] for i in range(0,N)]
print("Introduisez les %d éléments de la matrice:" %(N*M))
for i in range(0,N):
        for j in range(0,M):
                print("T[%d][%d]="%(i,j),end="") 
                T[i][j]=int(input())
print("Affichez la matrice sous fomre matricielle :")
for i in range(0,N):
         print()
         for j in range(0,M):
            print(T[i][j],end=" ")
         print()
Nb_pairs=0
Nb_impairs=0
for i in range(0,N):
        for j in range(0,M):
            if(T[i][j]%2==0):
                Nb_pairs=Nb_pairs+1
            else:
                Nb_impairs=Nb_impairs+1
print("Nombre des entiers pairs = %d "%(Nb_pairs))
print("Nombre des entiers impairs = %d "%(Nb_impairs))
