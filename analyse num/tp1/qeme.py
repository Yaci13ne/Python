N = int(input("Enter value N ="))

print("le tableau de multiplication de N :")
for i in range (0,11):
    print(N, "*" ,i, "=" ,N*i)
N=int(input("Entrez un entier N= "))
f=1
for i in range (1,N+1):
    f=f*i
print(N,"!=",f)