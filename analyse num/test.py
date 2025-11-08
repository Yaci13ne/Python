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


def calc_descent(T, N, B, i, X):
    somme = 0
    for j in range(0, i):
        somme += T[i][j] * X[j]
    X[i] = (B[i] - somme) / T[i][i]


def TriangulaireInf_Matrice(T, N):
    for i in range(N):
        for j in range(i + 1, N):
            if T[i][j] != 0:
                return False
    return True


T = [[8, 0, 0],
     [2, 1, 0],
     [1, 2, 3]]

B = [1, 2, 3]

X = Algo_descente_rec(T, 3, B, 2)
print(X)
