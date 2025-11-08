def fct_elimination(T, N, B, k, pivot):
    for i in range(k + 1, N):
        q = T[i][k]
        T[i][k] = 0
        B[i] = B[i] - (q / pivot) * B[k]
        for j in range(k + 1, N):
            T[i][j] = T[i][j] - (q / pivot) * T[k][j]
    print(f"Matrice après élimination de la colonne {k}:")
    for i in range(N):
        print(T[i], " | ", B[i])
    print("\n")





    