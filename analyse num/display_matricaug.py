def display_aug(A, b):
    n = len(A)
    for i in range(n):
        row_str = [f"{A[i][j]:.2f}" for j in range(n)]
        print(f"{row_str} | [{b[i]:.2f}]")
    print("\n")
    