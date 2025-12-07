from Jacobi import calcule_jacobi
from norm_diff import norme_diff


def Jacobi_rec(T, B, N_max, epsilon, X=None, k=0):
    n = len(T)
    if X is None:
        X = [0 for _ in range(n)]

    if k >= N_max:
        return X

    print(f"K = {k}")

    X_new = X.copy()
    calcule_jacobi(T, B, X, X_new, n)

    if norme_diff(X_new, X) < epsilon:
        print(f"Arrêt : ||X_new - X|| = {norme_diff(X_new, X):.6f} < epsilon")
        return X_new

    return Jacobi_rec(T, B, N_max, epsilon, X_new, k + 1)


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

    X = Jacobi_rec(T, B, N_max, epsilon, None, 0)