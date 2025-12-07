<<<<<<< HEAD
N=int(input("Entrez la taille du Tableau: "))
T=[0 for i in range (0,N)]
print("Entrez les éléments du Tableau: ")
for i in range (0,N): 
    print("T[",i,"] =",end="")
    T[i]=int(input())
print("Afficher les éléments du Tableau comme vecteur: ")
print("T=",T)
print("Afficher les éléments du Tableau élément par élément: ")
for i in range (0,N):
    print("T[%d]=%d"%(i,T[i]))
S=0
P=1
for i in range (0,N): 
    S=S+T[i]
    P=P*T[i]
print("la somme des valeurs de T= ",S)
=======
N=int(input("Entrez la taille du Tableau: "))
T=[0 for i in range (0,N)]
print("Entrez les éléments du Tableau: ")
for i in range (0,N): 
    print("T[",i,"] =",end="")
    T[i]=int(input())
print("Afficher les éléments du Tableau comme vecteur: ")
print("T=",T)
print("Afficher les éléments du Tableau élément par élément: ")
for i in range (0,N):
    print("T[%d]=%d"%(i,T[i]))
S=0
P=1
for i in range (0,N): 
    S=S+T[i]
    P=P*T[i]
print("la somme des valeurs de T= ",S)
>>>>>>> 84859807c659802f5fb906ef0c51e814dbe570c0
print("le produit des valeurs de T= ",P)