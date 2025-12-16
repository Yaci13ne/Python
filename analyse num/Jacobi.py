def Jacobi(T, B, N_max):
    n = len(T)
    X= [0 for _ in range(n)]       

    for k in range(N_max):
        print(f"K = {k}")

        for i in range(n):
            somme = 0
            for j in range(n):
                if j != i:
                    somme += T[i][j] * X[j]

            X[i] = (B[i] - somme) / T[i][i]
            print(f"X[{i}] = {X[i]:.4f}")
    print("La solution approchée est :")
    for i in range(n):
        print(f"X[{i}] = {X[i]:.2f}")
    return X


def Jacobi_rec(T, B, N_max, X=None, k=0):
    n = len(T)
    if X is None:
        X = [0 for _ in range(n)]

    if k == N_max:
        print("La solution approchée est :")
        for i in range(n):
            print(f"X[{i}] = {X[i]:.2f}")
        return X

    print(f"K = {k}")
    X_new = [0 for _ in range(n)]

    for i in range(n):
        somme = 0
        for j in range(n):
            if j != i:
                somme += T[i][j] * X[j]

        X_new[i] = (B[i] - somme) / T[i][i]
        print(f"X[{i}] = {X_new[i]:.4f}")

    return Jacobi_rec(T, B, N_max, X_new, k + 1)


def calcule_jacobi(T, B, X,X_new,n):
    for i in range(n):
        somme = 0
        for j in range(n):
            if j != i:
                somme += T[i][j] * X[j]

        X_new[i] = (B[i] - somme) / T[i][i]
        print(f"X[{i}] = {X_new[i]:.4f}")


if __name__ == "__main__":
    
    N_max = int(input("Entrer le nombre d'itérations maximales : "))
    n = int(input("Entrer la taille de la matrice : "))
    
    T = [[0 for j in range(n)] for i in range(n)]
    B = [0 for i in range(n)]
    
    print("Entrer les éléments de la matrice T :")
    for i in range(n):
        for j in range(n):
            T[i][j] = float(input(f"T[{i}][{j}] = "))
    
    print("Entrer les éléments du vecteur B :")
    for i in range(n):
        B[i] = float(input(f"B[{i}] = "))
    
    Jacobi_rec(T, B, N_max)
