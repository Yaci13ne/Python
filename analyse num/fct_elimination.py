from display_matricaug import display_aug


def fct_elimination(T, N, B, k, pivot):
    print("le system est :")
    display_aug(T, B)
    

    for i in range(k + 1, N):
        q = T[i][k]
        T[i][k] = 0
        B[i] = B[i] - (q / pivot) * B[k]
        for j in range(k + 1, N):
            T[i][j] = T[i][j] - (q / pivot) * T[k][j]

    # Print iteration
    print(f"Iteration {k+1}:, k = {k+1}, pivot = {pivot:.2f}")
    for i in range(N):
        # Round each element of T[i] to 2 decimals for printing
        row_str = [f"{x:.2f}" for x in T[i]]
        print(f"{row_str} | [{B[i]:.2f}]")
    print("\n")
