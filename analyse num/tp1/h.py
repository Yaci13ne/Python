def factoriel(n):
        f=1
        for i in range(1,n+1):
            f=f*i
        return(f)



a=int(input("Entrez un entier: "))
b=factoriel(a)
print(a,"!=",b)
print(a,"!=",factoriel(a))


