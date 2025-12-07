from fct_elimination import fct_elimination
from tp1_problem import *
from tp2_problem import *
import time

def triangulation(A, b):

    n = len(A)
    pivot_col = list(range(n))

    for k in range(n - 1):
        pivot = 0
        for i in range(k, n):
            for j in range(k, n):
                if abs(A[i][j]) > pivot:
                    pivot = abs(A[i][j])
                    l = i
                    c = j

        if l != k:
            A[k], A[l] = A[l], A[k]
            b[k], b[l] = b[l], b[k]

        if c != k:
            for i in range(n):
                A[i][k], A[i][c] = A[i][c], A[i][k]
            pivot_col[k], pivot_col[c] = pivot_col[c], pivot_col[k]

        pivot = A[k][k]
        fct_elimination(A, n, b, k, pivot)
        


    return A, b, pivot_col

def Algo_pivot_total_rec(A, b, n, k, pivot_col):
    if k >= n - 1:
        return

    pivot = 0
    for i in range(k, n):
        for j in range(k, n):
            if abs(A[i][j]) > pivot:
                pivot = abs(A[i][j])
                l = i
                c = j

    if l != k:
        A[k], A[l] = A[l], A[k]
        b[k], b[l] = b[l], b[k]

    if c != k:
        for i in range(n):
            A[i][k], A[i][c] = A[i][c], A[i][k]
        pivot_col[k], pivot_col[c] = pivot_col[c], pivot_col[k]

    pivot = A[k][k]
    fct_elimination(A, n, b, k, pivot)

    Algo_pivot_total_rec(A, b, n, k + 1, pivot_col)



def remontee(T, B, pivot_col):
    N = len(T)
    X = Algo_remontee(T, N, B)
    if X is None:
        return None

    x_final = [0] * N
    for i in range(N):
        x_final[pivot_col[i]] = X[i]

    return x_final

if __name__ == "__main__":
    T = [[1, 3, 3], [2, 2, 5], [3, 2, 6]]

    B = [-2, 7, 12]
    start_time = time.time()
    T_tri, B_tri, pivot_col = triangulation(T, B)
    X = remontee(T_tri, B_tri, pivot_col)
    end_time = time.time()

    print("La solution est :")
    for i in range(len(X)):
        print(f"x[{i}] = {X[i]:.2f}")

    print(f"Execution time: {end_time - start_time:.6f} seconds\n")
