

from norm_diff import norme_diff


def Gauss_Seidel_rec(T, B, N_max, epsilon, X=None, k=0):
    n = len(T)
    if X is None:
        X = [0 for _ in range(n)]

    if k >= N_max:
        return X
    
    X_new = X.copy()
    calcule_seidel(T, B, X_new,n)
    
    if norme_diff(X_new, X) < epsilon:
        print(f"Arrêt : ||X_new - X|| = {norme_diff(X_new, X):.6f} < epsilon")
        return X_new


    print(f"K = {k}")
    return Gauss_Seidel_rec(T, B, N_max, epsilon,X_new, k + 1)

def calcule_seidel(T, B, X,n):

    for i in range(n):
        somme1 = 0
        for j in range(i):
            if j != i:
                somme1 += T[i][j] * X[j]
        somme2=0
        for j in range(i+1, n):
            somme2 += T[i][j] * X[j]
        X[i] = (B[i] - somme1 - somme2) / T[i][i]
        print(f"X[{i}] = {X[i]:.4f}")



if __name__ == "__main__":
    N_max = int(input("Entrer le nombre d'itérations maximales : "))
    epsilon = float(input("Entrer epsilon : "))
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
    X = Gauss_Seidel_rec(T, B, N_max, epsilon, None,0)